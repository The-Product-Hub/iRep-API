import json
import unittest
from app import create_app

app= create_app("testing")

class Test (unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name = "testing")
        self.client = self.app.test_client
        self.data = {"title": "Police", "location": "Kenya", "status": "Resolved", "uploads": "default.jpg" } 

    def test_get(self):
        res = self.client().post('/', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(res.status_code, 201)
        result = json.loads(res.data)
        self.assertEqual(result['data'][0]['message'], "Record created succesfully.")
        res = self.client().get('/api/v1/inters')
        self.assertEqual(res.status_code, 200)

    def test_post(self):
        res = self.client().post('/api/v1/inters',data=json.dumps, content_type="application/json")
        result = json.loads(res.data)
        self.assertEqual(result['data'][0]['message'], "Record creted succesfully")
        self.assertEqual(res.status_code, 201)
        self.assertIn("Record created succesfully.", str(res.data))

    def test_find_by_id(self):
        res = self.client().post('/api/v1/inters', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(res.status_code, 201 )
        # result_in_json = json.loads(res.data.decode('utf-8').replace("'", "/"))
        # result = self.client().get('/api/v1/inters/{}'. format(result in json['data'][0]))

    def test_delete(self):
        rv = self.client().post('/api/v1/inters', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(rv.status_code, 201)
        res = self.client(). delete('/api/v1/inters/1')
        self.assertEqual(res.status_code,200)

    def test_edit(self):
        rv = self.client().post('/api/v1/inters', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(rv.status_code, 201)
        rv = self.client().patch('/api/v1/inters/1', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(rv.status_code, 201)
        results = self.client().get('/api/v1/inters/1')
        self.assertIn("Record updated succesfully.", str(results.data))



