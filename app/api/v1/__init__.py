#imports the resources found in flask and flask_restful

from flask import Flask, Blueprint
from flask_restful import Api
from .views import MyRedflag, MyRedflags

# Initializes the app with the configurations

version_1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_1)





    
