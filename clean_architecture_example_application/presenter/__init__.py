from clean_architecture_example_application.presenter.di.controllers import mock_controller_object


class MockApplication:
    def __init__(self):
        self._address = str()
        self._port = int()

    def register_controller(self, controller, path: str):
        # Register Controller
        pass

    def run(self, **configs):
        self._address = configs["host"]
        self._port = configs["port"]

        if self._address and self._port:
            print(f"*** Mock Application is run in {self._address}:{self._port}")
        else:
            print("*** Check an address and port")


def create_app():
    _app = MockApplication()

    register_controllers(_app)
    register_extensions(_app)

    return _app


def register_controllers(app: MockApplication):
    app.register_controller(mock_controller_object, "/")
    app.register_controller(mock_controller_object, "/index")


def register_extensions(app: MockApplication):
    # TODO
    pass
