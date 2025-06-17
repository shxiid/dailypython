#example 1 
x =  "git"
def gitfunc():
  print("my name is "+ x)
gitfunc()

#example 2
x =  "git"
def gitfunc():
  x = "hub"
  print("my name is "+ x)
gitfunc()
print("my name is "+ x)

#without global keyword 
x = 10 
def change():
    x = 5 
change()
print(x)

#with global keyword 
x = 10 
def change():
    global x
    x = 5 
change()
print(x)


