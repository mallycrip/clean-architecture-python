from clean_architecture_example_application.core.domain.entity.user import User
from clean_architecture_example_application.core.domain.repository.user_repository import UserRepository
from clean_architecture_example_application.core.usecases.usecase import UseCase


class CreateUserUseCase(UseCase):
    def __init__(self, user_repository):
        self._user_repository: UserRepository = user_repository

    def execute(self, input):
        self._user_repository.persist(
            User(input.id, input.pw, input.name, input.age, input.job)
        )
        return self.OutputValues()

    class InputValues(UseCase.InputValues):
        id = str()
        pw = str()
        name = str()
        age = int()
        job = str()

    class OutputValues(UseCase.OutputValues):
        pass
