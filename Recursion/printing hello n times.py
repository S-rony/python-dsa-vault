#printing hello n times

def printing(number):
    if number == 1:
        print("Hello")
        return
    printing(number - 1)
    print("Hello")



printing(5)