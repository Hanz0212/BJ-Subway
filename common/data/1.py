import pandas as pd  
import json  

# 读取 CSV 文件  
in_15min_df = pd.read_csv('D:\\a_tree\VUE\BJ-Subway\common\data\in_15min.csv', header=None)  
out_15min_df = pd.read_csv('D:\\a_tree\VUE\BJ-Subway\common\data\out_15min.csv', header=None)  

# 初始化结果列表  
result1 = []  
result2 = []  

# 遍历行，构建 JSON 格式  
for index in range(len(in_15min_df)):  
    result1.append(in_15min_df.iloc[index].tolist())  
    result2.append(out_15min_df.iloc[index].tolist())  
    # result1.append(in_15min_df.iloc[index].tolist()[:192])  
    # result2.append(out_15min_df.iloc[index].tolist()[:192])  

# 将 result1 和 result2 转换为 DataFrame
df_result1 = pd.DataFrame(result1)
df_result2 = pd.DataFrame(result2)

# 转置 DataFrame
df_result1_transposed = df_result1.transpose()
df_result2_transposed = df_result2.transpose()

# 将转置的 DataFrame 转换回列表
result1 = df_result1_transposed.values.tolist()
result2= df_result2_transposed.values.tolist()


# 将结果转换为 JSON 格式  
json_output1 = json.dumps(result1, indent=4)  
json_output2 = json.dumps(result2, indent=4)  


# print(max(max(result1, key=lambda x: max(x))))
# print(max(max(result2, key=lambda x: max(x))))

# 可选：将 JSON 写入文件  
with open('common\data\\beijing-subway-inflows.json', 'w') as json_file:  
    json_file.write(json_output1)
with open('common\data\\beijing-subway-outflows.json', 'w') as json_file:  
    json_file.write(json_output2)