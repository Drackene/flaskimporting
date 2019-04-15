from flask import Flask
from flask_restful import Resource, Api
from apitest.blueprints.home import home
from apitest.blueprints.api import api_bp

# Set up logging, remove for production
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

# instance_relative_config tells flask to look for an instance module that's in the same folder depth as the main module
app = Flask(__name__, instance_relative_config=True)
api = Api(app)
# look for a settings.py file in the config folder
app.config.from_object('config.settings')

# look in the instance folder for settings.py.  Silent = True means don't crash if file doesn't exist
# as instance settings is loaded after config settings, the instance settings will overide the config settings if duplicate settings exist
app.config.from_pyfile('settings.py', silent=True)

app.register_blueprint(home)
app.register_blueprint(api_bp)

from app import views
