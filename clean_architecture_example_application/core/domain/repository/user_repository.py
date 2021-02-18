from abc import abstractmethod, ABCMeta


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def persist(self, user): pass

    @abstractmethod
    def find_by_id(self, id): pass