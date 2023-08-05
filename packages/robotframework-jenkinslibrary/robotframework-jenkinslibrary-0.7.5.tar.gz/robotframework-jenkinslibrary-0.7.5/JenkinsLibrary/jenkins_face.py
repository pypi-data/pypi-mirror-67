import requests
import json
import urllib3
from robot.api.deco import keyword

BASE_ENDPOINT = '{}://{}:{}@{}/'
GET_JOB = '{}/api/json'
GET_JOB_BUILD = '{}/{}/api/json'
BUILD_JOB_WITH_PARAMETERS = '{}/buildWithParameters'


class JenkinsFace(object):

    def __init__(self):
        self._endpoint = None
        self._session = None
        self._settings = None

    @keyword('Create Session Jenkins')
    def create_session_jenkins(self,
                               protocol='https',
                               url=None,
                               username=None,
                               password=None,
                               verify=False):
        if not url or not username or not password:
            raise Exception('Require parameters should not be none')
        if not verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self._endpoint = BASE_ENDPOINT.format(protocol, username, password, url)
        self._session = requests.Session()
        self._settings = self._session.merge_environment_settings(
            self._endpoint, {}, None, verify, None
        )
        self._settings['allow_redirects'] = False

    @keyword('Get Jenkins Job')
    def get_jenkins_job(self, name=None):
        if not name:
            raise Exception('Job name should not be None')
        req = self._session.prepare_request(
            requests.Request(
                'GET',
                self._job_url(GET_JOB, [self._job_folder(name)])
            )
        )
        return self._get_response(
            self._send(req)
        )

    @keyword('Get Jenkins Job Build')
    def get_jenkins_job_build(self, name=None, build_number='lastBuild'):
        if not name:
            raise Exception('Job name should not be None')
        req = self._session.prepare_request(
            requests.Request(
                'GET',
                self._job_url(GET_JOB_BUILD, [self._job_folder(name), build_number])
            )
        )
        return self._get_response(
            self._send(req)
        )

    @keyword('Build Jenkins With Parameters')
    def build_jenkins_with_parameters(self, name=None, data=None):
        if not name:
            raise Exception('Job name should not be None')
        job_detail = self.get_jenkins_job(name)
        req = self._session.prepare_request(
            requests.Request(
                'POST',
                self._job_url(BUILD_JOB_WITH_PARAMETERS, [self._job_folder(name)]),
                data=data
            )
        )
        response = self._send(req)
        response.raise_for_status()
        return job_detail['nextBuildNumber']

    def _send(self, req):
        return self._session.send(req, **self._settings)

    @staticmethod
    def _get_response(response):
        response.raise_for_status()
        return json.loads(response.content, encoding='utf-8')

    def _job_url(self, url_format, params):
        url = url_format.format(*params)
        return self._endpoint + url

    @staticmethod
    def _job_folder(name):
        path_list = name.split('/')
        folder_name = ''
        job_name = path_list[-1]
        if len(path_list) > 1:
            folder_name = 'job/' + '/job/'.join(path_list[:-1]) + '/'
        return folder_name + 'job/' + job_name
