from Rectangle import Rectangle
from Surface import Surface
# When we run the program and just consider one value of the rest rectangle values, we are going to see that each one work perfectly inside the main function.
def main():
  r = Rectangle(10, 10, 10, 10)
  assert((r.x, r.y, r.height, r.width) == (10,10,10,10))
  r = Rectangle(-1, 1, 1, 1)
  assert((r.x, r.y, r.height, r.width) == (0,1,1,1))
  r = Rectangle(1, -1, 1, 1)
  assert((r.x, r.y, r.height, r.width) == (1,0,1,1))
  r = Rectangle(1, 1, -1, 1)
  assert((r.x, r.y, r.height, r.width) == (1,1,0,1))
  r = Rectangle(1, 1, 1, -1)
  assert((r.x, r.y, r.height, r.width) == (1,1,1,0))
  print(r)
  
  s = Surface("myimage.png", 10, 10, 10, 10)
  assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))
  srect = s.getRect()
  assert(srect.x,  s.getRect().y, srect.height,  srect.width) == (10,10,10,10)
  assert(s.image)
  print(srect)
  print("Test Complete!")




main()