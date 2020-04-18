import pymysql
import json
from flask import Flask, request, session, redirect, url_for, render_template, make_response, jsonify


# 管理员主页
def admin_project():
    id = session.get('id')

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 获取管理员所在学院
    cursor = connection.cursor()
    sql_dept = "SELECT department FROM `cs_user` WHERE id='" + id + "'"
    cursor.execute(sql_dept)
    result_dept = cursor.fetchone()  # {'department': 'cs'}
    dept = result_dept['department']

    # 查询序号（不必要）、项目编号、比赛类型、项目名称、已报人数、需要人数、user_id、sex，审核状态
    cursor = connection.cursor()
    sql_info = "SELECT cs_project.id as pid,cs_project.type,cs_project.name,cs_project.limit_number,cs_user.id,cs_user.sex,cs_score.`status`\
                  FROM cs_project,cs_user,cs_score\
                  WHERE cs_user.department = '" + dept + "' and cs_user.id = cs_score.student_id and cs_project.id = cs_score.project_id"
    cursor.execute(sql_info)
    result_info = cursor.fetchall()
    result_list = []

    for each_info in result_info:
        project_id = str(each_info['pid'])  # 每个项目编号
        each_info['pid'] = project_id
        # 查询各项目的报名人数（已通过+未审核）
        Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + project_id + "' and `status`!=2 "
        cursor.execute(Sql_count)
        result_count = cursor.fetchone()

        count = result_count['count(*)']
        each_info['count'] = count

        if each_info['sex'] == 0:
            each_info['sex'] = '女'
        elif each_info['sex'] == 1:
            each_info['sex'] = '男'

        result_list.append(each_info)

    data_json = json.dumps(result_list, ensure_ascii=False)
    print(data_json)
    return data_json


def admin_search_type():
    print("enter admin type")
    id = session.get('id')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 获取管理员所在学院
    cursor = connection.cursor()
    sql_dept = "SELECT department FROM `cs_user` WHERE id='" + id + "'"
    cursor.execute(sql_dept)
    result_dept = cursor.fetchone()  # {'department': 'cs'}
    dept = result_dept['department']

    searchkey = request.json.get('input')
    if searchkey.startswith("个人"):
        searchkey = '0'
    elif searchkey.startswith("团体"):
        searchkey = '1'
    # 操作sql
    sql_type = "SELECT cs_project.id as pid,cs_project.type,cs_project.name,cs_project.limit_number,cs_user.id,cs_user.sex,cs_score.`status`\
                  FROM cs_project,cs_user,cs_score\
                  WHERE cs_user.department = '" + dept + "' and cs_user.id = cs_score.student_id and cs_project.id = cs_score.project_id\
                  and cs_project.type = '" + searchkey + "'"
    cursor.execute(sql_type)
    result_info = cursor.fetchall()
    result_list = []

    for each_info in result_info:
        project_id = str(each_info['pid'])  # 每个项目编号
        each_info['pid'] = project_id
        # 查询各项目的报名人数（已通过+未审核）
        Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + project_id + "' and `status`!=2 "
        cursor.execute(Sql_count)
        result_count = cursor.fetchone()

        count = result_count['count(*)']
        each_info['count'] = count
        if each_info['sex'] == 0:
            each_info['sex'] = '女'
        elif each_info['sex'] == 1:
            each_info['sex'] = '男'

        result_list.append(each_info)

    data_json = json.dumps(result_list, ensure_ascii=False)
    print(data_json)
    return data_json


def admin_search_id():
    id = session.get('id')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 获取管理员所在学院
    cursor = connection.cursor()
    sql_dept = "SELECT department FROM `cs_user` WHERE id='" + id + "'"
    cursor.execute(sql_dept)
    result_dept = cursor.fetchone()  # {'department': 'cs'}
    dept = result_dept['department']

    searchkey = request.json.get('input')
    # 操作sql
    sql_id = "SELECT cs_project.id as pid,cs_project.type,cs_project.name,cs_project.limit_number,cs_user.id,cs_user.sex,cs_score.`status`\
                  FROM cs_project,cs_user,cs_score\
                  WHERE cs_user.department = '" + dept + "' and cs_user.id = cs_score.student_id and cs_project.id = cs_score.project_id\
                  and cs_project.id = '" + searchkey + "'"
    cursor.execute(sql_id)
    result_info = cursor.fetchall()
    result_list = []
    for each_info in result_info:
        project_id = str(each_info['pid'])  # 每个项目编号
        each_info['pid'] = project_id
        # 查询各项目的报名人数（已通过+未审核）
        Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + project_id + "' and `status`!=2 "
        cursor.execute(Sql_count)
        result_count = cursor.fetchone()

        count = result_count['count(*)']
        each_info['count'] = count
        if each_info['sex'] == 0:
            each_info['sex'] = '女'
        elif each_info['sex'] == 1:
            each_info['sex'] = '男'

        result_list.append(each_info)
    data_json = json.dumps(result_list, ensure_ascii=False)
    print(data_json)
    return data_json


