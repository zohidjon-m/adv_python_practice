# a = 10
# def fun1():
#     print()
# print(dir()) #attributes of current module
# print(__name__) #name of current module
print("The script1 __name__ is:", __name__)

def Ourfavoritefood(food):
    print(f"Our favorite food is {food}")
def main():
    print("This is script1.py")
    Ourfavoritefood("Pizza")

if __name__ == "__main__":
     main()
#  from script2 import *
# print(__name__)