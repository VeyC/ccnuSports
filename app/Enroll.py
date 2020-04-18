# 报名界面
import pymysql
import json
from flask import Flask, request, session, redirect, url_for, render_template, make_response, jsonify


def get_project():
    id = session.get('id')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    Sql_t = "SELECT is_teacher,sex FROM `cs_user` WHERE id='" + id + "'"
    cursor.execute(Sql_t)
    result_t = cursor.fetchone()
    tag_te = result_t['is_teacher']
    tag_sex = result_t['sex']
    # 操作sql
    Sql_info = "SELECT id, name, limit_number,time,type,participant FROM `cs_project`"
    cursor.execute(Sql_info)
    result_info = cursor.fetchall()
    result_list = []
    for each_info in result_info:
        project_id = str(each_info['id'])  # 每个项目编号
        if tag_te == each_info['participant'] and (project_id[2] == str(tag_sex) or project_id[2] == '2'):
            # print(project_id[2])
            # print(each_info)
            Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + project_id + "'"
            cursor.execute(Sql_count)
            result_count = cursor.fetchall()
            Sql_apply = "SELECT COUNT(*) FROM cs_score WHERE student_id='" + id + "' and project_id='" + project_id + "'"
            cursor.execute(Sql_apply)
            result_app = cursor.fetchall()
            for each_count in result_count:
                count = each_count['count(*)']
                each_info['count'] = count
                Time = each_info['time'].strftime("%Y-%m-%d-%H")
                each_info['time'] = Time
                each_info['hasapply'] = result_app[0]['COUNT(*)']
                if project_id[1] == '1':
                    each_info['ispre'] = '0'
                else:
                    each_info['ispre'] = '1'
                result_list.append(each_info)
    data_json = json.dumps(result_list, ensure_ascii=False)
    print(data_json)
    return data_json


def search_type():
    print("enter type")
    id = session.get('id')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    Sql_t = "SELECT is_teacher,sex FROM `cs_user` WHERE id='" + id + "'"
    cursor.execute(Sql_t)
    result_t = cursor.fetchone()
    tag_te = result_t['is_teacher']
    tag_sex = result_t['sex']

    searchkey = request.json.get('input')
    if searchkey.startswith("个人"):
        searchkey = '0'
    elif searchkey.startswith("团体"):
        searchkey = '1'
    # 操作sql
    Sql_info = "SELECT id, name, limit_number,time, type,participant FROM cs_project WHERE type ='" + searchkey + "'"
    cursor.execute(Sql_info)
    result_info = cursor.fetchall()
    result_list = []
    for each_info in result_info:
        project_id = str(each_info['id'])  # 每个项目编号
        if tag_te == each_info['participant'] and (project_id[2] == str(tag_sex) or project_id[2] == '2'):
            key = str(each_info['id'])
            Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + key + "'"
            cursor.execute(Sql_count)
            result_count = cursor.fetchall()
            Sql_apply = "SELECT COUNT(*) FROM cs_score WHERE student_id='" + id + "' and project_id='" + project_id + "'"
            cursor.execute(Sql_apply)
            result_app = cursor.fetchall()
            for each_count in result_count:
                count = each_count['count(*)']
                each_info['count'] = count
                Time = each_info['time'].strftime("%Y-%m-%d-%H")
                each_info['time'] = Time
                each_info['hasapply'] = result_app[0]['COUNT(*)']
                if project_id[1] == '1':
                    each_info['ispre'] = '0'
                else:
                    each_info['ispre'] = '1'
                result_list.append(each_info)
    data_json = json.dumps(result_list, ensure_ascii=False)
    print(data_json)
    return data_json


def search_name():
    print("enter name")
    id = session.get('id')
    print(id)
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    Sql_t = "SELECT is_teacher,sex FROM `cs_user` WHERE id='" + id + "'"
    cursor.execute(Sql_t)
    result_t = cursor.fetchone()
    tag_te = result_t['is_teacher']
    tag_sex = result_t['sex']

    searchkey = request.json.get('input')
    # 操作sql
    Sql_info = "SELECT id, name, limit_number, time, type,participant FROM cs_project WHERE name like '%" + searchkey + "%' "
    cursor.execute(Sql_info)
    result_info = cursor.fetchall()
    result_list = []
    for each_info in result_info:
        project_id = str(each_info['id'])  # 每个项目编号
        if tag_te == each_info['participant'] and (project_id[2] == str(tag_sex) or project_id[2] == '2'):
            key = str(each_info['id'])
            Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + key + "'"
            cursor.execute(Sql_count)
            result_count = cursor.fetchall()
            Sql_apply = "SELECT COUNT(*) FROM cs_score WHERE student_id='" + id + "' and project_id='" + project_id + "'"
            cursor.execute(Sql_apply)
            result_app = cursor.fetchall()
            for each_count in result_count:
                count = each_count['count(*)']
                each_info['count'] = count
                Time = each_info['time'].strftime("%Y-%m-%d-%H")
                each_info['time'] = Time
                each_info['hasapply'] = result_app[0]['COUNT(*)']
                if project_id[1] == '1':
                    each_info['ispre'] = '0'
                else:
                    each_info['ispre'] = '1'
                result_list.append(each_info)
    data_json = json.dumps(result_list, ensure_ascii=False)
    print(data_json)
    return data_json


