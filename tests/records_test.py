import json
import unittest
from app import create_app
from instance.config import TestingConfig
from app.v1.api.views import db_records

app= create_app("testing")

class Test(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name = TestingConfig)
        self.client = self.app.test_client()
        self.data = {"createdBy": "Levy", "Location": "Kenya", "Status": "Resolved", "Comment": "corruption" } 

    def test_get(self):
        res = self.client().get('/app', data=(self.data), content_type="application/json")
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data)
        self.assertEqual(len(data['records']), 1)
        self.assertEqual(res.status_code, 200)

    def test_post(self):
        res = self.client().post('/app', data=json.dumps(self.data), content_type="application/json")
        data = json.loads(res.data)
        self.assertEqual(res['data']['id'], 1)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], "Record created succesfully.")

    def test_find_by_id(self):
        res = self.client.post('/app', data=json.dumps(self.data), content_type="application/json")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], "Created succesfully")
        self.assertEqual(data['data']['id'], 1)

    def test_delete(self):
        res = self.client.delete('/app', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], "Deleted succesfully")
        self.assertEqual(res.status_code,204)

    def test_patch(self):
        self.client().patch('/app', data=json.dumps(patch_data), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(edit.status_code, 201)
        res = self.client().get('/api/v1/inters/1')
        self.assertEqual(data['message'], "Record updated succesfully.")

    def tearDown(self):
        db_records.clear()

if __name__ == '__main__':
    unittest.main()

