import os
from pathlib import Path
from datetime import datetime

def find_latest_file(directory):
    latest_file = None
    latest_time = None
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            # 排除刚创建的查找脚本
            if filepath.endswith('find_latest.py') or filepath.endswith('find_latest.ps1'):
                continue
            try:
                mtime = os.path.getmtime(filepath)
                if latest_time is None or mtime > latest_time:
                    latest_time = mtime
                    latest_file = filepath
            except:
                pass
    
    return latest_file, latest_time

if __name__ == "__main__":
    directory = r"f:\BNCFT"
    latest_file, latest_time = find_latest_file(directory)
    
    if latest_file:
        print(f"文件路径: {latest_file}")
        print(f"最后修改时间: {datetime.fromtimestamp(latest_time).strftime('%Y/%m/%d %H:%M:%S')}")
    else:
        print("未找到文件")
