
import csv
class Read_csv01():
    def read_csv01(self):
        with open("../DataPool/sjx.csv","r",encoding="utf-8")as f:
            datas = csv.reader(f)
            list=[]
            for data in datas:
                list.append(data)
            return list
if __name__ == '__main__':
    print(Read_csv01().read_csv01())