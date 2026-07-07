# OPTION ONE
# age = int(input("enter your age  :"))
# def is_adult(age):
#     if age>18:
#         return True
#     else:
#         return False

# OPTION TWO
age = int(input("enter your age  :"))
def is_adult(age):
    return True if age >18 else False
    
result = is_adult(age)
print(result)