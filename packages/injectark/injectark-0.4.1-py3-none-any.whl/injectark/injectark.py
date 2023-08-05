from inspect import signature
from typing import Any, Dict, Optional
from .factory import Strategy, Factory


class Injectark:
    def __init__(self, strategy: Strategy = None,
                 factory: Factory = None,
                 parent: 'Injectark' = None) -> None:
        self.parent = parent
        self.factory = factory
        self.strategy = strategy
        self.registry: Dict[str, Any] = {}

    def __getitem__(self, key: str):
        instance = self.resolve(key)
        if not instance:
            raise KeyError(
                f"The '{key}' resource can't be resolved by the injector.")
        return instance

    def resolve(self, resource: str):
        fetched = self._registry_fetch(resource)
        if fetched:
            return fetched

        persist = not self.strategy.get(resource, {}).get('ephemeral', False)
        instance = self._dependency_build(resource, persist)

        return instance

    def forge(self, strategy, factory):
        return Injectark(parent=self, strategy=strategy, factory=factory)

    def _registry_fetch(self, resource: str):
        fetched = False
        rule = self.strategy.get(resource, {})
        if rule.get('unique'):
            return fetched

        if resource in self.registry:
            fetched = self.registry[resource]
        else:
            parent = self.parent
            fetched = parent._registry_fetch(resource) if parent else False

        return fetched

    def _dependency_build(self, resource: str, persist=True):
        instance = None
        rule = self.strategy.get(resource, {'method': ''})
        builder = self.factory.extract(rule['method'])

        if builder:
            dependencies = [
                value.annotation.__name__ for key, value in
                signature(builder).parameters.items() if key != 'return']

            dependency_instances = []
            for dependency in dependencies:
                dependency_instance = self[dependency]
                dependency_instances.append(dependency_instance)

            instance = builder(*dependency_instances)

        else:
            instance = (self.parent._dependency_build(resource, persist)
                        if self.parent else instance)

            persist = (persist and self.strategy.get(
                resource, {}).get('unique', False))

        if persist:
            self.registry[resource] = instance

        return instance
