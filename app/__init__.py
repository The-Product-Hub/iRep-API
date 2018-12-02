
import os
from flask import Flask
from flask_restful import Resource, Api
from .api.v1 import version_1 as v1
from .api.v1.views import MyRedflags, MyRedflag

def create_app(config_name):
    app = Flask(__name__)
    api =  Api(app)
    app.register_blueprint(v1)

    api.add_resource( MyRedflags, "/redflags")
    api.add_resource( MyRedflag, "/redflags/<int:id>")
    
    return app