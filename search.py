#!/usr/bin/python
#coding: utf8
from lxml import etree
import fdb
import sys
import logging
def main():
 username='SYSDBA'
 password='TMohXJDr'
 hostname='10.9.4.14'
 concodepage='WIN1251'
 codepage='WIN1251'
 databases='all2007_02','all2007_01','all2007_05','all2007_07','all2007_09','all2007_10','all2007_11','all2008_01','all2008_02','all2008_03','all2008_04','all2008_05','all2008_06','all2008_07','all2008_08','all2008_09','all2008_10','all2008_11','all2009_02','all2009_03','all2009_04','all2009_05','all2009_06','all2009_07','all2009_08','all2009_09','all2009_10','all2009_11','all2009_12','all2010_02','all2010_03','all2010_04','all2010_05','all2010_06','all2010_07','all2010_08','all2010_09','all2010_10','all2010_11','all2010_12'
 for dd in databases:
  print dd
  try:
   con = fdb.connect (host=hostname, database=dd, user=username,password=password,charset=concodepage,port=3050)
  except  Exception, e:
   print("Ошибка при открытии базы данных:\n"+str(e))
   sys.exit(2)
  sql=u"select ip.num_ip,name_d,name_v,ip.sum_ from ip where upper( ip.name_v) containing upper('Джанчерова')" #and upper( ip.name_v) containing upper('Лариса')"
  cur = con.cursor()
  #print sql
  cur.execute(sql)
  row=cur.fetchall()
  #print len (row)
  if len (row)>0:
   for rr in row:
    print rr[0],rr[1],rr[2]
  con.close()
if __name__ == "__main__":
    main()
