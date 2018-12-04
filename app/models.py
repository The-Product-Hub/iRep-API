from flask import make_response, jsonify, request
import datetime

redflag_records = []

class MyRedflagModels():
    def __init__(self):
        self.db = redflag_records

    def save(self,CreatedBy, IncidenceType, Location, Status, Comment ):
        data = {
            "Id" : len(self.db) + 1,
            "createdOn" : createdOn,
            "createdBy" : createdBy,
            "Type": Type,
            "Location" : Location,
            "Status" : Status,
            "Uploads" : Uploads,
            "Comment" : Comment
            }
        self.db.append(data)
        return self.db

    def post_redflag(self):
        data = request.get_json()
        createdOn = datetime['Datetime']
        createdBy = data['createdBy']
        Type = data['Type'],
        Location = data['Location'],
        Status = data['Status'],
        Uploads = data['Uploads'],
        Comment = data['Comment']

        redflag_records.append(post-record)
        return jsonify{
            "status":201,
            "message":"Your Report Has Been Saved Successfully"
        }  

    def get(self, id):
        self.id = id
        response = self.model.find_by_id(self.id)
        return make_response (jsonify({"My red-flag" : response}), 200)
        record = [record for record in redflag_records if record['Id'] == id]
        if len(record) == 0:
             = jsonify({
                'status': 404,
                'message': "No redflag found"
            })

    def find_by_id(self, id):
        for redflag in redflags:
            if redflag['id'] != id: 
                return {"status": 404,
                        "message": "Redflag not found"}
            else:
                return jsonify({"status": 200,
                        "Redflag": redflag})

    def patch (self, id):
        data = request.get_json(force=True)
        record = [record for record in redflag_records if record['Id'] == id]
        if len(record) == 0:
            response = jsonify({
                'status' : 404,
                'message' : "No redflag found."
            })

            response.status_code = 404
        else:
            for k in data.keys():
                if data[k] is not None:
                    pass
            

            response = jsonify({
                'status' : 200,
                'message' : "redflag updated successfully."
            })

            response.status_code = 200
        return response                        


    def delete(self, id):
        data = request.get_json()
        for redflag in redflags:
            if redflag['id'] == id:
                redflags.remove(redflag)
                return jsonify({"status": 200,
                        "message": "Redflag has been deleted"})
            else:
                return jsonify({"status": 404,
                        "message": "Redflag does not exist"})        