from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy





import helpers
from config import DevelopmentConfig, basedir

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

helpers.register_blueprints(app, 'controllers', [basedir + '/controllers'])

from model.users import Users

if __name__ == '__main__':
    app.run(debug=True)
