# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps import db

# 销售搜集客户有效信息的任务
class ClientInfo(db.Model):

    __tablename__ = 'ClientInfo'

    id = db.Column(db.Integer, primary_key=True)
    charge = db.Column(db.String(64))  # 负责人
    company = db.Column(db.String(64)) # 公司名称
    source = db.Column(db.String(64))  # 信息来源
    type1 = db.Column(db.String(64))  # 行业分类
    type2 = db.Column(db.String(64)) # 具体分类
    info = db.Column(db.String(64))  # 其他信息
    product = db.Column(db.String(64)) # 对应销售的产品
    method = db.Column(db.String(64)) # 跟进方式
    progress = db.Column(db.String(64)) # 跟进进度
    who = db.Column(db.String(64))  # 对方客户联系人
    tel = db.Column(db.String(64)) # 联系电话
    remark = db.Column(db.String(64)) # 备注


    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)


