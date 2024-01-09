from email_checker import EmailChecker


if __name__ == '__main__':
    email_checker = EmailChecker()

    print(email_checker.add_new_email("taras.diakiv.dev@gmail.com"))

    print(email_checker.get_email_data("taras.diakiv.dev@gmail.com"))

    print(email_checker.add_new_email("test_email@gmail.com"))

    print(email_checker.get_all_emails_list())
