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
    
    def view(self):
        return self.db
  
    def find_by_id(self, id):

        record = [record for record in self.db if record['Id'] == id]

        return record

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

    def find_by_id(self, id):
        for redflag in redflags:
            if redflag['id'] != id: 
                return {"status": 404,
                        "message": "Redflag not found"}
            else:
                return jsonify({"status": 200,
                        "Redflag": redflag})

    
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
         
# return self.save(CreatedBy, IncidenceType, Location, Status, Comment)clear
# return {
            
#             "message":"Your Report Has Been Saved Successfully"
#         }  

#         # return {
            
        #     "message":"Your Report Has Been Saved Successfully"
        # }  



    #   record=next (filter[lambda record:record['Id']==Id, self.db])



    # class RedflagModels():
    # def __init__(self):
    #     pass
        
        
    # def get_one(self, id):
    #     for redflag in redflags:
    #         if redflag['id'] != id: 
    #             return {"status": 404,
    #                     "message": "Redflag not found"}
    #         else:
    #             return jsonify({"status": 200,
    #                     "Redflag": redflag})


    # def post_one(self):
    #     data = request.get_json()
    #     redflag = {
    #         'id': len(redflags)+1,
    #         'createdOn': str(datetime.datetime.now()),
    #         'createdBy': data['createdBy'],
    #         'type': data['type'],
    #         'location': data['location'],
    #         'status': data['status'],
    #         'Images': data['Images'],
    #         'Videos': data['Videos'],
    #         'description': data['description']

    #     }
    #     redflag_records.append(redflag)
    #     return jsonify({'status': 201,
    #             'message' : "Redflag created succesfuly"})


    # def delete_one(self, id):
    #     data = request.get_json()
    #     for redflag in redflags:
    #         if redflag['id'] == id:
    #             redflags.remove(redflag)
    #             return jsonify({"status": 200,
    #                     "message": "Redflag deleted succesfully"})
    #         else:
    #             return jsonify({"status": 404,
    #                     "message": "Redflag not found"})

    # def put_one(self, id):
    #     data = request.get_json()
    #     attribute = data["attribute"]
    #     change = data["change"]
    #     redflag =  [redflag for redflag in redflags if redflag ["id"] == id]
    #     redflag[0]['attribute'] = request.json['attribute']
    #     redflags.update(redflag[0])
    #     return jsonify ({"redflags": redflag[0]})
            
                      
    # def get_all(self):
    #     return jsonify({"status": 200,
    #             "Redflag": redflags })