# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import Email, DataRequired, Length


# login and registration


class CltInfoForm(FlaskForm):
    company = StringField('公司名称', id='company',validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    #source = SelectField('信息来源', choices=['行业会议', '公开信息', '熟人推荐', '客户介绍'],
                         #validators=[Length(0, 64, message='长度不正确')])
    source = StringField('信息来源', id='source', validators=[Length(0, 64, message='长度不正确')])
    #type1 = SelectField('行业分类', choices=['化工', '钢铁', '电力', '焦化', '其他'],
                        #validators=[Length(0, 64, message='长度不正确')])
    #type2 = SelectField('具体类别', choices=['硫酸', '锅炉', '玻璃窑炉', '燃煤锅炉'],
                        #validators=[Length(0, 64, message='长度不正确')])
    type1 = StringField('行业分类', validators=[Length(0, 64, message='长度不正确')])
    type2 = StringField('具体类别', validators=[Length(0, 64, message='长度不正确')])

    info = StringField('其他信息', id='info',validators=[Length(0, 64, message='长度不正确')])
    product = SelectField('适用产品', choices=['催化剂', '工程', '活性炭', '其他'],
                          validators=[Length(0, 64, message='长度不正确')])
    method = SelectField('跟进方式', choices=['电话', '微信', '到访', '其他'],
                         validators=[Length(0, 64, message='长度不正确')])
    progress = StringField('跟进进度', id='progress', validators=[Length(0, 64, message='长度不正确')])
    who = StringField('联系人', id='who', validators=[Length(0, 64, message='长度不正确')])
    tel = StringField('联系电话',id='tel', validators=[Length(0, 64, message='长度不正确')])
    remark = StringField('备注',id='remark', validators=[Length(0, 64, message='长度不正确')])

