""" Test module for Node Classifier """

import os
import nodeclassifier
import unittest
import pep8
import json

class NodeclassifierTestCase(unittest.TestCase):
    def test_pep8_conformance(self):
        """ Test PEP8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['nodeclassifier/views.py' ])
        self.assertEqual(result.total_errors, 0,
            "Found code style errors (and warnings).")

    def setUp(self):
        self.app = nodeclassifier.app.test_client()

    def tearDown(self):
        pass

    def test_root(self):
        res = self.app.get("/")
        assert res.status_code == 200

    def test_getroles(self):
        res = self.app.get("/v1.0/roles")
        assert res.status_code == 200

    def test_getrules(self):
        res = self.app.get("/v1.0/rules")
        assert res.status_code == 200

    def test_postrules_content(self):
        testrole = {
                'role' : 'testrole'
                }
        res = self.app.post(
                "/v1.0/rules",
                data=json.dumps(testrole),
                content_type='application/json'
                )
        content = "testrole"
        assert content in res.data
        
    def test_postrules(self):
        res = self.app.post("/v1.0/rules")
        assert res.status_code == 200

    def test_getnodes(self):
        res = self.app.get("/v1.0/nodes")
        assert res.status_code == 200

    def test_getnode(self):
        res = self.app.get("v1.0/nodes/node1")
        assert res.status_code == 200

    def test_getrole(self):
        res = self.app.get("v1.0/role")
        assert res.status_code == 200


if __name__ == '__main__':
    unittest.main()
