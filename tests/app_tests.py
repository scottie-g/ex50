from nose.tools import *
from app import app
import requests
from tests.tools import assert_response

def test_index():
	resp = requests.get("http://localhost:5000/")
	assert_response(resp, status="404")
	
	resp= requests.get("http://localhost:5000/hello")
	assert_response(resp)
	
	resp = requests.get("http://localhost:5000/hello", method="POST")
	assert_response(resp, contains="Nobody")
	
	data = {'name': 'Scott', 'greet': 'Howdy'}
	resp = requests.get("http://localhost:5000/hello", method="POST", data=data)
	assert_response(resp, contains="Scott")
