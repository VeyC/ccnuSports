import pymysql
import json
import datetime
import time


if __name__ == '__main__':
    project_id = '10102'
    # 连接数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='ccnusports',
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = connection.cursor()
    sql = "UPDATE cs_project set isfinish = 0 WHERE id = '" + project_id + "'"
    cursor.execute(sql)
    connection.commit()