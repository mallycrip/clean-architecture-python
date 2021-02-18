from clean_architecture_example_application.core.mapper import Mapper
from clean_architecture_example_application.core.usecases.usecase import UseCase
from clean_architecture_example_application.core.usecases.usecase_executor import UseCaseExecutor


class UseCaseExecutorImpl(UseCaseExecutor):
    def execute(self, usecase: UseCase, input: UseCase.InputValues, mapper: Mapper):
        return mapper.map(UseCase.execute(input))
