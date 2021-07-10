# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 18:18:58 2021

@author: admin
"""

import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()



def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS tasktable(Task TEXT,Task_type TEXT,due_date DATE,due_time INTEGER)')


def add_data(Task,Task_type,due_date,due_time):
	c.execute('INSERT INTO tasktable(Task,Task_type,due_date,due_time) VALUES (?,?,?,?)',(str(Task),str(Task_type),str(due_date),str(due_time)))
	conn.commit()


def view_all_data():
	c.execute('SELECT * FROM tasktable')
	data = c.fetchall()
	return data

def view_all_task_names():
	c.execute('SELECT DISTINCT task FROM tasktable')
	data = c.fetchall()
	return data

def get_task(Task):
	c.execute('SELECT * FROM tasktable WHERE Task="{}"'.format(Task))
	data = c.fetchall()
	return data

def edit_task_data(new_task,new_task_type,new_task_due_date,new_task_due_time,Task,Task_type,due_date,due_time):
	c.execute("UPDATE tasktable SET Task =?,Task_type=?,due_date=? ,due_time = ? WHERE Task=? and Task_type=? and due_date=? and due_time=? ",(str(new_task),str(new_task_type),str(new_task_due_date),str(new_task_due_time),str(Task),str(Task_type),str(due_date),str(due_time)))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(Task):
	c.execute('DELETE FROM tasktable WHERE Task="{}"'.format(Task))
	conn.commit()
