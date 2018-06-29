import csv
class Read_csv():
    def read_csv(self):
        with open("../DataPool/sjx.csv","r",encoding="utf-8") as f:
            datas = csv.reader(f)
            list = []
            for date in datas:
                list.append(date)
            return list
if __name__ == '__main__':
    print(Read_csv().read_csv())