#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
class InsertMysql(object):
    def __init__(self, ip, user, password, dbname):
        self.user = user
        self.password = password
        self.ip = ip
        self.dbname = dbname

    def instantiateMysql(self):
        """连接数据库并返回一个pymysql游标
        """
        db = pymysql.connect(self.ip, self.user, self.password, self.dbname).cursor()
        print(self.ip, self.user, self.password, self.dbname)
        return db

    @staticmethod
    def createDbConfig():
        sqlSsrn = """CREATE TABLE `employee` (
          `id` int(10) NOT NULL AUTO_INCREMENT,
          `first_name` char(20) NOT NULL,
          `last_name` char(20) DEFAULT NULL,
          `age` int(11) DEFAULT NULL,
          `sex` char(1) DEFAULT NULL,
          `income` float DEFAULT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
        return sqlSsrn
    def insertData(self):
        pass

mysqlconn = InsertMysql("192.168.1.158", "root", "123456", "ssrnDB")
# cursor = mysqlconn.instantiateMysql()
# cursor.execute(InsertMysql.createDbConfig())

