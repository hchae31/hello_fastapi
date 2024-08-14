from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, select
from sqlalchemy.orm import sessionmaker, declarative_base, Session

sqlite_url = 'sqlite:///app/clouds2024.db'
engine = create_engine(sqlite_url,
                       connect_args={}, echo=True)


# 데이터베이스 모델 정의
Base = declarative_base()

class Zipcode(Base):
    __tablename__ = 'zipcode'

    zipcode = Column(String, index=True)
    sido = Column(String)
    gugun = Column(String)
    dong = Column(String)
    ri = Column(String)
    bunji = Column(String)
    seq = Column(String, primary_key=True)

app = FastAPI()

@app.get('/zipcode/{dong}')
def zipcode(dong: str):
    result = ''

    # sessionmaker 없이 바로
    with Session(engine) as sess:
        stmt = select(Zipcode).where(Zipcode.dong.like(f'{dong}'))
        rows = sess.scalars(stmt)

        for row in rows:
            result += f'{row.zipcode} {row.sido} {row.gugun} {row.dong}'

    return f'{result}'

@app.get('/sido')
def getsido():
    pass

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('jinja01:app', reload=True)
