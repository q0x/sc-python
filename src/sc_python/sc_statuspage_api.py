import os
import requests
import json
import logging 
from enum import StrEnum, auto

log = logging.getLogger(__name__)

def to_json(obj):
    return json.dumps(obj,indent=2)

class ScImpactStatus(StrEnum):
    ''' https://sonarcloud.statuspage.io/api/#status '''
    NONE = auto()
    MINOR = auto()
    MAJOR = auto()
    CRITICAL = auto()

class ScComponentStatus(StrEnum):
    OPERATIONAL =  auto()
    DEGRADED_PERFORMANCE =  auto()
    PARTIL_OUTAGE  = auto()
    MAJOR_OUTAGE =  auto()

class ScIncidentStatus(StrEnum):
    INVESTIGATING = auto()
    IDENTIFIED  = auto()
    MONITORING  = auto()
    RESOLVED = auto()
    POSTMORTEM = auto()

class ScScheduledMaintenanceStatus(StrEnum):
    SCHEDULED = auto() 
    IN_PROGRESS = 'in progress'
    VERIFYING = auto()
    COMPLETED = auto()

class ScComponent(StrEnum):
    API = 'API'
    MANAGEMENT_PORTAL = "Management Portal"
    # Authentication and User Management 
    # Automatic Analysis 
    # Billing and Subscription 
    # CI-based Analysis 
    # Customer Support Portal 
    # Documentation 
    # Notifications 
    # Public APIs 
    # Pull Request Experience 
    # SonarLint Experience 
    # Third-Party Services 
    # Website 

class ScStatusPageApi:

    def __init__(self, endpoint=None):
        self._endpoint = 'https://sonarcloud.statuspage.io/api/v2' if endpoint is None else endpoint

    @property
    def endpoint(self):
        return self._endpoint

    def get_url(self, path):
        return self.endpoint + path

    def get_json(self,path):
        url = self.get_url(path)
        resp = requests.get(url)
        assert resp.ok, f'URL is returning {resp.status_code} : {url}'
        return resp.json()

    def get_summary(self):
        return self.get_json('/summary.json')

    def get_status(self):
        return self.get_json('/status.json')

    def is_up(self, status_json=None):
        status = self.get_status() if status is None else status

        assert 'indicator' in status, f'status object has no indicator {to_json(status)} '
        indicator = status['indicator']

        return ScImpactStatus.NONE == indicator 


