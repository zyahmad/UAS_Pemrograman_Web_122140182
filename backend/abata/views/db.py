from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker, scoped_session
from .models import Base

DBSession = scoped_session(sessionmaker())

def init_db(settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)