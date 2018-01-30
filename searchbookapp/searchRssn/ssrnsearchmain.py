#!/usr/bin/env python
# -*- coding: utf-8 -*-
from searchbookapp.searchSql.sqlabout import MyMysql
from searchbookapp.searchRssn.ssrnspider_outmoded import Ssrn
sq = "REPLACE　INTO ssrnpaper (gid ,title, author, link, downloads) VALUES "

if __name__ == "__main__":
    # # 如果表不存在创建相关表
    # mysqlQuery = MyMysql("192.168.1.158", "root", "123456", "ssrnDB")
    # mysqlQuery.ExecNonQuery(sql2)

    mm = Ssrn()
    tt = mm.getPaperInfoList()
    for i in tt:
        sql = sq + "(" + '{},"{}","{}","{}",{}'.format(i[0], str(i[1]), str(i[2]), str(i[3]), i[4]) + ");"
        print(sql)
        mysqlQuery = MyMysql("192.168.1.158", "root", "123456", "ssrnDB")
        mysqlQuery.ExecNonQuery(sql)


