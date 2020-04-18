# 比赛结果
import pymysql
import json
from flask import Flask, request, session, redirect, url_for, render_template, make_response, jsonify


# 比赛结果表格
def get_gameresult():
    print("enter get_gameresult")
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    selectUserSql = "SELECT cs_project.id as project_id,cs_project.type as type,cs_project.`name` as project_name,cs_project.time,cs_user.id as user_id,cs_user.name as user_name,cs_user.department as department,\
                                cs_score.score as score,cs_score.ranking as ranking\
                                from cs_user,cs_score,cs_project\
                                where cs_user.id = cs_score.student_id and cs_project.id = cs_score.project_id"
    cursor.execute(selectUserSql)
    data_info = cursor.fetchall()
    result_li = []
    for each_info in data_info:
        Time = each_info['time'].strftime("%Y-%m-%d-%H")
        each_info['time'] = Time
        result_li.append(each_info)
    data_json = json.dumps(result_li, ensure_ascii=False)
    print(data_json)
    return data_json


# 比赛结果搜索
def get_selected():
    print("get selected")
    selected = request.json.get('select')
    input_key = request.json.get('input')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    if selected == '1':
        # 按项目名称搜索
        selectUserSql = "SELECT cs_project.id as project_id,cs_project.type as type,cs_project.name as project_name,cs_project.time,\
                                            cs_user.id as user_id,cs_user.`name` as user_name,cs_user.department as department,cs_score.score as score,cs_score.ranking as ranking\
                                            FROM cs_user,cs_score,cs_project\
                                            WHERE cs_score.project_id = cs_project.id and cs_score.student_id = cs_user.id and cs_project.`name` like '%" + input_key + "%'"
    elif selected == '2':
        # 按学院搜索
        selectUserSql = "SELECT cs_project.id as project_id,cs_project.type as type,cs_project.name as project_name,cs_project.time,cs_user.id as user_id,cs_user.name as user_name,cs_user.department as department,\
                                         cs_score.score as score,cs_score.ranking as ranking\
                                        from cs_user,cs_score,cs_project\
                                         where cs_user.id = cs_score.student_id and cs_project.id = cs_score.project_id and cs_user.department like '%" + input_key + "%'"
    elif selected == '3':
        # 按学号搜索
        selectUserSql = "SELECT cs_project.id as project_id,cs_project.type as type,cs_project.`name` as project_name,cs_project.time,cs_user.id as user_id,cs_user.name as user_name,cs_user.department as department,\
                                        cs_score.score as score,cs_score.ranking as ranking \
                                        from cs_user,cs_score,cs_project\
                                        where cs_user.id = cs_score.student_id and cs_project.id = cs_score.project_id and cs_user.id = '" + input_key + "'"
    cursor.execute(selectUserSql)
    data_info = cursor.fetchall()
    result_li = []
    for each_info in data_info:
        Time = each_info['time'].strftime("%Y-%m-%d-%H")
        each_info['time'] = Time
        result_li.append(each_info)
    data_json = json.dumps(result_li, ensure_ascii=False)
    print(data_json)
    return data_json


# 查看积分
def get_score_board():
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    sql = "SELECT * from cs_scoreboard ORDER BY grade DESC"
    cursor.execute(sql)
    data = cursor.fetchall()
    data_json = json.dumps(data, ensure_ascii=False)
    print(data_json)
    return data_json