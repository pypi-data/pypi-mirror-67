data = [{  
    "tb_name": "config_log",
    "create_sql": 
    "CREATE TABLE config_log (cfg_id integer PRIMARY KEY autoincrement, host text, port int, user text, passwd text, alias text, deleted int default 0);"
}, {
    "tb_name": "detail",
    "create_sql":
    "create table detail (cfg_id int,detail text)"
}]