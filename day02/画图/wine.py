# -*- coding:utf-8 -*-
import pymysql as pm

con = pm.connect(host='localhost', user='root', password="123456", database='test', port=3306)
cour = con.cursor()

sql1 = '''create table wine(
	exam_id int primary key auto_increment,
	type_id tinyint,
	water float,
	Ethanol float,
	酒石酸 float,
	苹果酸 float,
	柠檬酸 float,
	乳酸 float,
	醋酸 float,
	自然红色素 float,
	单宁 float,
	糖份	float,
	芳香物质 float,
	蛋白质 float,
	氨基酸 float 
);'''
# cour.execute(sql1)
num = 1
with open('wine.data', encoding="utf-8") as file:
    s = file.readline()
    while s is not None and s != "":
        sql2 = 'insert into wine values ({},'.format(num)
        ls = s.split(",")
        for i in ls:
            sql2 = sql2 + i + ','
        sql2 = sql2[:len(sql2) - 1] + ');'
        print(sql2)
        cour.execute(sql2)
        num += 1
        s = file.readline()
con.commit()
cour.close()
con.close()
