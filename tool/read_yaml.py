import yaml


def read_yaml(filename):
    # 定义空字列表，组装测试数据
    file_path = "./data/" + filename
    arr = []
    # 获取文件流
    with open(file_path, 'r', encoding='utf-8') as f:
        # 遍历
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))
    # 返回结果
    print(arr)
    return arr

