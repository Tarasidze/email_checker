import os
from dotenv import load_dotenv
from hunter_io_email_checker_v2.email_service import EmailService
from hunter_io_email_checker_v2.email_checker import EmailChecker


load_dotenv()

hunter_api_key = os.getenv('HUNTER_API_KEY')
url_api_email_verify = os.getenv('URL_EMAIL_API_VERIFY')


if __name__ == '__main__':
    my_email = "taras.diakiv.dev@gmail.com"
    test_email = "test_email@gmail.com"

    e_service = EmailService(url_api_email_verify, hunter_api_key)
    email_checker = EmailChecker(e_service)

    em_data = email_checker.email_verify(my_email)
    print(em_data)

    email_checker.add_new_email(my_email)
    print(email_checker.get_email_data(my_email))

    email_checker.add_new_email(test_email)
    email_checker.delete_email(test_email)

    print(email_checker.get_email_data("asdad"))

    print(email_checker.add_new_email(test_email))
    print(email_checker.add_new_email(test_email))

    print(email_checker.get_all_emails_list())



