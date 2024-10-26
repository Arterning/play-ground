from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker

# 配置数据库连接信息
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/fba"

# 创建 SQLAlchemy 引擎
engine = create_engine(DATABASE_URL)

# 创建一个会话工厂
Session = sessionmaker(bind=engine)
session = Session()

# 初始化 MetaData 对象
metadata = MetaData()

# 反射获取 sys_doc 表结构
sys_doc = Table('sys_doc', metadata, autoload_with=engine)

# 查询表中的所有数据
query = select(sys_doc)
result = session.execute(query)

# 打印查询结果
for row in result:
    print(row)
    print(type(row))

# 关闭会话和连接
session.close()
