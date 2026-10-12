import csv
import json

def read_data_csv(filename):
    data = []
    try:
        with open(filename,"r",encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({
                    'name' : row["name"],
                    'age' : int(row["age"]),
                    'birthday' : row["birthday"]
                })
        return data
    except Exception as e:
        print(f"文件信息读取错误，error is {e}")
        return []

def calculate_average(data):
    if not data:
        return 0
    total = sum(s['age'] for s in data) #推导式
    return total / len(data)

def find_top_age(data):
    if not data:
        return None
    return max(data, key=lambda s: s['age'])

def save_report(filename, data):
    try:
        report = {
            'total_students': len(data),
            'average_age': calculate_average(data),
            'top_age': find_top_age(data),
            'data': data
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"报告已保存到 '{filename}'")
    except Exception as e:
        print(f"错误：保存报告失败 - {e}")

if __name__ == '__main__':
    data = read_data_csv('../data.csv')
    print(data)
