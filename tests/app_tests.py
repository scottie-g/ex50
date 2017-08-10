from nose.tools import *
from app import app
from unittest import *

app.config['TESTING'] = True
web = app.test_client()

def test_index():
	rv = web.get('/', follow_redirects=True)
	assert_equal(rv.status_code, 404)
	
	rv = web.get('/hello', follow_redirects=True)
	assert_equal(rv.status_code, 200)
	("Fill Out This Form", rv.data)
	
	#data = {'name': 'Scottie', 'greet': 'Howdy'}
	#rv = web.post('/hello, follow_redirects=True, data=data)
	#assert_in("Scottie", rv.data)
	#assert_in("Howdy", rv.data)
