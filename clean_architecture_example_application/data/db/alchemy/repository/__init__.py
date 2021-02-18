from clean_architecture_example_application.data.db.alchemy import alchemy
from clean_architecture_example_application.data.db.alchemy.repository.alchemy_user_repository import \
    AlchemyUserRepository

alchemy_user_repository = AlchemyUserRepository(alchemy=alchemy)