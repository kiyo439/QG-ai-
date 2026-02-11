# 基于 “封装 + 继承 + 多态” 设计「图形计算器」：
# 定义基类 Shape （私有属性 area ，封装计算面积的私有方法 calc_area ）
# 子类 Circle / Rectangle 继承 Shape ，重写面积计算逻辑（多态体现）
# 类变量记录所有图形的创建数量，实例变量存储各自尺寸
# 要求：通过实例调用公开方法获取面积，禁止直接访问私有属性

import math
class Shape:
    count = 0
    def __init__(self):
        self.__area= None
        Shape.count+=1

    def _calc_area(self):
        raise NotImplementedError("子类必须重写父类面积计算方法!")

    @property
    def area(self):
        self._calc_area()
        return self.__area

    @area.setter
    def area(self,area):
        self.__area = area

class Rectangle(Shape):
    def __init__(self,width,long):
        super().__init__()
        self.width = width
        self.long = long

    def _calc_area(self):
        self.area = self.width * self.long

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def _calc_area(self):
        self.area = math.pi*self.radius**2

if __name__ == '__main__':
    circle1 = Circle(5)
    circle2 = Circle(10)
    rectangle1 = Rectangle(5,5)
    rectangle2 = Rectangle(5,10)
    print(f"以5为半径的圆的面积是{circle1.area:.2f}")
    print(f"以10为半径的圆的面积是{circle2.area:.2f}")
    print(f"宽为5，长为5的矩形的面积是{rectangle1.area:.2f}")
    print(f"宽为5，长为10的矩形的面积是{rectangle2.area:.2f}")
    print(f"所有图形的创建数量是{Shape.count}")