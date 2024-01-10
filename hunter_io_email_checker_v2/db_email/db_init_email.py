from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from pathlib import Path


engine = create_engine(f'sqlite:///{Path(__file__).parent.parent/Path("db_instances")/Path("db_email.db")}')
Local_Session = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

email_db = Local_Session()
