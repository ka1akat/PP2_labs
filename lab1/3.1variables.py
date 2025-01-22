#global variables
a = "awesome"

def kfunc():
  global a
  a = "fantastic"

kfunc()

print("Kbtu is " + a)