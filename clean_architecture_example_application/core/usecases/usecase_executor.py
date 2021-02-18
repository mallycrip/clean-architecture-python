from abc import ABCMeta, abstractmethod

from clean_architecture_example_application.core.mapper import Mapper
from clean_architecture_example_application.core.usecases.usecase import UseCase


class UseCaseExecutor(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, usecase: UseCase, input: UseCase.InputValues, mapper: Mapper): pass