import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width=0, height=0, corner=None):
        self.width = width
        self.height = height
        self.corner = corner

class Circle:
    def __init__(self, center, radius):
        self.center = center  
        self.radius = radius

center_point = Point(150, 100)
my_circle = Circle(center_point, 75)

def point_in_circle(circle, point):
    distance = math.sqrt((point.x - circle.center.x)**2 + 
                         (point.y - circle.center.y)**2)
    return distance <= circle.radius

def rect_in_circle(circle, rect):
    p1 = rect.corner 
    p2 = Point(p1.x + rect.width, p1.y) 
    p3 = Point(p1.x, p1.y + rect.height) 
    p4 = Point(p1.x + rect.width, p1.y + rect.height) 
    
    return (point_in_circle(circle, p1) and 
            point_in_circle(circle, p2) and 
            point_in_circle(circle, p3) and 
            point_in_circle(circle, p4))

def rect_circle_overlap(circle, rect):
    p1 = rect.corner
    p2 = Point(p1.x + rect.width, p1.y)
    p3 = Point(p1.x, p1.y + rect.height)
    p4 = Point(p1.x + rect.width, p1.y + rect.height)
    
    if (point_in_circle(circle, p1) or 
        point_in_circle(circle, p2) or 
        point_in_circle(circle, p3) or 
        point_in_circle(circle, p4)):
        return True
    
    return False

#Kiểm tra thử
print(f"Kiểm tra điểm (160, 110): {point_in_circle(my_circle, Point(160, 110))}")

box = Rectangle(50, 50, Point(140, 90))
print(f"Hình chữ nhật nằm trọn trong vòng tròn? {rect_in_circle(my_circle, box)}")