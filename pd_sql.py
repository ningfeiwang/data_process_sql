#!/usr/local/bin/python
# coding:utf-8

import mysql.connector as sql
import pandas as pd

def connect():

	db_connection = sql.connect( database='uniquemachine', user='root', password='485002wnf')
	db_cursor = db_connection.cursor()
	# db_cursor.execute('SELECT * FROM features')
	db_cursor.execute('SELECT * FROM features')
	rows = db_cursor.fetchall() 
	# for row in rows:  
	# 	print row[15] 
	# 	# 0 ip, 9 gpuimgs, 15 agent
	return rows
	# f = pd.read_sql('SELECT * FROM table_name', con=db_connection)

def get_dis_num(data,k):
	tmp = []
	for i in range(0,len(data)):
		tmp.append(data[i][k])
	s = set(tmp)
	return len(s)

if __name__ == '__main__':
	# agent = []
	gpuimgs = []
	gpuimgs_webgl = []
	gpuimgs_unigl= []
	rows = connect()
	i = 0
	for row in rows:
		if 'iPhone' in row[15]:
			continue
		if 'Android' in row[15]:
			continue
		if "Chrome" not in row[15]:
			continue
		if row[9] is None:
			continue
		# print row[15]
		i += 1
		# agent.append(row[15])

		a = row[9].split('-')
		gpuimgs.append(a)
	for i in range(0, len(gpuimgs)):
		# print gpuimgss
		if len(gpuimgs[i]) == 22:
			gpuimgs_webgl.append(gpuimgs[i])
		if len(gpuimgs[i]) == 16:
			gpuimgs_unigl.append(gpuimgs[i])
	k = 9
	# print gpuimgs_webgl
	# num_webgl = get_dis_num(gpuimgs_webgl,k)
	# print num_webgl
	num_unigl = get_dis_num(gpuimgs_unigl,k)
	print num_unigl

	# tmp = []
	# for i in range(0,len(gpuimgs_webgl[0])):
	# 	tmp.append(gpuimgs_webgl[0][0])
	# 	tmp.
	# print len(gpuimgs_webgl)
	# print len(gpuimgs_unigl)
		# print row[9]
	# print i
	# print len(rows)





# table_rows = db_cursor.fetchall()

# df = pd.DataFrame(table_rows)
# print table_rows