# Repositories

Repositories facilitate the access to persisted data in the form of domain models. This separation of concerns reduces dependencies and allows the persistence layer to change without affecting other layers. Further, domain modeling is free from technical constraints related to persistence, and the data can be stored in the most optimal way.

## Design Conventions

### Base Repositories

The abstract base `Repository` classes are intended to be minimal, standardizing only the most basic requirements and enabling basic type safety. Subclasses such as `FileRepository`or `DatabaseRepository` define broad categories for persisted data sources as their names imply. Again, these should be kept as minimal as possible to allow necessary flexibility in the concrete repository implementations.

## Model Repositories

Repositories are used to access domain models. Repositories should only be used for top-level domain models (aggregate roots or standalone entities and value objects). To conform to DDD principles, a repository should create full aggregate roots. All models contained within an aggregate root should be accessed and created within the aggregate's repository. In other words, the contained models should not have their own repositories.

An abstract model repository should only define an interface. It should not implement any specific functionality or impose any restrictions on data sources, etc. Therefore, a abstract model repository class should not inherit from `Repository`, and its methods should be abstract.

```
class AggregateRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Aggregate]:
        ...
```

Concrete implementations can inherit from any repository subclass. This allows multiple implementations - and therefore methods of persistence - to exist simultaneously. For example, one concrete class to access data from a database, and one to access data from file storage.

```
class AggregateDatabaseRepository(DatabaseRepository, ABC):
    def get_all(self) -> List[Aggregate]:
        # Concrete implementation here
        ...

class AggregateFileRepository(FileRepository, ABC):
    def get_all(self) -> List[Aggregate]:
        # Concrete implementation here
        ...
```

### Entity Caching

Identity is a central concept of entities. The characteristics of an entity may change, but (unlike value objects) these changes do not change an entity into a fundamentally different entity. Persistence plays a large part in ensuring this consistency, but measures must also be taken within the application.

Specifically, only _one_ instance of an entity should exist in a transaction (no reinstantiation). Any services which use an entity should be passed the _same_ instance. Consider a situation where an entity is modified in some way. Any other code within the same transaction should be aware of these changes, ensuring that code is always working with the most current state. Furthermore, if multiple instances existed at the same time, each instance may be changed in _different_ ways, resulting in not just an out-of-date object, but a completely invalid state which was never intended.

#### Implementing Entity Caching

Because of the wide range of use-cases that repositories must cover, it is very difficult to enforce or automate entity caching through code. Therefore, it is up to the developer to ensure that model requirements are documented properly, and that all repository implementations are thoroughly tested for consistency with regard to entity instances.

Concrete repositories for entities should make use of the `EntityCache` class to handle model instances by subclassing `EntityCache` and implementing the `_get_primary_key()` method. It's worth noting that this logic is specific to entity caching in the persistence layer, and therefore does not need to be generalized or defined in a more central location - alongside the entity cache is fine. 

For models with complex primary keys, it is valid to define a `PrimaryKey` class for the cache to use. This key should only use primitive types (no domain models) so that other layers can also interact with the class. For example, it's vital to be able to use information in a database ORM object to access cached domain models.

### Filters

Separate `Filter` classes should be used to define the criteria which users use to access specific subsets of data. This serves to reduce the number of functions required for each repository class while leaving filtering requirements open to extension as the domain layer evolves. These filters should be defined in the database layer, but using language from the domain layer. This will ensure that the domain models are accessed using language and concepts from the domain rather than the persistence layer.

```
class ModelRepository(ABC):
    @abstractmethod
    def get_all(self, filters: ModelFilter | None = None) -> List[Model]:
        ...
```

#### Filter Implementation

Filters should be implemented using the Builder pattern to allow users the flexibility needed to handle the wide range of data access requirements. A concrete Filter should define filter criteria as private class attributes. Each criteria will use a set to store values in the query, with a public method to add values to the underlying set. This set implementation allows `None` to be a valid filter criteria for optional attributes, while multiple calls to the same filter method will just add values to the set. The values for each criteria will treated as part of an "or" operation.

```
class ModelFilter(Filter):
    def __init__(self):
        self._names: set[str] = set()
        self._categories: set[str] = set()

    def name(self, names: list[str]) -> ModelFilter:
        self._names.update(names)
        return self
    
    def category(self, categories: list[str]) -> ModelFilter:
        self._categories.update(categories)
        return self


filters = ModelFilter().name(["test"]).category(["thing"])
```

It is difficult to enforce integration of Filters in Repository code. It is up to the developers to update Repositories when Filters change. This is a realistic expectation, since extensions to Filter implementation will be driven by larger changes to data access requirements.

## Testing

## Usage

For anything beyond the simplest, single step use cases, repository instances should be injected using an Inversion of Control container. This ensures that entities are cached consistently within each session, and efficiently across multiple concurrent sessions.
