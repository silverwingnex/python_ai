from info_utils import *

def main():
    data = read_data_csv('data.csv')

    if not data:
        print("没有学生数据")
        return

    print(f"总人数：{len(data)}")
    print(f"平均年龄：{calculate_average(data):.2f}")

    top = find_top_age(data)
    if top:
        print(f"最高成绩：{top['name']} - {top['age']}")

    save_report('report.json', data)

if __name__ == '__main__':
    main()