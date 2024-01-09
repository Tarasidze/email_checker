"""
The module allows you to do various operations with email.

There are the next operations with email:
    - save to instance of the class
    - add email
    - get email
    - delete email
"""

import json
import os
from typing import Dict, List
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin, urlparse
from urllib.request import urlopen

from dotenv import load_dotenv

load_dotenv()
hunter_api_key = os.getenv('HUNTER_API_KEY')
url_api_email_verify = os.getenv('URL_EMAIL_API_VERIFY')


class EmailChecker:
    """
    The class provides the next methods: verify_email, save_email, get_email, delete_email.

    All data will be save in self.inner_value variable (dictionary)
    """

    def __init__(self) -> None:
        """Instance of the class configures by using api-key and url in environment variable."""
        self._current_storage = {}
        self._url_email_api_verify = url_api_email_verify
        self._api_key = hunter_api_key

    def verify_email(self, email: str) -> Dict:
        """Send request to hunter-api, varify it and return dictionary with essential information."""
        url_params = {'email': email, 'api_key': self._api_key}
        url = urljoin(self._url_email_api_verify, '?' + urlencode(url_params))

        try:
            response_local = urlopen(url)
        except HTTPError as error:
            return {'status': False, 'error code': error.code, 'error reason': error.reason}
        except URLError as error:
            return {'status': False, 'error reason': error.reason}

        response_data = response_local.read()
        encoding = response_local.info().get_content_charset('utf-8')

        return json.loads(response_data.decode(encoding))

    def add_new_email(self, email: str) -> Dict[str, dict]:
        """Save email to local variable."""
        email_status = self.verify_email(email)

        if email_status.get('status') is not False:
            self._current_storage[email] = email_status

        return email_status

    def get_email_data(self, email: str) -> Dict[str, dict]:
        """Return current email."""
        return self._current_storage.get(email)

    def delete_email(self, email: str) -> None:
        """Delete current email."""
        self._current_storage.pop(email)

    def get_all_emails_list(self) -> List[str]:
        """Return list of all emails."""
        list_of_emails = []

        for key in self._current_storage:
            list_of_emails.append(key)

        return list_of_emails

    def set_api_url(self, url_f: str) -> bool:
        """
        Change the API URL.

        This method allows changing the API URL for email verification.

        Parameters:
        - url_f (str): The new API URL.

        Returns:
        bool: True if the URL is valid and updated successfully, False otherwise.
        """
        if not self._is_url_valid(url_f):
            raise URLError('Invalid url, try again')

        self._url_email_api_verify = url_f
        return True

    def _is_url_valid(self, url_f: str) -> bool:
        try:
            result_parse = urlparse(url_f)
        except (ValueError, URLError):
            return False

        return all([result_parse.scheme, result_parse.netloc])
