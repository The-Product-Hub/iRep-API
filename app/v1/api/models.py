from flask import make_response, jsonify, request
from datetime import date

db_records = []

class MyRedflagModels():
    
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