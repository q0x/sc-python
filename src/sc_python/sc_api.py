''' ScApi '''
import os
from sonarqube import SonarQubeClient

class ScApi:
    ''' TODO '''
    def __init__(self):
        ''' TODO '''
        url = os.getenv('SONAR_HOST_URL','https://sonarcloud.io')
        token = os.getenv('SONAR_TOKEN')
        self._client = SonarQubeClient(sonarqube_url=url, token=token)

    def is_valid(self):
        ''' :return check_credentials '''
        return self._client.auth.check_credentials()
