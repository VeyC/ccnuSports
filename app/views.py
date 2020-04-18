# -*- coding: utf-8 -*-


from app import app, Login, Enroll, GameResult, Admin, SelfInfo, Judge, News
from flask import Flask, session, render_template, jsonify


# token加密解密

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='ccnusports')


@app.route('/api/login', methods=['POST',])
def user_login():
    return Login.user_login()


@app.route('/api/logout', methods=['POST',])
def user_logout():
    return Login.user_logout()


@app.route('/api/getUsername', methods=["POST",])
def get_username():
    return SelfInfo.get_username()


@app.route('/api/searchType',methods=["POST",])
def search_type():
    return Enroll.search_type()


@app.route('/api/searchName', methods=["POST",])
def search_name():
    return Enroll.search_name()


@app.route('/api/searchId',methods=["POST",])
def search_id():
    return Enroll.search_id()


@app.route('/api/getProjectInfo', methods=["POST",])
def get_project():
    return Enroll.get_project()


# 注销有问题
@app.route('/api/logout', methods=["POST",])
def logout():
    session.clear()
    print("session确实被删除了")
    print(session['id'])
    print("123")
    code = 0
    if session['id'] == "":
        code = 1
    return code


# 比赛报名
@app.route('/api/enrollProject', methods=['POST',])
def enroll():
    return Enroll.enroll()


# 取消报名
@app.route('/api/cancelProject', methods=['POST',])
def cancel():
    return Enroll.cancel()


# 报名信息
@app.route('/api/enrollInfo', methods=['POST',])
def enroll_info():
    return Enroll.enroll_info()


# 个人信息
@app.route('/api/selfInfo', methods=['POST',])
def self_info():
    return SelfInfo.self_info()


# 修改电话号码
@app.route('/api/changeTel', methods=['POST',])
def change_tel():
    return SelfInfo.change_tel()


# 比赛结果表格
@app.route('/api/getGameresult', methods=['POST',])
def get_gameresult():
    return GameResult.get_gameresult()


# 比赛结果搜索
@app.route('/api/getselectedresult', methods=['POST',])
def get_selected():
    return GameResult.get_selected()


# 查看积分
@app.route('/api/getScoreBoard', methods=['POST',])
def get_score_board():
    return GameResult.get_score_board()


# 管理员主页
@app.route('/api/admingetProjectInfo', methods=['POST', ])
def admin_project():
    return Admin.admin_project()


@app.route('/api/adminsearchType', methods=["POST", ])
def admin_search_type():
    return Admin.admin_search_type()


@app.route('/api/adminsearchId', methods=["POST", ])
def admin_search_id():
    return Admin.admin_search_id()


@app.route('/api/adminsearchName', methods=["POST", ])
def admin_search_name():
    return Admin.admin_search_name()


# 管理员审核比赛报名---通过
@app.route('/api/adminenrollProject', methods=['POST', ])
def admin_enroll():
    return Admin.admin_enroll()


# 管理员审核比赛报名---不通过
@app.route('/api/admincancelProject', methods=['POST', ])
def admin_cancel():
    return Admin.admin_cancel()


# 获取裁判负责的所有项目列表
@app.route('/api/getGameList', methods=['POST',])
def get_game_list():
    return Judge.get_game_list()


# 已知project_id,获取该project_name
@app.route('/api/getGameName', methods=['POST',])
def get_game_name():
    return Judge.get_game_name()


# 已知project_id,  查询该项目的所有参赛的department、user_id（参赛者or队长）、user_name，socre
@app.route('/api/getGameDetail', methods=['POST',])
def get_game_detail():
    return Judge.get_game_detail()


# 按学院1/参赛者学号2搜索
@app.route('/api/searchResult', methods=['POST',])
def get_search_result():
    return Judge.get_search_result()


# 已知前端传的project_id,department,user_id,user_name,score，插入数据库，并查询是否成功插入
@app.route('/api/saveForm', methods=['POST',])
def save_form():
    return Judge.save_form()


# 已知前端传的project_id,修改isfinish为1
@app.route('/api/submitForm', methods=['POST',])
def submit_form():
    return Judge.submit_form()


# 新闻负责人主页,显示所有新闻
@app.route('/api/getallnews', methods=['POST',])
def get_news():
    return News.get_news()


# 添加新闻
@app.route('/api/addnews', methods=['POST',])
def add_news():
    return News.add_news()


# 通过新闻编号显示新闻内容
@app.route('/api/getnewsbyid', methods=['POST',])
def getnews_id():
    return News.getnews_id()


# 通过新闻编号显示新闻内容,用于运动员页面
@app.route('/api/getnews', methods=['POST',])
def getnews_athlete():
    return News.getnews_athlete()


# 通过新闻编号显示新闻内容,用于运动员页面
@app.route('/api/getNewsTitle', methods=['POST',])
def getnews_title():
    return News.getnews_title()


# 修改新闻
@app.route('/api/revisenews', methods=['POST',])
def revise_news():
    return News.revise_news()


# 删除新闻
@app.route('/api/deletenews', methods=['POST',])
def delete_news():
    return News.delete_news()
