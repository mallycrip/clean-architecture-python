from abc import ABCMeta, abstractmethod


class UseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, input): pass

    class InputValues(metaclass=ABCMeta): pass

    class OutputValues (metaclass=ABCMeta): pass