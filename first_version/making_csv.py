import os
import pandas as pd
import csv

path = "./imgs"
file_list = os.listdir(path)
print("imgs 폴더 파일 리스트로 불러옴")


dir = "./"
csv_name = "players_21"
f_read = open('{}/{}.csv'.format(dir,csv_name),'r',encoding='UTF8')
lines = f_read.readlines()
f_read.close()
print("players_21.csv 를 열었음")


f = open('file_ovr.csv','w', newline='')
wr = csv.writer(f)
for i in file_list:
	file_name =  i.split('.')[0]
	ovr = lines[int(file_name)].split(",")[12]
	wr.writerow(["./imgs/" + file_name + ".jpg", ovr])

f.close()
print("csv 작성완료")

