import json
class Read_json():
    def read_json(self):
        with open("../DataPool/sjx01.json","r",encoding="utf-8")as f:
            datas = json.load(f)
            return datas["data"]
if __name__ == '__main__':
    print(Read_json().read_json())


