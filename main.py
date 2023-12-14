a = [1,3,4,5]

try:
    b = a[6]
    print(b)
except IndexError:
    print('Ви звертаєтесь до неіснуючого індексу')

