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

### Filters


## Testing

## Usage



### Dependency Injection

