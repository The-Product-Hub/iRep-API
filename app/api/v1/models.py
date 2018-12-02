from flask import make_response, jsonify, request
import datetime

redflag_records = []

class MyRedflagModels():
    def __init__(self):
        self.db = redflag_records

    def save(self,CreatedBy, IncidenceType, Location, Status, Comment ):
        data = {
            "Id" : len(self.db) + 1,
            "CreatedBy" : CreatedBy,
            "IncidenceType": IncidenceType,
            "Location" : Location,
            "Status" : Status,
            "Comment" : Comment
            }
        self.db.append(data)
        return self.db
    
    def view(self):
        return self.db
  
    def find_by_id(self, id):

        record = [record for record in self.db if record['Id'] == id]

        return record
    
    def post_redflag(self):
        data = request.get_json(force=True)
        CreatedBy = data['CreatedBy']
        IncidenceType = data['IncidenceType']
        Location = data['Location']
        Status = data['Status']
        Comment = data['Comment'] 
         
        resp = self.save(CreatedBy, IncidenceType, Location, Status, Comment)
        return {
            "data":resp,
            "message":"Your Report Has Been Saved Successfully"
        }  



       