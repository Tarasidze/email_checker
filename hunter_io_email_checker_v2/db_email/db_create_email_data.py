from hunter_io_email_checker_v2.db_email.db_init_email import Base, engine
from hunter_io_email_checker_v2.db_email.models.email_data import EmailData


def create_db():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_db()
