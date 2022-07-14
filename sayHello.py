# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/14 14:49
# @Software: PyCharm
class SayHello():

    def __init__(self, name="World"):
        self.name = name

    def sayHello(self):
        print("hello" +" " + self.name + "!")

if __name__ == '__main__':
    person = SayHello()
    person.sayHello()