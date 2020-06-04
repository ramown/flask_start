"""This file intializes a Python module. Without it, Python will not
recognize the app directory as a module."""

from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from app import views


app.config.from_object('config')