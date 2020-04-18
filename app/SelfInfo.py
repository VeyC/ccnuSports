# 个人信息
import pymysql
import json
from flask import Flask, request, session, jsonify


def get_username():
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    id = session.get('id')
    Sql = "SELECT * FROM `cs_user` WHERE id='" + id + "'"
    cursor.execute(Sql)
    result = cursor.fetchone()
    return result['name']


def self_info():
    print("enter self_info")
    user_id = session.get('id')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    sql_info = "SELECT name,id,sex,department,phonenum FROM `cs_user` where id = '" + user_id + "'"
    cursor.execute(sql_info)
    data_info = cursor.fetchone()
    data_json = json.dumps(data_info, ensure_ascii=False)
    print(data_json)
    return data_json


# 修改电话号码
def change_tel():
    print("enter change_tel")
    user_id = session.get('id')
    phoneNum = request.json.get('tel')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()

    selectUserSql = "UPDATE cs_user set phonenum = '" + phoneNum + "' WHERE id = '" + user_id + "'"
    cursor.execute(selectUserSql)
    connection.commit()
    return phoneNum
