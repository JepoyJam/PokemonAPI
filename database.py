
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://root:qOYbnGj8coe8XF4pEg35PxLeCwmga4fc@dpg-cfgkdr9a6gdma8h2onmg-a.frankfurt-postgres.render.com/testd2"
                        
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()