# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 数据库的核心接口 Engine实例
# echo标志是sqlalchemy日志开启标志,通过Python标准logging模块实现.
# 当使用engine.execute()或engine.connect()被称为建立一个真实的连接.
# engine创建时并未尝试连接数据库.第一次执行任务时会进行连接
engine = create_engine('sqlite:///test.db', echo=True)

# 数据库会话句柄session
# 每当与数据库进行会话时,都需要实例化一个Session
Session = sessionmaker(bind=engine)

# 声明性基类 通常只有一个
# 给模型类提供构造函数__init__
Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        """可选择的方法
        为了显示良好的User实例对象"""
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname
        )


# 传入engine作为数据库连接的来源
# Base.metadata.create_all(engine)

# ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# print(ed_user.name, ed_user.nickname, str(ed_user.id))

# 每当与数据库会话时,都需要实例化一个Session
session = Session()

# 添加一个对象,但不提交
# ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# session.add(ed_user)

# 查询对象 返回的行是已经在其对象内部映射中表示的实例
# our_user = session.query(User).filter_by(name='ed').first()
# print(our_user)
# print(our_user is ed_user)

# 使用add_all添加更对User对象
# session.add_all([
#     User(name='test1', fullname='test1full', nickname='test1nick'),
#     User(name='test2', fullname='test2full', nickname='test2nick'),
#     User(name='test3', fullname='test3full', nickname='test3nick'),
# ])

# 修改ed的昵称
# ed_user.nickname = 'test4'

# 被修改过的数据
# print(session.dirty)

# 插入但未被修改的数据
# print(session.new)

# 对所有更改发布到数据库, 提交整个过程中一直进行的事务
# commit刷新对数据库的所有剩余更改,并提交事务
# 会话引用的连接资源现在返回到连接池.
# 此会话的后续操作将再new事务
# 它将在第一次需要时重新获取连接资源
# session在数据库插入新行, 所有新生成的标识符和数据库生成的默认值都在实例上立即可用
# 或者第一次访问时加载
# session.commit()
# print(ed_user.id)

# ed_user.name = 'Edwardo'
# fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
# session.add(fake_user)

# now_users = session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
# print(now_users)

# session.rollback()
#
# print(ed_user.name)
#
# print(fake_user in session)
#
# print(session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all())

# 普通查询
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

# 查询:query接收ORM插入描述符作为参数.当多个类实体或基于列的实体表示为query()函数,返回结果表示为元组
for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

# 返回的元组query是已命名元组.可以像普通的
for row in session.query(User, User.name).all():
    print(row.User, row.name)

# 可以用label()构造,从任何一个ColumnElement派生对象映射到一个对象的任何类属性
for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)

# 可以使用实体别名
from sqlalchemy.orm import aliased

user_alias = aliased(User, name='user_alias')

for row in session.query(user_alias, user_alias.name).all():
    print(row.user_alias)

# 基本query包括发布限制和偏移.使用Python数组切片, 通常与order_by结合使用
for u in session.query(User).order_by(User.id)[1:3]:
    print(u)

# 过滤结果:filter_by,使用关键字参数
for name, in session.query(User.name).filter_by(fullname='Ed Jones'):
    print(name)

# 或者使用filter.在映射类上使用具有类级属性的常规Python运算符
for name, in session.query(User.name).filter(User.fullname == 'Ed Jones'):
    print(name)

# 大多数方法调用都返回一个新的query对象.在此对象上可以添加其他条件.
for user in session.query(User).filter(User.name == 'ed').filter(User.fullname == 'Ed Jones'):
    print(user)

# 常用筛选器运算符
# filter()
# equals: query.filter(User.name == 'ed')

# not equals: query.filter(User.name != 'ed')

# LIKE: query.filter(User.name.like('%ed%'))

# ILIKE(不区分大小写): query.filter(User.name.like('%ed%'))

# IN: query.filter(User.name.in_(['ed', 'wendy']))

# 返回列表和标量
# all() 返回一个列表
print('-'*30)
query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
print(query.all())

print('-'*30)

# first()限制,以标量形式返回第一个结果
print(query.first())

print('-'*30)

# one() 完全获取所有行 如果结果中不存在一个对象标识或复合行,则引发错误.
user = query.one()
print(user)
# one_or_none() 如果没有找到结果,则不会引发错误, 只返回None.
# scalar()调用one()方法. 在成功时返回行的第一列
print('-'*30)
query = session.query(User.id).filter(User.name == 'ed').order_by(User.id)
print(query.scalar())
print('-'*30)

# 计数 count()
count = session.query(User).filter(User.name.like('%ed')).count()
print(count)
print('-'*30)

# 特别计数某字段,比如返回不同用户名的计数
from sqlalchemy import func
print(session.query(func.count(User.name), User.name).group_by(User.name).all())
print('-'*30)

# 实现简单的SELECT count(*) FROM table 可以使用如下形式:
print(session.query(func.count('*')).select_from(User).scalar())
print('-'*30)

# 使用User主键计数
print(session.query(func.count(User.id)).scalar())
print('-'*30)
