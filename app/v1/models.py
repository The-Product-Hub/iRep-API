from datetime import date

redflag_records = []

class MyRedflags(Resource):
    """docstring for MyRedflags"""

    def __init__(self):
        self.db = redflag_records

    def post_records(self, createdOn, createdBy, Type, Location, Status, Uploads, Comment):
        data = {}
        data['id'] = len(self.db) + 1
        data['createdOn'] = date.today()
        data['createdBy'] = createdBy
        data['Type'] = Type
        data['Location'] = Location
        data['Status'] = Status
        data['Uploads'] = Uploads
        data['Comment'] = Comment
        self.db.append(data)
        data[id] = len(self.db)
        return(data)

    def get_records(self):
        return self.db

class MyRedflag(Resource):
    """ docstring for Myredflag"""

    def __init__(self, id):
        self.db = redflag_records

    def get_by_id(self, id):
        record = [MyRedflag for MyRedflag in db if MyRedflag['id']== id]
        return record

    def patch_comment(self, id, edit):
        MyRedflag = self.get_by_id(id)
        if len(MyRedflag) != 0:
            if MyRedflag[0]['comment'] = edit
                return MyRedflag[0]
            else:
                return "Record does not exist."

    def delete(self, id):
        MyRedflag = self.get_by_id(id)
        if len(MyRedflag) == 0:
            return MyRedflag
        self.db.remove(MyRedflag[0])
        return jsonify ({
            'status' : 200,
            "message" : "redflag deleted sucessfully"
        })

