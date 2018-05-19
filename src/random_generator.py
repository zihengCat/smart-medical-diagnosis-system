import numpy as np
import csv

# 读取医疗指标数据集
def read_data():
    f = open('input_data.txt', 'rt')
    data_list = list()
    # 转换为列表返回
    for l in f.readlines():
        data_list.append(l.replace('\n', ''))
    return data_list

def generate_data():

    # 获取医疗指标列表
    data_list = read_data()
    id_list = list()

    # ID化医疗指标 =>
    # A0, A1, A2 ... An
    for i in data_list:
        id_list.append([data_list.index(i), i])

    # 确定各项医疗指标的正常范围
    # 数据结构：[id, [下限, 上限]]
    range_list = list()
    # 0 => 性别 [0, 1]
    range_list.append([0, [0, 1]])

    # 1 => 年龄 [10, 80]
    range_list.append([1, [10, 80]])

    # 2 => 尿素 [20, 71]
    range_list.append([2, [2, 7.1]])

    # 3 => 肌酐 [53, 115]
    range_list.append([3, [53, 115]])

    # 4 => 尿酸 [89, 357]
    range_list.append([4, [89, 357]])

    # 5 => 血清尿酸 [150 ,420]
    range_list.append([5, [150, 420]])

    # 6 => 碱性磷酸酶 [45, 125]
    range_list.append([6, [45, 125]])

    # 7 => 血清总蛋白 [60, 80]
    range_list.append([7, [60, 80]])

    # 8 => 血清白蛋白 [3.5, 5.5]
    range_list.append([8, [3.5, 5.5]])

    # 9 => 球蛋白 [2.1, 3.5]
    range_list.append([9, [2.1, 3.5]])

    # 10 => A/G [1.2, 2.5]
    range_list.append([10, [1.2, 2.5]])

    # 11 => 血清总胆红素 [3, 21]
    range_list.append([11, [3, 21]])

    # 12 => 血清直接胆红素 [1, 7]
    range_list.append([12, [1, 7]])

    # 13 => 血清间接胆红素 [1, 13]
    range_list.append([13, [1, 13]])

    # 14 => 血清前白蛋白 [240, 350]
    range_list.append([14, [240, 350]])

    # 15 => 'ALT/AST' [5, 40]
    range_list.append([15, [5, 40]])

    # 16 => 血清总胆固醇 [2.86, 5.98]
    range_list.append([16, [2.86, 5.98]])

    # 17 => 血清甘油三酯 [0.5, 0.7]
    range_list.append([17, [0.5, 0.7]])

    # 18 => 血清甘油三酯 [0.5, 0.7]
    range_list.append([18, [0.5, 0.7]])

    # 19 => 血清高密度脂蛋白胆固醇 [1.06, 1.56]
    range_list.append([19, [1.06, 1.56]])

    # 20 => 血清低密度脂蛋白胆固醇 [105, 130]
    range_list.append([20, [105, 130]])

    # 21 => 血清载脂蛋白A1
    range_list.append([21, [100, 160]])

    # 22 => 血清载脂蛋白B [0.75, 0.9]
    range_list.append([22, [0.75, 0.9]])

    # 23 => 血清载脂蛋白a  [0.8, 2.5]
    range_list.append([23, [0.8, 2.5]])

    # 24 => 血清丙氨酸氨基转移酶 [1, 35]
    range_list.append([24, [1, 35]])

    # 25 => 血清天门冬氨酰基转移酶 [15, 40]
    range_list.append([25, [15, 40]])

    # 26 => 血清γ--谷氨酰基转移酶 [10, 50]
    range_list.append([26, [10, 50]])

    # 27 => 血清碳酸氢盐 [23, 29]
    range_list.append([27, [23, 29]])

    # 28 => 乳酸脱氢酶 [100, 300]
    range_list.append([28, [100, 300]])

    # 29 => 血清肌酸激酶 [18, 198]
    range_list.append([29, [18, 198]])

    # 30 => 血清肌酸激-酶MB [0.1, 0.6]
    range_list.append([30, [18, 198]])

    # 31 => 同功酶活性 [10, 24]
    range_list.append([31, [10, 24]])

    # 32 => 血清a羟基丁酸脱氢酶 [80, 220]
    range_list.append([32, [80, 220]])

    # 33 => 钾测定 [25, 100]
    range_list.append([33, [25, 100]])

    # 34 => 钠测定 [130, 260]
    range_list.append([34, [130, 260]])

    # 35 => 氯测定 [170, 250]
    range_list.append([35, [170, 250]])

    # 36 => 钙测定 [100, 300]
    range_list.append([36, [100, 300]])

    # 37 => 葡萄糖 [70, 140]
    range_list.append([37, [70, 140]])
    #print(id_list)
    #print(range_list)
    return range_list

