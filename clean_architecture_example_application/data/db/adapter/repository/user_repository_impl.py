from clean_architecture_example_application.core.domain.repository.user_repository import UserRepository
from clean_architecture_example_application.data.db.alchemy import alchemy
from clean_architecture_example_application.data.db.alchemy.repository import AlchemyUserRepository
from clean_architecture_example_application.data.db.adapter.mapper.user_repository_mapper import map


class UserRepositoryImpl(UserRepository):
    def __init__(self):
        self._alchemy_user_repository = AlchemyUserRepository(alchemy)

    def persist(self, user):
        self._alchemy_user_repository.persist(map(user))

    def find_by_id(self, id):
        self._alchemy_user_repository.find_by_id(id)