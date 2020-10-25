"""
Counter API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import logging
from unittest import TestCase
from flask_api import status  # HTTP Status Codes
from service import app
from service.routes import rest_counter

######################################################################
#  T E S T   C A S E S
######################################################################
class CounterTest(TestCase):
    """ REST API Server Tests """

    @classmethod
    def setUpClass(cls):
        """ This runs once before the entire test suite """
        app.testing = True

    @classmethod
    def tearDownClass(cls):
        """ This runs once after the entire test suite """
        pass

    def setUp(self):
        """ This runs before each test """
        rest_counter()
        self.app = app.test_client()

    def tearDown(self):
        """ This runs after each test """
        pass

######################################################################
#  T E S T   C A S E S 
######################################################################

    def test_index(self):
        """ Test Root URL """
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_counter(self):
        """ Get a Counter """
        resp = self.app.get("/counter")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.get_json()
        self.assertEqual(data["counter"], 1)

    def test_increment_counter(self):
        """ Increment a Counter """
        resp = self.app.get("/counter")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        resp = self.app.get("/counter")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        resp = self.app.get("/counter")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.get_json()
        self.assertEqual(data["counter"], 3)

