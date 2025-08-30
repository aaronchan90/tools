import pandas as pd

def process_excel():
    # 读取Excel文件
    df = pd.read_excel("resource.xlsx")
    
    # 从应用名中提取服务名并写入第二列
    df.iloc[:, 1] = df.iloc[:, 0].str.split('-').str[0]

    # 将H20_141G替换为H20
    df.iloc[:, 3] = df.iloc[:, 3].replace('H20_141G', 'H20')
    
    # 按服务名和GPU型号排序
    df = df.sort_values(by=[df.columns[1], df.columns[3]])
    
    # 初始化汇总卡数和汇总标签列
    df.iloc[:, 5] = 0  # 汇总卡数
    df.iloc[:, 6] = 0  # 汇总标签
    
    # 对相同服务名和GPU型号的组进行处理
    current_service = ""
    current_gpu = ""
    sum_cards = 0
    start_idx = 0
    
    for i in range(len(df)):
        service = df.iloc[i, 1]
        gpu = df.iloc[i, 3]
        cards = df.iloc[i, 4]
        
        # 如果是新的组
        if service != current_service or gpu != current_gpu:
            # 为上一组的第一行写入汇总数据
            if i > 0 and sum_cards > 0:
                df.iloc[start_idx, 5] = sum_cards  # 写入汇总卡数
                df.iloc[start_idx, 6] = 1  # 写入汇总标签
            
            # 重置计数器
            current_service = service
            current_gpu = gpu
            sum_cards = cards
            start_idx = i
        else:
            # 累加卡数
            sum_cards += cards
    
    # 处理最后一组
    if sum_cards > 0:
        df.iloc[start_idx, 5] = sum_cards
        df.iloc[start_idx, 6] = 1
    
    # 保存处理后的文件
    df.to_excel("resource_processed.xlsx", index=False)

if __name__ == "__main__":
    process_excel()
