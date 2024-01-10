"""
The module allows you to do various operations with email.

There are the next operations with email:
    - save to instance of the class
    - add email
    - get email
    - delete email
"""
from typing import Any, Dict, List

from hunter_io_email_checker_v2.email_service import EmailService


class EmailChecker:
    """The class provides the next methods: verify_email, save_email, get_email, delete_email."""

    def __init__(self, email_service: EmailService):
        """Initialize the EmailChecker by the email_service instance."""
        self._email_service = email_service

    def email_verify(self, email: str) -> Dict:
        """Send request to hunter-api, varify it and return dictionary with essential information."""
        return self._email_service.email_verification(email=email)

    def add_new_email(self, email: str) -> Dict[str, dict]:
        """Save email to database."""
        email_data = self.email_verify(email=email)

        return self._email_service.save_email_to_db(email_data)

    def get_email_data(self, email: str) -> Dict[str, dict]:
        """Return current email."""
        return self._email_service.read_email_from_db(email=email)

    def delete_email(self, email: str) -> None:
        """Delete current email."""
        self._email_service.delete_email_from_db(email=email)

    def get_all_emails_list(self) -> List[str]:
        """Return list of all emails."""
        return self._email_service.get_emails_list()

    def update_email(self, email: str) -> Dict[str, Any]:
        """Update email in database."""
        email_data = self.email_verify(email=email)

        if email_data.get('status') == 'valid':
            return self._email_service.update_email_in_db(email_data)

        self.delete_email(email=email)
        return email_data
