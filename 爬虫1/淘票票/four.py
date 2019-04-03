import csv
import os

if not os.path.exists('cinmal_href.csv'):
    f = open('cinmal_href.csv', 'w')
    f.close()
csv_file = csv.reader(open('cinmal_href.csv', 'r'))

stu1 = ['marry',26]
stu2 = ['bob',23]


"""
csv文件的写入
import csv
with open("test.csv","w") as csvfile: 
    writer = csv.writer(csvfile)

    #先写入columns_name
    writer.writerow(["index","a_name","b_name"])
    #写入多行用writerows
    writer.writerows([[0,1,3],[1,2,3],[2,3,4]])
  
csv文件的读取  
import csv
with open("test.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    #这里不需要readlines
    for line in reader:
        print line

"""
