# 导入JSON包
import json
# 打开JSON文件并解析
class Read_json():
    def read_json(self):
        with open("../DataPool/sjx.json","r",encoding='utf-8' )as f:
            result = json.load(f)
            return result["data"]
if __name__ == '__main__':
    print(Read_json().read_json())