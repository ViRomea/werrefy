from math import * 
class Triangle:
  def __init__(self, a, b, /, c: int =0, alpha: int =0): 
    self.a = a 
    self.b = b 
    self.c = c
    del a
    del b 
    del c 
    if self.c == 0:
      self.c = round(sqrt(self.a**2 + self.b**2))
  def S(self,):
    PHalf = (self.a + self.b +  self.c) / 2 
    x = PHalf * (PHalf - self.a) * (PHalf - self.b) * (PHalf - self.c)
    del PHalf
    self.S = sqrt(x)
    return self.S
    
   
ABC = Triangle(5,8) 
print(ABC.c) 
print(ABC.S())


  