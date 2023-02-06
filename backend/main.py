from flask import Flask
from databases.setup_database import SetupDatabase
from configs.main_config import APP_CONFIG, API_PREFIX, API_VERSION
from controllers.movies_controller import movies


def main():
    app = Flask(__name__)
    db = SetupDatabase()
    db.initialize_db()
    app.register_blueprint(movies, url_prefix=f"/{API_PREFIX}/{API_VERSION}/")
    app.run(**APP_CONFIG)


if __name__ == "__main__":
    main()
