# 模式匹配
person1 = ('James', 23, 'male')
person2 = ('Lili', 33, 'female')
person3 = ('Mary', 34, 'female')


def func(person):
    match person:
        case (name, _, 'female'):
            print(f'{name} is woman')
        case (name, _, 'male'):
            print(f'{name} is man')
        case (name, age, gender):
            print(f'{name} is {age} old')


'''
James is man
Lili is woman
Mary is woman
'''
func(person1)
func(person2)
func(person3)
