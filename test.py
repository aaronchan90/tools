import pandas as pd

def analyze_team_stats(df):
    # 按团队分组统计
    team_stats = df.groupby('团队').agg({
        '应用': 'count',  # 统计服务数量
        'GPU卡数': 'sum'  # 统计GPU卡数总和
    }).reset_index()
    
    # 重命名列
    team_stats.columns = ['团队', '服务数量', 'GPU卡总数']
    
    # 打印统计结果
    print("\n各团队统计结果:")
    print(team_stats)
    
    return team_stats

def analyze_business_stats(df):
    # 按业务线分组统计
    business_stats = df.groupby('业务线').agg({
        '应用': 'count',  # 统计服务数量
        'GPU卡数': 'sum'  # 统计GPU卡数总和
    }).reset_index()
    
    # 重命名列
    business_stats.columns = ['业务线', '服务数量', 'GPU卡总数']
    
    # 打印统计结果
    print("\n各业务线统计结果:")
    print(business_stats)
    
    return business_stats

if __name__ == "__main__":
    df = read_excel_file()
    if df is not None:
        analyze_business_stats(df)

# 定义需要的28列名称
columns = ['应用名', '业务线名称', '团队', '应用owner', '卡型号']
EXPECTED_COLUMNS = 28

def read_excel_file():
    # 获取用户输入的Excel文件路径
    file_path = input("请输入Excel文件的路径: ")
    
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path)
        
        # 显示Excel文件的基本信息
        print("\nExcel文件信息:")
        print(f"行数: {len(df)}")
        print(f"列数: {len(df.columns)}")
        print("\n前5行数据:")
        print(df.head())
        
        return df
    
    except FileNotFoundError:
        print("错误：找不到指定的文件")
    except Exception as e:
        print(f"错误：读取文件时发生异常 - {str(e)}")
        
if __name__ == "__main__":
    read_excel_file()