# 生成正常人的数据集
def generate_normal():
    # 获取各项医疗指标的正常范围
    range_list = generate_data()

    # 设置 Numpy 随机数种子
    random = np.random.RandomState(0)
    all_data = [ ]
    # 生成数据数量：1000
    for i in range(1000):
        data_list = [ ]
        # 数据结构：[id, [下限, 上限]]
        for j in range_list:
            # 处理性别（只能为男或女）
            if(j[0] == 0):
                data_list.append(round(random.uniform(j[1][0], j[1][1]), 0))
                continue
            # 处理性别（应取整数）
            if(j[0] == 1):
                data_list.append(round(random.uniform(j[1][0], j[1][1]), 0))
                continue
            # 加入剩余医疗数据项
            data_list.append(round(random.uniform(j[1][0], j[1][1]), 2))
        # 加入数据标签
        data_list.append('normal')
        # 合成完整数据添加
        all_data.append(data_list)

    # CSV 表头
    # A0, A1, A2 ... An, result
    headers = []
    for i in range(len(all_data[0]) - 1):
        headers.append('A' + str(i))
    headers.append('result')

    # 写入 CSV 文件
    with open('records_normal.csv','w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(all_data)

# 生成高血压病人的数据集
def generate_gaoxueya():
    range_list = generate_data()
    random = np.random.RandomState(0)
    all_data = [ ]
    for i in range(1000):
        data_list = [ ]
        for j in range_list:
            # 处理性别（男女）
            if(j[0] == 0):
                data_list.append(round(random.uniform(j[1][0], j[1][1]), 0))
                continue
            # 处理年龄（大龄, 30岁以上）
            if(j[0] == 1):
                data_list.append(round(random.uniform(j[1][0]+20, j[1][1]), 0))
                continue
            # 处理 #32 => 血清a羟基丁酸脱氢酶 [80, 220]（高于正常值20）
            if(j[0] == 32):
                data_list.append(round(random.uniform(j[1][1], j[1][1])+20, 2))
                continue
            # 处理 #33 => 钾测定 [25, 100]（高于正常值20）
            if(j[0] == 33):
                data_list.append(round(random.uniform(j[1][1], j[1][1])+20, 2))
                continue
            # 处理# 37 => 葡萄糖（高于正常值20）
            if(j[0] == 37):
                data_list.append(round(random.uniform(j[1][1], j[1][1]+20), 2))
                continue
            # 其余医疗指标数据正常
            data_list.append(round(random.uniform(j[1][0], j[1][1]), 2))

        # 加入数据标签
        data_list.append('gaoxueya')
        # 合成完整数据添加
        all_data.append(data_list)

    # CSV 表头
    headers = []
    for i in range(len(all_data[0]) - 1):
        headers.append('A' + str(i))
    headers.append('result')

    # 写入 CSV 文件
    with open('records_gaoxueya.csv','w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(all_data)

if __name__ == '__main__':
    generate_normal()
    generate_gaoxueya()
    print("Generate data successful!")