def admin_search_name():
    print("enter name")
    id = session.get('id')
    print(id)
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 获取管理员所在学院
    cursor = connection.cursor()
    sql_dept = "SELECT department FROM `cs_user` WHERE id='" + id + "'"
    cursor.execute(sql_dept)
    result_dept = cursor.fetchone()  # {'department': 'cs'}
    dept = result_dept['department']

    searchkey = request.json.get('input')
    # 操作sql
    sql_name = "SELECT cs_project.id as pid,cs_project.type,cs_project.name,cs_project.limit_number,cs_user.id,cs_user.sex,cs_score.`status`\
                  FROM cs_project,cs_user,cs_score\
                  WHERE cs_user.department = '" + dept + "' and cs_user.id = cs_score.student_id and cs_project.id = cs_score.project_id\
                  and cs_project.name like '%" + searchkey + "%' "
    cursor.execute(sql_name)
    result_info = cursor.fetchall()
    result_list = []
    for each_info in result_info:
        project_id = str(each_info['pid'])  # 每个项目编号
        each_info['pid'] = project_id
        # 查询各项目的报名人数（已通过+未审核）
        Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + project_id + "' and `status`!=2 "
        cursor.execute(Sql_count)
        result_count = cursor.fetchone()

        count = result_count['count(*)']
        each_info['count'] = count
        if each_info['sex'] == 0:
            each_info['sex'] = '女'
        elif each_info['sex'] == 1:
            each_info['sex'] = '男'

        result_list.append(each_info)
    data_json = json.dumps(result_list, ensure_ascii=False)
    print(data_json)
    return data_json


# 管理员审核比赛报名---通过
def admin_enroll():
    print("enter enroll")
    admin_id = session.get('id')
    project_id = request.json.get('project_id')
    user_id = request.json.get('id')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql_info = "UPDATE cs_score SET `status`= 1 WHERE student_id = '" + user_id + "' and project_id='" + project_id + "'"
    cursor.execute(sql_info)
    connection.commit()

    cursor = connection.cursor()
    sql_return = "SELECT cs_project.id as pid,cs_project.type,cs_project.name,cs_project.limit_number,cs_user.id as use_id,cs_user.sex,cs_score.`status`\
                  FROM cs_project,cs_user,cs_score\
                  WHERE cs_user.id = cs_score.student_id and cs_project.id = cs_score.project_id\
                  and cs_user.id='" + user_id + "' and cs_project.id = '" + project_id + "' "
    cursor.execute(sql_return)
    result_info = cursor.fetchone()

    project_id = str(result_info['pid'])  # 每个项目编号
    result_info['pid'] = project_id
    # 查询各项目的报名人数（已通过+未审核）
    Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + project_id + "' and `status`!=2 "
    cursor.execute(Sql_count)
    result_count = cursor.fetchone()

    count = result_count['count(*)']
    result_info['count'] = count
    if result_info['sex'] == 0:
        result_info['sex'] = '女'
    elif result_info['sex'] == 1:
        result_info['sex'] = '男'

    data_json = json.dumps(result_info, ensure_ascii=False)
    print(data_json)
    return data_json


# 管理员审核比赛报名---不通过
def admin_cancel():
    print("enter cancel")
    admin_id = session.get('id')
    project_id = request.json.get('project_id')
    user_id = request.json.get('id')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql_cancel = "UPDATE cs_score SET `status`= 2 WHERE student_id = '" + user_id + "' and project_id='" + project_id + "'"
    cursor.execute(sql_cancel)
    connection.commit()

    cursor = connection.cursor()
    sql_return = "SELECT cs_project.id as pid,cs_project.type,cs_project.name,cs_project.limit_number,cs_user.id as use_id,cs_user.sex,cs_score.`status`\
                  FROM cs_project,cs_user,cs_score\
                  WHERE cs_user.id = cs_score.student_id and cs_project.id = cs_score.project_id\
                  and cs_user.id='" + user_id + "' and cs_project.id = '" + project_id + "' "
    cursor.execute(sql_return)
    result_info = cursor.fetchone()

    project_id = str(result_info['pid'])  # 每个项目编号
    result_info['pid'] = project_id
    # 查询各项目的报名人数（已通过+未审核）
    Sql_count = "SELECT project_id, count(*) from cs_score where project_id ='" + project_id + "' and `status`!=2 "
    cursor.execute(Sql_count)
    result_count = cursor.fetchone()

    count = result_count['count(*)']
    result_info['count'] = count
    if result_info['sex'] == 0:
        result_info['sex'] = '女'
    elif result_info['sex'] == 1:
        result_info['sex'] = '男'

    data_json = json.dumps(result_info, ensure_ascii=False)
    print(data_json)
    return data_json