def search_id():
    id = session.get('id')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    Sql_t = "SELECT is_teacher,sex FROM `cs_user` WHERE id='" + id + "'"
    cursor.execute(Sql_t)
    result_t = cursor.fetchone()
    tag_te = result_t['is_teacher']
    tag_sex = result_t['sex']

    searchkey = request.json.get('input')
    # 操作sql
    Sql_info = "SELECT id, name, limit_number,time,type, participant FROM cs_project WHERE id ='" + searchkey + "'"
    cursor.execute(Sql_info)
    result_info = cursor.fetchall()
    result_list = []
    for each_info in result_info:
        project_id = str(each_info['id'])  # 每个项目编号
        if tag_te == each_info['participant'] and (project_id[2] == str(tag_sex) or project_id[2] == '2'):
            Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + project_id + "'"
            cursor.execute(Sql_count)
            result_count = cursor.fetchall()
            Sql_apply = "SELECT COUNT(*) FROM cs_score WHERE student_id='" + id + "' and project_id='" + project_id + "'"
            cursor.execute(Sql_apply)
            result_app = cursor.fetchall()
            for each_count in result_count:
                count = each_count['count(*)']
                each_info['count'] = count
                Time = each_info['time'].strftime("%Y-%m-%d-%H")
                each_info['time'] = Time
                each_info['hasapply'] = result_app[0]['COUNT(*)']
                if project_id[1] == '1':
                    each_info['ispre'] = '0'
                else:
                    each_info['ispre'] = '1'
                result_list.append(each_info)
    data_json = json.dumps(result_list, ensure_ascii=False)
    print(data_json)
    return data_json


# 比赛报名
def enroll():
    print("enter enroll")
    user_id = session.get('id')
    project_id = str(request.json.get('project_id'))

    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    Sql_insert = "INSERT INTO cs_score(student_id,project_id,status) VALUES ('" + user_id + "','" + project_id +" ','0')"
    cursor.execute(Sql_insert)
    connection.commit()

    Sql_check = "SELECT COUNT(*) FROM cs_score WHERE student_id='" + user_id + "' and project_id='" + project_id + "'"
    cursor.execute(Sql_check)
    # result保存该用户的所有报名信息
    result_li = cursor.fetchall()
    print(result_li[0]['COUNT(*)'])
    if result_li[0]['COUNT(*)'] == 1:
        hasapply = 1
        print("已报名")
    else:
        hasapply = 0
        print("未报名")
    # 查该项目报名总人数
    Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + project_id + "'"
    cursor.execute(Sql_count)
    result_count = cursor.fetchall()
    print(result_count[0])

    Sql_info = "SELECT * FROM `cs_project` where id = '" + project_id + "'"
    cursor.execute(Sql_info)
    result_info = cursor.fetchone()
    result_info['hasapply'] = hasapply
    result_info['count'] = result_count[0]['count(*)']
    if project_id[1] == '1':
        result_info['ispre'] = '0'
    else:
        result_info['ispre'] = '1'
    Time = result_info['time'].strftime("%Y-%m-%d-%H")
    result_info['time'] = Time
    data_json = json.dumps(result_info, ensure_ascii=False)
    print(data_json)
    return data_json


# 取消报名
def cancel():
    print("enter cancel")
    user_id = session.get('id')
    project_id = str(request.json.get('project_id'))
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    Sql_delete = "DELETE FROM cs_score WHERE student_id = '"+user_id+"' and project_id = '"+project_id+"'"
    cursor.execute(Sql_delete)
    connection.commit()

    Sql_check = "SELECT COUNT(*) FROM cs_score WHERE student_id='" + user_id + "' and project_id='" + project_id + "'"
    cursor.execute(Sql_check)
    # result保存该用户的所有报名信息
    result_li = cursor.fetchall()
    print(result_li[0]['COUNT(*)'])
    if result_li[0]['COUNT(*)'] == 1:
        hasapply = 1
        print("已报名")
    else:
        hasapply = 0
        print("未报名")
    # 查该项目报名总人数
    Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + project_id + "'"
    cursor.execute(Sql_count)
    result_count = cursor.fetchall()
    print(result_count[0])

    Sql_info = "SELECT * FROM `cs_project` where id = '" + project_id + "'"
    cursor.execute(Sql_info)
    result_info = cursor.fetchone()
    result_info['hasapply'] = hasapply
    result_info['count'] = result_count[0]['count(*)']
    if project_id[1] == '1':
        result_info['ispre'] = '0'
    else:
        result_info['ispre'] = '1'
    Time = result_info['time'].strftime("%Y-%m-%d-%H")
    result_info['time'] = Time
    data_json = json.dumps(result_info, ensure_ascii=False)
    print(data_json)
    return data_json


# 查看个人信息
def enroll_info():
    print("enter enroll_info")
    student_id = session.get('id')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()

    selectUserSql = "SELECT cs_score.project_id,cs_project.`name`,cs_project.type,cs_project.time,cs_score.status \
                        FROM cs_score,cs_project WHERE cs_score.student_id = '" + student_id + "'AND cs_score.project_id = cs_project.id"
    cursor.execute(selectUserSql)
    result = cursor.fetchall()
    result_li = []
    for each in result:
        Time = each['time'].strftime("%Y-%m-%d-%H")
        each['time'] = Time
        result_li.append(each)
    data_json = json.dumps(result_li, ensure_ascii=False)
    print(data_json)
    return data_json