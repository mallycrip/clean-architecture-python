from clean_architecture_example_application.data.db.alchemy.models.AlchemyUser import AlchemyUser


def map(user):
    return AlchemyUser(user._id, user._password, user._name)