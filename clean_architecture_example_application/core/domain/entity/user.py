class User:
    def __init__(self, id, password, name, age, job):
        self._id = id
        self._password = password
        self._name = name
        self._age = age
        self._job = job

    def grow(self, age):
        self._age += 1
        return self

