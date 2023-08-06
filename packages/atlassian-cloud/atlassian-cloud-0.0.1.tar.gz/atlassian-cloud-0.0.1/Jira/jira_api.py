import requests
from base64 import b64encode
from urllib.parse import urljoin
import logging


class JiraApi:
    def __init__(self, username, token, instance_name, log_level="INFO"):
        """Python class for Jira Cloud REST API

        Args:
            token (str): API token to access Jira Cloud
            instance_url (str): Base URL of Jira instance (ex: domain.atlassian.net)
            log_level (str, optional): Application log level. Defaults to "INFO".
        """
        self.logger = logging.getLogger("default")
        self.logger.setLevel(logging.getLevelName(log_level))

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(funcName)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        self.base_url = f"https://{instance_name}/rest/api/3/"
        self.headers = {"Content-type": "application/json"}
        self.username = username
        self.token = token

    def issue_search(
        self,
        jql,
        start_at=0,
        max_results=50,
        validate_query="strict",
        fields="*all",
        fields_by_keys="false",
    ):
        url = urljoin(self.base_url, "search")
        parameters = {
            "jql": jql,
            "start_at": start_at,
            "max_results": max_results,
            "validate_query": validate_query,
            "fields": fields,
            "fields_by_keys": fields_by_keys,
        }
        response = requests.get(
            url,
            headers=self.headers,
            params=parameters,
            auth=(self.username, self.token),
        )

        if response.status_code == 200:
            try:
                return response.json()
            except AttributeError as e:
                self.logger.error(e.args)
                pass
