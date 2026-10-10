# 模式1：写入（覆盖）
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('第一行\n')
    f.write('第二行\n')

# 模式2：追加
with open('output.txt', 'a', encoding='utf-8') as f:
    f.write('追加的内容\n')

# 模式3：使用 print() 函数
with open('output.txt', 'w', encoding='utf-8') as f:
    print('第一行', file=f)
    print('第二行', file=f)

#最终版覆盖
lines = ['第一行\n', '第二行\n', '第三行\n']
with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

#迭代读取
with open('output.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip('\n'))