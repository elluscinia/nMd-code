# -*- coding: utf-8 -*-
import math
def C(n, k):
    return (math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

def Plotkin_bound(n, d):
    return ((2*d)/(2*d-n))

def Hamming_bound(n, d):
    t = (d-1)/2
    summ = 0
    for i in xrange(0, t+1):
        summ += C(n, i)
    return ((2**n)/summ)

def Gilbert_Varshamov_bound(n, d):
    t = (d-1)/2
    summ = 0
    for i in xrange(0, (2*t)+1):
        summ += C(n, i)
    return ((2**n)/summ)

def Singleton_bound(n, d):
    return (2**(n-d+1))
if __name__ == '__main__':
    n = int(raw_input('Введите параметр n: '))
    d = int(raw_input('Введите параметр d: '))
    M = raw_input('Введите параметр M: ')
    if M == '':
        print 'Отсутствует параметр M (мощность кода)'
        print 'M = A(n, d), наименьшая верхняя оценка'
    else:
        print 'A(n, d) =', int(M)
    if 2*d > n:
        print 'условие 2d > n выполняется => проверим по т. Плоткина'
        print 'A(n, d) <=', Plotkin_bound(n, d)
    print 'теорема Хэмминга'
    print 'A(n, 2t+1) <=', Hamming_bound(n, d)
    print 'теорема Варшамова-Гилберта'
    print 'A(n, 2t+1) >=', Gilbert_Varshamov_bound(n, d)
    print 'теорема Джоши (граница Синглтона)'
    print 'A(n, d) <=', Singleton_bound(n, d)