"""Module for various operation with email database."""

from __future__ import annotations

import json
from typing import Any, Dict, List
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import urlopen

from hunter_io_email_checker_v2.db_email.db_init_email import email_db
from hunter_io_email_checker_v2.db_email.models.email_data import EmailData


class EmailService:
    """The service maintains a database and provides simple CRUD operations."""
    def __init__(self, url_api_email_verify: str, hunter_api_key: str) -> None:
        """Instance of the class configures by using api-key and url in environment variable."""
        self._url_email_api_verify = url_api_email_verify
        self._api_key = hunter_api_key

    def email_verification(self, email) -> Dict[str, Any]:
        """Verifies email by using an external API."""
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
        email_data = json.loads(response_data.decode(encoding))

        return email_data.get('data')

    def save_email_to_db(self, email_data: dict) -> Dict[str, Any] | None:
        """Save email status to database."""
        email_status = self._check_email_in_db(email_data.get('email'))

        if email_status.get('status') is True:
            return email_status

        email_instance = EmailData(**email_data)
        email_db.add(email_instance)
        email_db.commit()

        return {'status': 'email saved to database'}

    def read_email_from_db(self, email: str) -> Dict[str, Any]:
        """Read the email rom database."""
        email_status = self._check_email_in_db(email)

        if email_status.get('status') is False:
            return email_status

        email_instance = email_db.query(EmailData).filter_by(email=email).first()

        return email_instance.to_dict()

    def delete_email_from_db(self, email: str) -> dict:
        """Delete the email from the database."""
        email_to_delete = email_db.query(EmailData).filter_by(email=email).first()

        if email_to_delete is None:
            return {'status': False, 'error reason': 'Email is not exist'}

        email_db.delete(email_to_delete)
        email_db.commit()

    def update_email_in_db(self, email_data: dict) -> Dict:
        """Update the email in the database."""
        email_to_update = self._check_email_in_db(email=email_data.get('email'))

        if email_to_update.get('status') is True:
            self.delete_email_from_db(email=email_data.get('email'))
            return self.save_email_to_db(email_data)

        return email_to_update

    def get_emails_list(self) -> List[str]:
        """Get all emails from the database."""
        queries = email_db.query(EmailData.email).all()

        return [query[0] for query in queries]

    def _check_email_in_db(self, email: str) -> Dict[str, Any]:
        """Check if email exists in the database and returns status."""
        email_instance = email_db.query(EmailData).filter_by(email=email).first()

        if email_instance is None:
            return {'status': False, 'error reason': 'Email does not exist in database'}

        return {'status': True, 'error reason': 'Email already exists in database'}
