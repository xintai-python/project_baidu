#GET DEMO WITH URLLIB2
import requests
import unittest
import json
from requests.auth import HTTPBasicAuth


class JenkinsGetTestCase(unittest.TestCase):
    def setUp(self):
        self.requests = requests.get('http://localhost:8080/jenkins/api/json?tree=jobs[name]', auth=('admin','70872ae549414d758760572203bec7d8'))


    def test_get_all_job_names(self):
        print(self.requests.text)


#url_request = 'http://localhost:8080/jenkins/api/'
#response = requests.get(url = 'url_request', verify=False)
#print(response.read())
