# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.

def hello(name):
    print("Hello " + name)

hello("user")

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.

def pack(x, y, z):
    return (x,y,z)

print(pack("a", "b", "c"))




# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.

def eat_lunch(food_list):
  if len(food_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(food_list)):
      if i == 0:
        print(f"First I eat {food_list[0]}")
      else:
        print(f"Next I eat {food_list[i]}")

eat_lunch(food_list= [])
eat_lunch(food_list=["gummy bears"])
eat_lunch(food_list=["gummy bears", "cereal", "sushi"])