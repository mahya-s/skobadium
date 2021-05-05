from flask import Flask
from flask_restful import Api
from authz.config.config import Config

api = Api()

from authz import resource

def create_app():
	
	app = Flask(__name__)
	
	app.config.from_object(Config) #load configs from env variables.

	api.init_app(app)
	
	return app
