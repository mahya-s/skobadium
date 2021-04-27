from flask import Flask

from authz.config.config import Config

def create_app():
	
	app = Flask(__name__)
	
	app.config.from_object(Config) #load configs from env variables.
	
	return app
