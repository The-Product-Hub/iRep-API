from flask_restful import Api, Resource
from flask import jsonify, make_response, request
from .models import MyRedflagModels, redflag_records
#import datetime

class MyRedflags(Resource):
    """docstring for MyRedflags"""

    def __init__(self):
        self.model = MyRedflagModels()

    def get(self):
        redflags=self.model.view()
        return make_response(jsonify({"My Red-Flag records": redflags}), 200)
       
       

    def post(self): 
        post_record = self.model.post_redflag()    
        return make_response(jsonify({
           "status" : 201,
           "data" : post_record
        }), 201)  


class MyRedflag(Resource):
    """ docstring for Myredflag"""

    def __init__(self):
        self.db = redflag_records
        self.model = MyRedflagModels()
        # self.id = id

    def get (self, id):
        self.id = id
        resp = self.model.find_by_id(self.id)
        return make_response (jsonify({"My red-flag" : resp}), 200)
 
    def patch (self, id):
        data = request.get_json(force=True)
        record = [record for record in redflag_records if record['Id'] == id]
        if len(record) == 0:
            response = jsonify({
                'status' : 404,
                'data' : [{
                    "Id" : id,
                    "msg" : "redflag not found"

                }]

            })

            response.status_code = 404
        else:
            for k in data.keys():
                if data[k] is not None:
                    pass
            

            response = jsonify({
                'status' : 200,
                'data' : [{
                    "id" : id,
                    "msg" : "redflag updated successfully"

                }]
            })
            response.status_code = 200
        return response
        

    def delete(self, id):
        msg = 'Not Found'
        record = [record for record in redflag_records if record['Id'] == id]
        if len(record) == 0:
            return jsonify ({'status': 404, 'error': msg})
        self.db.remove(record[0])
        return jsonify ({
            'status' : 200,
            'data' : [{
                "Id" : id,
                "message" : "redflag deleted sucessfully"
            }]
        })
        # response.status_code = 200
        # success_msg = {'id' : redflag_id,'message' : " Red-flag record has been deleted"}

        # return make_response(jsonify({"status" : 204, "data" : }), 204)
        # return make_response(jsonify({"status" : 404, "error" : "Item does not exist"}), 404)

    
