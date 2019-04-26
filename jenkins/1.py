import requests
import http.client
from requests.auth import HTTPBasicAuth
import json
import unittest

class JenkinsPost(unittest.TestCase):
    def setUp(self):
        self.build_job_url = 'http://localhost:8080/jenkins/job/check_python_version/build'
        self.disable_jol_url = 'http://localhost:8080/jenkins/job/check_python_version/disable'
        self.job_url = 'http://localhost:8080/jenkins/job/check_python_version/api/json'

    def test_build_job(self):
        r = requests.post(self.build_job_url, data={}, auth= ('admin', '70872ae549414d758760572203bec7d8'))
        print(r.status_code)


if __name__ == '__main__':
    unittest.main()
