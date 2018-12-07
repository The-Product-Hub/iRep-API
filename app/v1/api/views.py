from flask_restful import Resource
from flask import jsonify, make_response, request
from .app.v1.api import MyRedflagModels


db = db_records()

class MyRedflags(Resource):
    """docstring for MyRedflags"""

def __init__(self):
    self.db = db_records()

def get(self):
    response = self.db.get_redflag()
    return response

def post(self):
    data = request.get_json()
    createdOn = data['createdOn']
    createdBy = data['createdBy']
    Type = data['Type']
    Location = data['Location']
    Status = data['Status']
    Uploads = data['Uploads']
    Comment = data['Comment']

    record = self.db.save()
    return make_response(record)

def delete(self):
    response = self.db.deleteMyRedflags()
    return make_response(response)

class MyRedflag(Resource):
    """ docstring for Myredflag"""

def __init__(self):
    self.db = db_records()

def get_id(self, id):
    response = self.db.get_by_id(id)
    return make_response(jsonify(response))

def patch(self, id):
    redflag = self.db.patch(id)
    return redflag
    
def delete_by_id(self, id):
    response = db.deleteMyRedflag(id)
    return make_response(response)


    

