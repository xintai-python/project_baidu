import requests
from requests.auth import HTTPBasicAuth
import json
import unittest

class JenkinsPost(unittest.TestCase):
    def setUp(self):
        self.build_job_url = 'http://localhost:8080/jenkins/api/json?pretty=true'
        self.r = requests.get(self.build_job_url,auth=('admin', '70872ae549414d758760572203bec7d8'))

    def tearDown(self):
        pass

    def test_get_all_job(self):
        print(self.r.text)
        result = self.r.text
        json_result = json.loads(result)
        #把json格式文件转换成为Python的字典格式
        #把Python字典转换成为就送格式使用dumps
        print(json_result)
        self.assertEqual(json_result['jobs'][0]['name'], 'check_python_version')
    #def test_build_job(self):
        #r = requests.get(self.build_job_url, data={}, auth= ('admin', '70872ae549414d758760572203bec7d8'))
        #print(r.text)


if __name__ == '__main__':
    unittest.main()

