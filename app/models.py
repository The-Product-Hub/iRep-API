from flask import make_response, jsonify, request
from datetime import date

db_records = []

class MyRedflagModels():
<<<<<<< HEAD
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
=======
    
    def __init__(self):
        self.db = db_records

    def save(self, createdOn, createdBy, Type, Location, Status, Uploads, Comment):
        data = {}
        data['id'] = len(self.db) + 1
        data['createdOn'] = date.today()
        data['createdBy'] = createdBy
        data['Type'] = Type
        data['Location'] = Location
        data['Status'] = Status
        data['Uploads'] = Uploads
        data['Comment'] = Comment
        db_records.append(data)
        records = len(self.db)
        print(records)
        return jsonify({
            "status" : 201,
            "message" : "Record created succesfully"
        })

    def get_redflags(self):
        if len(db_records) == 0:
            return jsonify({
                "Status" : 200,
                "message" : "No Record created"
            })

    def get_by_id(self, id):
        for record in db_records:
            if record['id'] == (id): 
                return record
            else:
                return jsonify({"status": 404,
                        "message": "Record does not exist."})

    def patch (self, id):
        for record in db_records:
            if record(id) == (id):
                return jsonify({
                    "status" : 201,
                    "message" : "Record has been sucessfully updated."
                })
            else:
                return jsonify({
                    "status" : 404,
                    "message" : "Record does not exist."})

    def delete(self, id):
        for record in db_records:
            if record[id] == (id):
                db_records.remove(db_records.index(record))
                return jsonify({
                    "status" : 204,
                    "message" : "Record has been sucessfully deleted."
                })
            else:
                return jsonify({
                    "status" : 404,
                    "message" : "Record does not exist."
                }) 
>>>>>>> 76749cb4942c9f25808ec9ebf08edbbeb02f92f5
