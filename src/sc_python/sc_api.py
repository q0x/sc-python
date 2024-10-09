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

    @property
    def client(self):
        return self._client

    def is_valid(self):
        ''' :return check_credentials '''
        return self.client.auth.check_credentials()

    def get_user_groups(self):
        return self.client.user_groups.search_all_user_groups()