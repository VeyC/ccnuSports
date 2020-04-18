import pymysql
from flask import Flask, request, session, redirect, url_for, render_template, make_response, jsonify


def user_login():
    id = request.json.get('id')
    password = request.json.get('password')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    # 操作sql
    Sql1 = "SELECT * FROM `cs_basicmessage` WHERE id='" + id + "'"
    cursor.execute(Sql1)
    result1 = cursor.fetchone()
    # 存session
    session.permanent = True  # 默认session的时间持续31天
    session['id'] = id
    # 身份判断
    if id.startswith('admin'):
        Sql2 = "SELECT * FROM `cs_manage` WHERE id='" + id + "'"
        cursor.execute(Sql2)
        result2 = cursor.fetchone()
        if result2 is None: # 用户名不存在
            return jsonify({'code': 401, 'msg': 'error'})
        else:
            if result1['password'] == password:
                return jsonify({'code': 200, 'msg': 'ok', 'token': id, 'identity': "admin"})
            else:
                return jsonify({'code': 402, 'msg': 'error'}) # 密码错误
    elif id.startswith('judge'):
        Sql2 = "SELECT * FROM `cs_judge` WHERE id='" + id + "'"
        cursor.execute(Sql2)
        result2 = cursor.fetchone()
        if result2 is None:  # 用户名不存在
            return jsonify({'code': 401, 'msg': 'error'})
        else:
            if result1['password'] == password:
                return jsonify({'code': 200, 'msg': 'ok', 'token': id, 'identity': "judge"})
            else:
                return jsonify({'code': 402, 'msg': 'error'})  # 密码错误
    elif id.startswith('news'):
        if result1 is None:  # 用户名不存在
            return jsonify({'code': 401, 'msg': 'error'})
        else:
            if result1['password'] == password:
                return jsonify({'code': 200, 'msg': 'ok', 'token': id, 'identity': "news"})
            else:
                return jsonify({'code': 402, 'msg': 'error'})  # 密码错误
    else:
        Sql2 = "SELECT * FROM `cs_user` WHERE id='" + id + "'"
        cursor.execute(Sql2)
        result2 = cursor.fetchone()
        if result2 is None:  # 用户名不存在
            return jsonify({'code': 401, 'msg': 'error'})
        else:
            if result1['password'] == password:
                if result2['is_teacher'] == 1:
                    return jsonify({'code': 200, 'msg': 'ok', 'token': id, 'identity': "teacher"})
                else:
                    return jsonify({'code': 200, 'msg': 'ok', 'token': id, 'identity': "student"})
            else:
                return jsonify({'code': 402, 'msg': 'error'})  # 密码错误


def user_logout():
    session.clear()
    print(session.get('id'))
    if session.get(id) is None:
        return '1'
    else:
        return '0'
