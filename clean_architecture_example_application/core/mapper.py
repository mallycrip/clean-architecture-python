from abc import ABCMeta, abstractmethod

from clean_architecture_example_application.core.usecases.usecase import UseCase


class Mapper(metaclass=ABCMeta):
    @abstractmethod
    def map(self, input: UseCase.OutputValues): pass