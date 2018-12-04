from flask_restful import Api, Resource
from flask import jsonify, make_response, request
from models import MyRedflagModels, redflag_records
from datetime import datetime

class MyRedflags():
    """docstring for MyRedflags"""

redflag_records = []

def __init__(self):
    self.db = redflag_records

def post(self):
        redflag = self.redflag_model.post()
        return redflag

def view(self):
    return self.db

def post_redflag(self):
    self.db.append()

class MyRedflag(Resource):
    """ docstring for Myredflag"""

def find_by_id(self, id):

    record = [record for record in self.db if record['Id'] == id]

    return record
    
def delete(self, id):
    record = [record for record in redflag_records if record['Id'] == id]
    if len(record) == 0:

        response = jsonify({
            'status' : 404,
            'message' : "Record not found"

        })
    return response

    

