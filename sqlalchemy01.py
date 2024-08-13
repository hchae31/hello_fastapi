
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.future import engine
from sqlalchemy.orm import sessionmaker, declarative_base

# sqlalchemy
# 파이썬용 ORM 라이브러리
# sqlalchemy.org

# 데이터베이스 설정
sqlite_url = 'sqlite:///python.db'
engine = create_engine(sqlite_url,
            connect_args={'check_same_thread': False}, echo=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 모델 정의
Base = declarative_base()

class Sungjuk(Base):
    __tablename__ = 'sungjuk'

    sjno = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    kor = Column(Integer)
    eng = Column(Integer)
    mat = Column(Integer)

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)


# FastAPI 메인
app = FastAPI()

# fastapi 앱 실행방법
# python -m uvicorn 파일명:app --reload
# python -m uvicorn hello_fastapi:app --reload

@app.get('/')
def index():
    return 'Hello,  sqlalchemy!!'

# __name__: 실행중인 모듈 이름을 의미하는 매직키워드
# 만일, 파일을 직접 실행하면 __name__의 이름은 __main__으로 자동지정
if __name__ == "__main__":
    import uvicorn
    uvicorn.run('sqlalchemy01:app', reload=True)
