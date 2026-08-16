#Method loop

def reverse_string(s):
    rev_string = ""
    for char in s:
        rev_string = char + rev_string
    return rev_string

print(reverse_string("hello"))

#Method Recursive
def re_s(ss):
    if ss == "":
        return ''
    return  re_s(ss[1:]) + ss[0]

print(re_s("hello"))

