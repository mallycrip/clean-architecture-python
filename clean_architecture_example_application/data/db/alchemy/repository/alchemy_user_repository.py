class AlchemyUserRepository:
    def __init__(self, alchemy):
        self._alchemy = alchemy

    def persist(self, user):
        self._alchemy.save(user)

    def find_by_id(self, id):
        return self._alchemy.filter(id=id).first()