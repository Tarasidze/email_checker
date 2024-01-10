from sqlalchemy import (
    Column,
    String,
    Integer,
    JSON,
    BOOLEAN,
)

from hunter_io_email_checker_v2.db_email.db_init_email import Base


class EmailData(Base):
    __tablename__ = "email_data"

    status = Column(String, nullable=False)
    result = Column(String, nullable=False)
    _deprecation_notice = Column(String, nullable=False)
    score = Column(Integer, default=None)
    email = Column(String, nullable=False, primary_key=True)
    regexp = Column(BOOLEAN, default=False)
    gibberish = Column(BOOLEAN, default=False)
    disposable = Column(BOOLEAN, default=False)
    webmail = Column(BOOLEAN, default=False)
    mx_records = Column(BOOLEAN, default=False)
    smtp_server = Column(BOOLEAN, default=False)
    smtp_check = Column(BOOLEAN, default=False)
    accept_all = Column(BOOLEAN, default=False)
    block = Column(BOOLEAN, default=False)
    sources = Column(JSON)

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}
