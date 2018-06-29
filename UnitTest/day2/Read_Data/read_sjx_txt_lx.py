class Read_txt():
    def read_txt(self):
        with open("../DataPool/sjx.txt","r",encoding="utf_8")as f:
            datas = f.readlines()
            list = []
            for data in datas:
                list.append(data.strip().split(","))
            return  list
if __name__ == '__main__':
    print(Read_txt().read_txt())