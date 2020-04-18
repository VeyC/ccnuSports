# 裁判页面
import pymysql
import json
from flask import Flask, request, session, jsonify


# 获取裁判负责的所有项目列表
def get_game_list():
    judge_id = session.get('id')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    sql = "SELECT id,type,cs_project.`name`,time ,isfinish from cs_project WHERE judge_id = '" + judge_id + "'"
    cursor.execute(sql)
    result = cursor.fetchall()
    result_li = []
    for each in result:
        Time = each['time'].strftime("%Y-%m-%d-%H")
        each['time'] = Time
        result_li.append(each)
    data_json = json.dumps(result_li, ensure_ascii=False)
    print(data_json)
    return data_json


# 已知project_id,获取该project_name
def get_game_name():
    project_id = str(request.json.get('project_id'))
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    sql = "SELECT name as project_name from cs_project WHERE id = '" + project_id + "'"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result['project_name'])
    return result['project_name']


# 已知project_id,  查询该项目的所有参赛的department、user_id（参赛者or队长）、user_name，socre
def get_game_detail():
    project_id = str(request.json.get('project_id'))
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    sql = "SELECT cs_user.id as id,cs_user.department,cs_user.`name` as name,cs_score.score,cs_score.status from cs_user,cs_project,cs_score\
                                WHERE cs_user.id = cs_score.student_id and cs_project.id = cs_score.project_id and cs_score.status = 1 and cs_project.id = '" + project_id + "' "
    cursor.execute(sql)
    result = cursor.fetchall()
    data_json = json.dumps(result, ensure_ascii=False)
    print(data_json)
    return data_json


# 按学院1/参赛者学号2搜索
def get_search_result():
    global sql
    selected = request.json.get('select')
    search_key = request.json.get('input')
    project_id = str(request.json.get('project_id'))
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    if selected == '1':
        # 已知学院（模糊查询），查询出department，参赛者id, username，score
        sql = "SELECT department,cs_user.id,cs_user.name,cs_score.score,cs_score.status from cs_user,cs_score,cs_project \
                            WHERE cs_score.status = 1 and cs_project.id = cs_score.project_id and cs_score.student_id = cs_user.id and \
                            cs_user.department like '%" + search_key + "%' and cs_project.id = '" + project_id + "'"
    elif selected == '2':
        # 已知参赛者学号，查询出department，user_id,username,score
        sql = "SELECT department,cs_user.id,cs_user.name,cs_score.score,cs_score.status from cs_user,cs_score,cs_project \
                            WHERE cs_score.status = 1 and cs_project.id = cs_score.project_id and cs_score.student_id = cs_user.id and \
                            cs_user.id = '" + search_key + "' and cs_project.id = '" + project_id + "'"
    cursor.execute(sql)
    result = cursor.fetchall()
    data_json = json.dumps(result, ensure_ascii=False)
    print(data_json)
    return data_json


# 已知前端传的project_id,department,user_id,user_name,score，插入数据库，并查询是否成功插入
def save_form():
    print("enter save_form")
    data = request.json.get('tableData')
    project_id = str(request.json.get('project_id'))
    print(data)
    data = json.loads(data)
    print(type(data))
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    for each in data:
        if  each['score'] is not None:
            print(each)
            user_id = each['id']
            score = str(each['score'])
            print(type(score))
            sql = "UPDATE cs_score set score=" + score + " WHERE project_id= '" + project_id + " 'and student_id='" + user_id + "'"
            cursor.execute(sql)
            connection.commit()
    check = '1'
    for each_check in data:
        print(each_check)
        user_id = each_check['id']
        sql_check = "SELECT score from cs_score WHERE student_id ='" + user_id + "'and project_id = '" + project_id + "'"
        cursor.execute(sql_check)
        result = cursor.fetchone()
        if not result['score']:
            check = '0'
    return check


# 已知前端传的project_id,修改isfinish为1
def submit_form():
    project_id = str(request.json.get('project_id'))
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    sql = "UPDATE cs_project set isfinish = 1 WHERE id = '" + project_id + "'"
    cursor.execute(sql)
    connection.commit()
    sql_check = "SELECT isfinish from cs_project WHERE id = '" + project_id + "'"
    cursor.execute(sql_check)
    result = cursor.fetchone()
    if result['isfinish'] == 1:
        check = '1'
    else:
        check = '0'
    print("check:")
    print(check)
    # 查询出该项目的前八名参赛者的信息，放入result_score中
    sql_info = "select * from (\
    								SELECT cs_score.student_id,cs_score.status,cs_user.department,cs_score.score,cs_score.ranking\
    								from cs_score,cs_user WHERE cs_score.status = 1 and project_id = '" + project_id + "' and cs_user.id = cs_score.student_id\
    								ORDER BY score desc)new_table LIMIT 8"
    cursor.execute(sql_info)
    result_score = cursor.fetchall()
    print(result_score)
    # 插入该八名参赛者的排名
    i = 1  # 标记排名
    for each_info in result_score:
        i_str = str(i)
        student_id = each_info['student_id']
        department = each_info['department']
        print(student_id + '===========' + department + '=============' + i_str)
        sql_rank = "update cs_score SET ranking = '" + i_str + "' WHERE student_id = '" + student_id + "' and project_id = '" + project_id + "'"
        cursor.execute(sql_rank)
        connection.commit()
        sql_deptscore = "SELECT * from cs_scoreboard WHERE department = '" + department + "'"
        cursor.execute(sql_deptscore)
        result_deptscore = cursor.fetchone()
        grade = result_deptscore['grade']  # 读取该学院积分
        new_grade = grade + 9 - i
        sql_return = "update cs_scoreboard set grade = '" + str(new_grade) + "' where department = '" + department + "'"
        cursor.execute(sql_return)
        connection.commit()
        i = i + 1
    return check
