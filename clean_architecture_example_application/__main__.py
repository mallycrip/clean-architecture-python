from clean_architecture_example_application.config.run_setting import RUN_SETTINGS
from clean_architecture_example_application.presenter import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(**RUN_SETTINGS)
