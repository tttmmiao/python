#!/usr/bin/env python 
#coding:utf-8
import os  
import time
import sys  
reload(sys)    
import MySQLdb

# 根据某个维度拆分数据，拆分后表名为 _xxxx

Host = 'xxx'
User = "xxx"
Passwd = 'xxx'
DB = "x"
Port = 3306 
source_table = "xxxx"

conn = MySQLdb.connect(host=Host,user=User,passwd=Passwd,db=DB,port=Port)
cur = conn.cursor()


def get_warehouse_list():
    sql = 'select distinct(warehouse_id) from %s'
    cur.execute(sql % source_table)
    ids=[]
    for row in cur.fetchall():
        ids.append(row[0])
    return ids


def get_target_name(warehouse_id):
    number = "%04d" % (warehouse_id-1)
    target_name = source_table+"_"+number
    return target_name

def dump_mysql(condition,export_file):   
        print "dump the host database to local"                                       
        os.popen("mysqldump -h%s -u%s -p%s -P %d --default-character-set=utf8 %s  %s --where %s> %s"    # 
                                            % (Host, User ,  
                                            Passwd, Port, DB,
                                            source_table, condition ,export_file)) 
    
def replace_str(file_path, old_str,new_str):
    try:  
        f = open(file_path,'r+')  
        all_lines = f.readlines()  
        f.seek(0)  
        f.truncate()  
        for line in all_lines:  
            line = line.replace(old_str, new_str)  
            f.write(line)  
        f.close()  
    except Exception,e:  
        print e
# 导出数据
def dump_data(warehouse_id):
    targetTbName = get_target_name(warehouse_id)
    print "targetTbName:" + targetTbName
    condition = "  warehouse_id="+str(warehouse_id)
    print condition
    dump_mysql(condition,targetTbName)
    replace_str(targetTbName, source_table,targetTbName)

def load_sql(target_table,import_file):   
        print "import sql data :" + target_table 
        x =  "mysql -h%s -u%s -p%s -P%d  %s -f < %s" % (Host, User, Passwd, Port, DB,import_file)
        #print x
        os.popen(x)

# 导入数据
def load_data(warehouse_id):
    targetTbName = get_target_name(warehouse_id)
    print targetTbName
    import_file = targetTbName
    load_sql(targetTbName,import_file)

def dump():
    ids = get_warehouse_list()   
    for index in range(len(ids)): 
        dump_data(ids[index]) 

def load():
    ids = get_warehouse_list()  
    for index in range(len(ids)): 
        load_data(ids[index]) 

def check_params():
    print "Host="+Host+"\n User="+User+"\n DB="+DB +"\n source_table="+source_table + "\n"
    confirm = input("mysqldump导出确认(1确认or 0退出):")
    if confirm == 1:
        print '已确认，执行ing'
    elif confirm == 0:
        sys.exit(-1)
    else:
        print "Only 1 or 0\n"  
        sys.exit(-1)

if __name__ == "__main__": 
    command = input("请输入命令：1(mysqldump导出数据) 或者 2(mysql导入)\n")
    if command == 1:
        check_params()
        dump()
        print("导出完成!")
    elif command == 2:
        check_params()
        load()
        print("导出完成!")
    else:
        print "Only mysqldump or mysql\n"  # should never print
        sys.exit(-1)


