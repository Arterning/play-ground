from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from doc import SysDoc, Base  # 替换为你的模型文件名

# 配置数据库连接信息
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/fba"

# 创建 SQLAlchemy 引擎
engine = create_engine(DATABASE_URL)

# 创建所有表（如果表不存在）
Base.metadata.create_all(engine)

# 创建会话工厂和会话对象
Session = sessionmaker(bind=engine)
session = Session()

# 查询所有 SysDoc 记录
docs = session.query(SysDoc).all()

# 打印结果
for doc in docs:
    print(doc)

# 关闭会话
session.close()
