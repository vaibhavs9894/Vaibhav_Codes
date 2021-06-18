# *variablename -> variable number of arguments (*args)

def mean(*numbers):
    if numbers:
        print("mean=>",sum(numbers)/len(numbers))

mean()
mean(1)
mean(12,3,312,321)
mean(12,3,3,1,2,3,2,1,1,2,3,12,312,3,123,12,31,23,12,31,23,12,312,3,123,123,1)

def agg(*numbers, operation = 'sum'):
    if numbers:
        if operation == 'sum':
            print('total',sum(numbers))
        elif operation =='mean':
            print('mean',sum(numbers)/len(numbers))
        elif operation =='max':
            print('max',max(numbers))


agg(12,34,56,78,89,123,345)
agg(12,3,12,2,operation='mean')
agg(12,3,43,56,67,8,989,89,8,98,98,98,98,9,8,98,3,3,34,3,2,1,12,operation='max')
agg(12,3,43,56,67,8,989,89,8,98,98,98,98,9,8,98,3,3,34,3,2,1,12,operation='sum')

print('hello','world','is','there','any','food',sep='---')

# **variablename -> variable number of keyword arguments (**kwargs)

def settings(**info):
    for k,v in info.items():
        print(k, v)


settings(color='red',x=28,y=39,size=(100,100))

settings(font='calibri',fontsize=20,rotation=100)