from clean_architecture_example_application.core.usecases.usecase import UseCase
from clean_architecture_example_application.core.usecases.usecase_executor import UseCaseExecutor
from clean_architecture_example_application.core.usecases.user.create_user_usecase import CreateUserUseCase
from clean_architecture_example_application.presenter.controller.mapper.mock_mapper import MockMapper


class MockController:
    def __init__(self, usecase_executor, usecase):
        self.name = "Mock Controller"
        self.usecase_executor: UseCaseExecutor = usecase_executor
        self.usecase: UseCase = usecase

    def post(self, header, body):
        input = CreateUserUseCase.InputValues()
        input.id = body.id
        input.pw = body.pw

        return self.usecase_executor.execute(self.usecase, input, MockMapper())