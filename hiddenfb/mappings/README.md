# Object Mapping

This module contains classes handle mapping related objects. This often takes place between layers (database objects to domain models, for example) but has other use cases.

## Conventions
```
class TargetMapper:
    def from_source(self, source: Source) -> Target:
        ...
    
    def _parse_tags(self, tags: List[int]) -> List[Tag]:
        ...
```

This is a minimal implementation of a mapper class. Note that the target is always in the class name, and the source is in the method name. (Here, fake `Target` and `Source` classes are used for clarity). Other helper methods can be defined if more complex logic is required (for example, the `_parse_tags` method above).