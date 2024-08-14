from sqlalchemy import create_engine
from fastapi.params import Depends
from sqlalchemy.orm import sessionmaker

from app.settings import config
from app.models import sungjuk, member

engine = create_engine(config.sqlite_url, connect_args={}, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def db_startup():
    sungjuk.Base.metadata.create_all(engine)
    member.Base.metadata.create_all(engine)

async def db_shutdown():
    pass

def get_db():
    db = SessionLocal() # 데이터베이스 세션 객체 생성
    try:
        yield db # yield : 파이썬 제너레이터 객체
        # 함수가 호출될때 비로소 객체를 반환(넘김)
    finally:
        db.close()  # 데이터베이스 세션 닫음 (디비 연결해제, 리소스 반환)