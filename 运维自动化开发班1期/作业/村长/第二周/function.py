### 1.
def my_lst(xx):
    my_lst_test = set(lst)
    my_lst_test_test = tuple(my_lst_test)
    return my_lst_test_test

lst = [1, 1, 2, 3, 4, 4, -1, -1]
xxx = my_lst(lst)
yyy = list(xxx)
print(yyy)


### 2.
def my_num(*ret):
    count = {}
    for i in ret:
        count[i]= ret.count(i)
    return count

rest1  = my_num('ab', 'ab', 'c' ,'cccc', 'ccc' ,'cccc')
print(rest1)

### 3.
source = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}
target = {}

def flatmap(srcDic, targetKey=''):
    for k, v in srcDic.items():
        if isinstance(v, dict):
            flatmap(v, targetKey=targetKey + k + '.')
        else:
            target[targetKey + k] = v

flatmap(source)
print(target)
