from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import TEXT, VARCHAR, TIMESTAMP as PG_TIMESTAMP

# 创建基础类，用于声明模型
Base = declarative_base()

class SysDoc(Base):
    __tablename__ = 'sys_doc'  # 指定表名

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(TEXT, nullable=False)
    name = Column(TEXT, nullable=False)
    type = Column(VARCHAR(500), nullable=False)
    content = Column(TEXT, nullable=True)
    desc = Column(TEXT, nullable=True)  # "desc" 是关键字，Python 中用 desc 替代
    file = Column(TEXT, nullable=True)
    created_time = Column(PG_TIMESTAMP(timezone=True), nullable=False)
    updated_time = Column(PG_TIMESTAMP(timezone=True), nullable=True)

    def __repr__(self):
        return f"<SysDoc(id={self.id}, title='{self.title}', name='{self.name}')>"
