def func(*args,**kwargs):
    print("元组信息如下：")
    for arg in args:
        print(arg)
    print("字典信息如下：")
    for k,v in kwargs.items():
        print(f"{k}:{v}")

func(1,2,3,4,name = "llx")
print("********")
#打包为元组和字典
tuple_data = (1,2,3,4,5)
dict_data = {'name':'llx'}
func(tuple_data,dict_data)
print("********")
#传入时拆包
func(*tuple_data,**dict_data)