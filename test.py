#!/usr/bin/python3.8

from authz import create_app

app = create_app()

if __name__ == "__main__":
	app.run()
