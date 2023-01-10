# local-python-setup

I'm not sure if I was able to add the python code correctly so I'm adding it here. 


def hello(name):
    print("Hello " + name)

hello("user")


def pack(x, y, z):
    return (x,y,z)

print(pack("a", "b", "c"))


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
eat_lunch(food_list=["gummy bears", "cereal", "sushi", "protein shake"])
