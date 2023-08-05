# -*- coding: utf-8 -*-
# @Description: 
# @Author: kowhoy
# @Date:   2020-04-29 10:31:13
# @Last Modified by:   zhouke
# @Last Modified time: 2020-04-29 15:27:58


import click
from . import tools
from pylsy import pylsytable
import csv

def table_stdout(list_dict):
    if list_dict == {}:
        tools.format_stdout("no data", "finish")
    else:
        table_head = [i for i in list_dict if i != 'deleted']
        table = pylsytable(table_head)

        for idx, data in list_dict.items():
            if idx != 'deleted':
                table.add_data(idx, data)

        print(table)


@click.group()
def cli():
    pass


@click.command()
def init():
    tools.init()

@click.command()
def formatting():
    tools.formatting()

@click.command()
def l():
    list_dict = tools.get_list_by_condition()
    table_stdout(list_dict)

@click.command()
@click.option("-h", default="", help="config's host")
@click.option("-port", default="", help="config's port")
@click.option("-u", default="", help="config's user")
@click.option("-p", default="", help="config's passwd")
def add(h, port, u, p):
    alias = input("config's alias/remark:")

    tools.add(h, port, u, p, alias)

@click.command()
@click.option("-k", default="", help="search keyword")
def s(k):
    list_dict = tools.get_list_by_condition(k)
    table_stdout(list_dict)

@click.command()
@click.option("-id", default="", help="the config's id")
def rm(id):
    if id == "":
        tools.format_stdout("require the config's id", "failure")
    else:
        tools.rm_by_id(id)

@click.command()
@click.option("-csv_file", default="", help="upload from csv file")
@click.option("-cfg_file", default="", help="upload from cfg file")
@click.option("-json_file", default="", help="upload from json file")
def upload(csv_file, cfg_file, json_file):
    if csv_file == "" and cfg_file == "" and json_file == "":
        tools.format_stdout("require the upload file's path", "failure")
    else:
        if csv_file != "":
            try:
                with open(csv_file, "r") as f:
                    csv_f = csv.reader(f)
                    for idx, row in enumerate(csv_f):
                        if idx == 0 and row != ["host", "port", "user", "passwd", "alias"]:
                            tools.format_stdout("the csv file's head should like |host|port|user|passwd|alias", "failure")
                            raise

                        if idx != 0:
                            tools.add(row[0], row[1], row[2], row[3], row[4])
            except Exception as e:
                tools.format_stdout(e, 'failure')


        if cfg_file != "":
            import configparser
            cp = configparser.ConfigParser()
            try:
                cp.read(cfg_file)
                sections = cp.sections()
                for alias in sections:
                    sec = cp[alias]
                    host = sec['host'] if 'host' in sec else ''
                    port = sec['port'] if 'port' in sec else ''
                    user = sec['user'] if 'user' in sec else ''
                    passwd = sec['passwd'] if 'passwd' in sec else ''
                    tools.add(host, port, user, passwd, alias)
            except Exception as e:
                tools.format_stdout(e, 'failure')


        if json_file != "":
            import json
            try:
                with open(json_file, "r") as f:
                    json_data = json.loads(f.read())

                for d in json_data:
                    host = d.get("host", "")
                    port = d.get("port", "")
                    user = d.get("user", "")
                    passwd = d.get("passwd", "")
                    alias = d.get("alias", "")

                    tools.add(host, port, user, passwd, alias)
            except Exception as e:
                tools.format_stdout(e, 'failure')

        tools.format_stdout('upload finished', 'finish')


@click.command()
@click.option("-k", default="", help="search keyword")
@click.option("-csv_file", default="", help="saved csv file's path")
@click.option("-cfg_file", default="", help="saved cfg/ini/conf... file's path")
@click.option("-json_file", default="", help="saved json file's path")
def download(k, csv_file, cfg_file, json_file):
    
    list_dict = tools.get_ld_by_condition(k)
    if csv_file != "":
        
        try:
            head =  ["host", "port", "user", "passwd", "alias"]

            rows = []
            for dt in list_dict:
                rows.append([dt['host'], dt['port'], dt['user'], dt['passwd'], dt['alias']])

            with open(csv_file,'w')as f:
                f_csv = csv.writer(f)
                f_csv.writerow(head)
                f_csv.writerows(rows)
                tools.format_stdout('saved to ' + csv_file, 'success')
        except Exception as e:
            tools.format_stdout(e, 'failure')


    if cfg_file != "" or (csv_file == "" and cfg_file == "" and json_file == ""):
        import configparser
        try:
            cfg_file = cfg_file if cfg_file != "" else "./catconfig.cfg"
            cp = configparser.ConfigParser()
            for dt in list_dict:
                cp[dt['alias']] = {
                    "host": dt['host'],
                    "port": dt['port'],
                    "user": dt['user'],
                    "passwd": dt['passwd']
                }

            with open(cfg_file, 'w') as f:
                cp.write(f)
            tools.format_stdout('saved to ' + cfg_file, 'success')
        except Exception as e:
            tools.format_stdout(e, 'failure')

    if json_file != "":
        import json
        try:
            json_data = json.dumps(list_dict, ensure_ascii=False)

            with open(json_file, 'w') as f:
                f.write(json_data)

            tools.format_stdout('saved to ' + json_file, 'success')
        except Exception as e:
            tools.format_stdout(e, 'failure')
        


cli.add_command(init)
cli.add_command(formatting)
cli.add_command(l)
cli.add_command(add)
cli.add_command(s)
cli.add_command(rm)
cli.add_command(upload)
cli.add_command(download)

if __name__ == "__main__":
    cli()