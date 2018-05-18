#!/usr/bin/env python
# -*-coding:utf-8-*-
import time


class PolyNode:
    """
    多项式结点
    coef表示参数
    expon表示指数
    """
    def __init__(self,coef, expon):
        self.coef = coef
        self.expon = expon
        self.next = None

class Polynomial:
    def __init__(self):
        self.rear = None

    def attach(self,node):
        if not self.rear:
            self.rear = node
        else:
            link_node = self.rear
            while link_node.next:
                link_node = link_node.next
            link_node.next = node

    def printpoly(self):
        if not self.rear:
            return None
        else:
            node = self.rear
            poly = '{0}x^{1}'.format(node.coef, node.expon)
            while node.next:
                node = node.next
                if not node.expon:
                    poly += '+' + '{0}'.format(node.coef)
                else:
                    poly += '+' + '{0}x^{1}'.format(node.coef, node.expon)
            print(poly)

def add(P1,P2):
    t1 = P1.rear
    t2 = P2.rear
    P = Polynomial()
    while t1 and t2:
        if t1.expon == t2.expon:
            P.attach(PolyNode(t1.coef+t2.coef, t1.expon))
            t1 = t1.next
            t2 = t2.next
        elif t1.expon > t2.expon:
            P.attach(PolyNode(t1.coef, t1.expon))
            t1 = t1.next
        else:
            P.attach(PolyNode(t2.coef, t2.expon))
            t2 = t2.next

    while t1:
        P.attach(PolyNode(t1.coef, t1.expon))
        t1 = t1.next
    while t2:
        P.attach(PolyNode(t2.coef, t2.expon))
        t2 = t2.next

    return P

def multi(P1, P2):
    t1 = P1.rear
    t2 = P2.rear
    P = Polynomial()
    if t1 == None or t2 == None:
        return None
    else:
        while t1:
            t2 = P2.rear
            PP = Polynomial()
            while t2:
                coef = t1.coef * t2.coef
                expon = t1.expon + t2.expon
                PP.attach(PolyNode(coef, expon))
                t2 = t2.next
            P = add(P,PP)
            t1 = t1.next
    return P




def readpoly():
    N = eval(input("输入多项式的项数:"))

    P = Polynomial()
    while N:
        coef, expon = eval(input("依次输入多项式每项的指数和系数:"))
        P.attach(PolyNode(coef, expon))
        N -= 1
    return P

if __name__ == '__main__':

    P1 = readpoly()
    P2 = readpoly()
    PP = multi(P1, P2)
    PP.printpoly()

    #PS = add(P1, P2)
    #P1.printpoly()
    #P2.printpoly()
    #PS.printpoly()
