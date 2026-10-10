"""
逆向思维
第n个要移到target上，则前n-1个需要移到assistant
接下来考虑前n-1个
第n-1个要移到assistant上，则前n-2个需要移到target
以此类推
直到第n个移到target上，其余全在assistant上
接下来借助start将前n-1个移到target上
"""
def hannuota(num,start,assistant,target):
    if num == 1:
        print(f"{start} --> {target}")
        return
    hannuota(num-1,start,target,assistant) #对应前n-1个整体，递归自动拆解
    print(f"{start} --> {target}") #对应第n个
    hannuota(num-1,assistant,start,target) #将assistant上的借助start移到target

hannuota(5,'A','B','C')