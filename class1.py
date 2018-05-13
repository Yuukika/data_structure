#!/usr/bin/env python
# -*-coding:utf-8-*-
import time

## 例2：定义一个函数，传入一个正整数为N的参数后，按顺序打印1到N

def printN(n):
    """
        循环的方法
    """
    for i in range(1,n+1):
        print('{0}\n'.format(i))

def printN2(n):
    """
        递归的方法
    """
    if n:
        printN2(n-1)
        print('{0}\n'.format(n))
    return

## 写程序计算给定多项式在给定点x处的值
def poly(n, a, x):
    """
        循环的方法
    """
    sum = 0
    for i in range(n+1):
        sum += a[i] * x ** i
    return sum

def poly2(n,a,x):
    """
        递归的方法
    """
    sum = 0
    for i in range(n,-1,-1):
        sum = a[i] + x * sum
    return sum
## 给定一个序列，求最大子列和
def MaxSubseqSum1(a):
    max_sum = 0
    n = len(a)
    for i in range(n):
        for j in range(i,n):
            sub_sum = 0
            for k in range(i,j+1):
                sub_sum += a[k]
            if sub_sum > max_sum:
                max_sum = sub_sum
    return max_sum

def MaxSubseqSum2(a):
    max_sum = 0
    n = len(a)
    for i in range(n):
        sub_sum = 0
        for j in range(i,n):
            sub_sum += a[j]
            if sub_sum > max_sum:
                max_sum = sub_sum
    return max_sum

def DivideAndConquer(a, left, right):
    if left == right:
        if a[left] > 0:
            return a[left]
        else:
            return 0
    center = (left + right) // 2
    MaxLeftSum = DivideAndConquer(a,left,center)
    MaxRightSum = DivideAndConquer(a,center+1, right)

    MaxLeftBorderSum = 0
    LeftBorderSum = 0
    for i in range(center,left-1,-1):
        LeftBorderSum += a[i]
        if LeftBorderSum > MaxLeftBorderSum:
            MaxLeftBorderSum = LeftBorderSum
    MaxRightBorderSum = 0
    RightBorderSum = 0
    for i in range(center+1, right+1):
        RightBorderSum += a[i]
        if RightBorderSum > MaxRightBorderSum:
            MaxRightBorderSum = RightBorderSum
    return max(MaxLeftSum, MaxRightSum, MaxLeftBorderSum+MaxRightBorderSum)

def MaxSubseqSum3(a):
    n = len(a)
    return DivideAndConquer(a,0,n-1)

def MaxSubseqSum4(a):
    n = len(a)
    sub_sum = max_sum = 0
    for i in range(n):
        sub_sum += a[i]
        if sub_sum > max_sum:
            max_sum = sub_sum
        elif sub_sum < 0:
            sub_sum = 0
    return max_sum


if __name__ == '__main__':
    #printN(10)
    #printN2(994)
    #print ('x为2时,1+2x+3x^2+4x^3的结果是:{0}'.format(poly(3,[1,2,3,4],2)))
    #print('_________________________________')
    #print ('x为2时,1+2x+3x^2+4x^3的结果是:{0}'.format(poly2(3,[1,2,3,4],2)))
#    start = time.time()
#    for i in range(100):
#        poly(3,[1,2,3,4],2)
#    end = time.time()
#   print('poly的运行时间为{0}s'.format(end-start))
#    start = time.time()
#    for i in range(100):
#        poly2(3,[1,2,3,4],2)
#    end = time.time()
#    print('poly2的运行时间为{0}s'.format(end-start))

    print(MaxSubseqSum1([1,2,3,-1,10,-6]))
    print(MaxSubseqSum2([1,2,3,-1,10,-6]))
    print(MaxSubseqSum3([1,2,3,-1,10,-6]))
    print(MaxSubseqSum4([1,2,3,-1,10,-6]))