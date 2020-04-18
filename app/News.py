import pymysql
import json
from flask import Flask, request, session, redirect, url_for, render_template, make_response, jsonify
import time

def get_news():
    print("getnews============================================")
    charge_id = session.get('id')
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql_news ="SELECT * FROM `cs_news`"
    cursor.execute(sql_news)
    result_news = cursor.fetchall()

    for each_news in result_news:
        Time = each_news['publishtime'].strftime("%Y-%m-%d %H:%M:%S")
        each_news['publishtime'] = Time
        if each_news['newscharger_id'] == charge_id:
            each_news['self'] = 1
        else:
            each_news['self'] = 0

    data_json = json.dumps(result_news, ensure_ascii=False)
    print(data_json)

    return data_json


def add_news():
    print("addnews============================================")
    charge_id = session.get('id')
    title = request.json.get('title')
    text = request.json.get('text')
    # picture = #插入图片，这里考虑富文本，稍后添加
    time_now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    
    # 获取编号
    sql_count = "SELECT COUNT(*) as num FROM cs_news"
    cursor.execute(sql_count)
    result_count = cursor.fetchone()
    num = result_count['num']
    news_id = 100+num+1

    # 插入数据
    sql_add ="INSERT INTO cs_news VALUES('"+str(news_id)+"','"+charge_id+"',\
             '"+time_now+"','"+title+"','"+text+"')"
    cursor.execute(sql_add)
    connection.commit()
    
    # 重新查询，用于回显
    sql_news ="SELECT * FROM `cs_news`"
    cursor.execute(sql_news)
    result_news = cursor.fetchall()

    for each_news in result_news:
        Time = each_news['publishtime'].strftime("%Y-%m-%d %H:%M:%S")
        each_news['publishtime'] = Time
        if each_news['newscharger_id'] == charge_id:
            each_news['self'] = 1
        else:
            each_news['self'] = 0

    data_json = json.dumps(result_news, ensure_ascii=False)
    print(data_json)

    return data_json
    


def getnews_id():
    print("getnewsid============================================")
    charge_id = session.get('id')
    news_id = request.json.get('input')

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql_info = "SELECT * FROM cs_news WHERE news_id='"+str(news_id)+"'"
    cursor.execute(sql_info)
    result_news = cursor.fetchall()
    rusult_info = result_news[0]

    # 重新查询，用于回显
    Time = rusult_info['publishtime'].strftime("%Y-%m-%d %H:%M:%S")
    rusult_info['publishtime'] = Time

    if rusult_info['newscharger_id'] == charge_id:
        rusult_info['self'] = 1
    else:
        rusult_info['self'] = 0

    data_json = json.dumps(result_news, ensure_ascii=False)
    print(data_json)

    return data_json


def getnews_athlete():
    print("getnewsathlete============================================")
    id = session.get('id')
    news_id = request.json.get('id')
    print(news_id)

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql_info = "SELECT news_id as id,title,publishtime,newscharger_id as publishname,text FROM cs_news WHERE news_id='"+str(news_id)+"'"
    cursor.execute(sql_info)
    result_news = cursor.fetchall()
    rusult_info = result_news[0]

    # 重新查询，用于回显
    Time = rusult_info['publishtime'].strftime("%Y-%m-%d %H:%M:%S")
    rusult_info['publishtime'] = Time

    data_json = json.dumps(result_news, ensure_ascii=False)
    print(data_json)

    return data_json


def getnews_title():
    print("getnewstitle============================================")
    charge_id = session.get('id')
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()    
    sql_info = "select news_id as id ,title from cs_news ORDER BY publishtime desc LIMIT 5"
    cursor.execute(sql_info)
    result_news = cursor.fetchall()
    data_json = json.dumps(result_news, ensure_ascii=False)
    print(data_json)
    return data_json


def revise_news():
    print("revisenews============================================")
    charge_id = session.get('id')
    news_id =str( request.json.get('news_id') )
    title = request.json.get('title')
    text = request.json.get('text')
    # picture = #插入图片，这里考虑富文本，稍后添加

    time_now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    if title != None:
        sql_change = "UPDATE cs_news set title = '"+ title +"' WHERE news_id = '"+ news_id +"'"
    elif text != None: 
        sql_change = "UPDATE cs_news set text = '"+ text +"' WHERE news_id = '"+ news_id +"'"
    cursor.execute(sql_change)
    connection.commit()

    # 用于回血
    sql_news ="SELECT * FROM `cs_news`"
    cursor.execute(sql_news)
    result_news = cursor.fetchall()
    # print(result_news)

    for each_news in result_news:
        Time = each_news['publishtime'].strftime("%Y-%m-%d %H:%M:%S")
        each_news['publishtime'] = Time
        if each_news['newscharger_id'] == charge_id:
            each_news['self'] = 1
        else:
            each_news['self'] = 0

    data_json = json.dumps(result_news, ensure_ascii=False)
    print(data_json)

    return data_json
    

def delete_news():
    print("deletenews============================================")
    charge_id = session.get('id')
    news_id = request.json.get('news_id')

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusportss',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql_delete = "DELETE  FROM `cs_news` WHERE news_id = '"+str(news_id)+"'"
    cursor.execute(sql_delete)
    connection.commit()


    # 重新查询，用于回显
    sql_news ="SELECT * FROM `cs_news`"
    cursor.execute(sql_news)
    result_news = cursor.fetchall()

    for each_news in result_news:
        Time = each_news['publishtime'].strftime("%Y-%m-%d %H:%M:%S")
        each_news['publishtime'] = Time
        if each_news['newscharger_id'] == charge_id:
            each_news['self'] = 1
        else:
            each_news['self'] = 0

    data_json = json.dumps(result_news, ensure_ascii=False)
    print(data_json)
    return data_json
