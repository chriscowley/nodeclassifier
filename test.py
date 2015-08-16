""" Test module for Node Classifier """

import os
import nodeclassifier
import unittest

class NodeclassifierTestCase(unittest.TestCase):
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

    def test_getnodes(self):
        res = self.app.get("/v1.0/nodes")
        assert res.status_code == 200

if __name__ == '__main__':
    unittest.main()
