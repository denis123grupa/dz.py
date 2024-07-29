age = int(input())

a_1 = age // 10000
a_2 = age // 1000 % 10
a_3 = age // 100 % 10
a_4 = age // 10 % 10
a_5 = age % 10

a = a_5 * 10000 + a_4 * 1000 + a_3 * 100 + a_2 * 10 + a_1

print(a)
