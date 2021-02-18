from clean_architecture_example_application.core.mapper import Mapper
from clean_architecture_example_application.core.usecases.usecase import UseCase


class MockMapper(Mapper):
    def map(self, input: UseCase.OutputValues):
        # controller_response_field = input.value
        return {
            "Status": 200
        }