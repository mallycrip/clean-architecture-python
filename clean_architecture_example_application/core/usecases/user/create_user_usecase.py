from __future__ import annotations

from clean_architecture_example_application.core.domain.entity.user import User
from clean_architecture_example_application.core.domain.repository.user_repository import UserRepository
from clean_architecture_example_application.core.usecases.usecase import UseCase


class CreateUserUseCase(UseCase):
    def __init__(self, user_repository):
        self._user_repository: UserRepository = user_repository

    def execute(self, input: CreateUserUseCase.InputValues):
        self._user_repository.persist(
            User(input.id, input.pw, input.name, input.age, input.job)
        )
        return self.OutputValues()

    class InputValues(UseCase.InputValues):
        def __init__(self, id, pw, name, age, job):
            self.id = id
            self.pw = pw
            self.name = name
            self.age = age
            self.job = job

    class OutputValues(UseCase.OutputValues):
        pass
