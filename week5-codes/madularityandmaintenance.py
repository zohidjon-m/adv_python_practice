#######Ex: Original (no functions):
# print("Happy birthday to you!")
# print("Happy birthday to you!")
# print("Happy birthday, dear Fred")
# print("Happy birthday to you!")
# ######################With functions:###########################
# def happy():
#     print("Happy birthday to you!")
# def singFred():
#     happy()
#     happy()
#     print("Happy birthday, dear Fred")
#     happy()
# singFred()

# #Only two print statements used. If the lyric changes, edit once inside happy()
# ############Extensibility & Readability
def happy():
    print("Happy birthday to you!")
def sing(name):
    happy()
    happy()
    print("Happy birthday, dear " + name)
    happy()
sing("Fred")
sing("Lucy")
#Easier to extend, read, and reuse.