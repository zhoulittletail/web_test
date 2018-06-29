class Read_txt01():
    def read_txt01(self):
        with open("../DataPool/sjx.txt","r",encoding="utf-8")as f:
            datas = f.readlines()
            list =[]
            for data in datas:
                list.append(data.strip().split(","))
            return list
if __name__ == '__main__':
    print(Read_txt01().read_txt01())