import pymysql
import sys

conn = pymysql.connect(host = '192.168.0.102', user = 'python', passwd = 'a123456', db = 'lck')

try:
    cursor = conn.cursor()
    #光标获取成功
    cursor.execute('CREATE DATABASE T_python;')
    print('创建T-Python数据库成功')
    #创建T-python数据库

    cursor.execute('USE T_python;')
    #进入T-Python数据库

    cursor.execute('CREATE TABLE test_python(id int, name char(20), team char(20), hear char(20));')
    #创建数据表
    print('数据表test_python可以使用')
    conn.commit()

except:
    print('创建表失败，请检查！')
conn.close()


    #except:
        #print('连接失败，请检查！')
        #conn.close()
        #sys.exit()