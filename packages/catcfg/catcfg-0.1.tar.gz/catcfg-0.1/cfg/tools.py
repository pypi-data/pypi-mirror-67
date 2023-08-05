# -*- coding: utf-8 -*-
# @Description: 
# @Author: kowhoy
# @Date:   2020-04-29 11:08:29
# @Last Modified by:   zhouke
# @Last Modified time: 2020-04-29 15:27:55


import sqlite3
import datetime
import os
import json
from . import db

cwd = os.path.realpath(__file__)
cwd = "/".join(cwd.split("/")[:-1])

db_name = cwd+"/catcfg.db"

conn = sqlite3.connect(db_name)

def format_stdout(msg, format_type):
    format_type_dict = {
        "success": "🌈",
        "failure": "❌",
        "finish": "✅",
        "wait": "⌛️"
    }

    msg = format_type_dict[format_type] + "\t" + str(msg) + "\t" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(msg)


def execute(sql):
    conn.execute(sql)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def fetchall(sql):
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


def init():
    try:
        sql_json = db.data
        for sql_dict in sql_json:
            create_sql = sql_dict['create_sql']
            tb_name = sql_dict['tb_name']
            msg = "{tb_name} initialization completed".format(tb_name=tb_name)

            conn.execute(create_sql)
            format_stdout(msg, 'success')
    except Exception as e:
        sug = str(e)
        if 'exists' in str(e):
            sug  = str(e) + " , you should try catcfg formatting"
        format_stdout(sug, 'failure')

    format_stdout('innitializtion finished', 'finish')


def formatting():
    try:
        sql_json = db.data
        for sql_dict in sql_json:
            tb_name = sql_dict['tb_name']

            drop_sql = 'drop table {tb_name}'.format(tb_name=tb_name)
            conn.execute(drop_sql)
            msg = "{tb_name} has dropped".format(tb_name=tb_name)
            format_stdout(msg, "success")

    except Exception as e:
        format_stdout(e, 'failure')

    init()

    format_stdout('formatting finished', 'finish')

def get_list_by_condition(condition=""):
    if condition == "":
        sql = 'select host, port, user, passwd, alias from config_log where deleted = 0'
    else:
        sql = '''select distinct host, port, user, passwd, alias from config_log a, detail b where a.cfg_id = b.cfg_id
        and b.detail like "%%{condition}%%" '''.format(condition=condition)

    list_data = fetchall(sql)

    result = {}

    for d in list_data:
        for idx, val in d.items():
            if idx not in result:
                result[idx] = []

            result[idx].append(val)

    return result


def get_ld_by_condition(condition):
    if condition == "":
        sql = 'select host, port, user, passwd, alias from config_log where deleted = 0'
    else:
        sql = '''select distinct host, port, user, passwd, alias from config_log a, detail b where a.cfg_id = b.cfg_id
        and b.detail like "%%{condition}%%" '''.format(condition=condition)

    list_data = fetchall(sql)
    return list_data


def add(host, port, user, passwd, alias):
    insert_sql = '''
        insert into config_log (host, port, user, passwd, alias)
        values ('{host}', '{port}', '{user}', '{passwd}', '{alias}')
    '''.format(host=host, port=port, user=user, passwd=passwd, alias=alias)

    cursor = conn.cursor()
    cursor.execute(insert_sql)
    conn.commit()

    cfg_id_sql = 'select max(cfg_id) from config_log'
    cursor.execute(cfg_id_sql)
    cfg_id = cursor.fetchone()[0]

    insert_sql_2 = '''
    insert into detail (cfg_id, detail) values
    ({cfg_id}, '{host}'),
    ({cfg_id}, '{port}'),
    ({cfg_id}, '{user}'),
    ({cfg_id}, '{passwd}'),
    ({cfg_id}, '{alias}')
    '''.format(cfg_id=cfg_id, host=host, port=port, user=user, passwd=passwd, alias=alias)

    cursor.execute(insert_sql_2)
    conn.commit()

    format_stdout("insert finished", 'wait')


def rm_by_id(id):
    exists_sql = 'select * from config_log where deleted = 0 and cfg_id = {id}'.format(id=id)

    result = fetchall(exists_sql)

    if len(result) == 0:
        format_stdout("the record is not exist", "failure")
    else:
        sql = '''
            update config_log set deleted = 1 where cfg_id = {id}
        '''.format(id=id)

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            format_stdout("deleted success", "success")
        except Exception as e:
            format_stdout(e, "failure")

