#String concatenation
"""
a="Dishan"+" Darshan"
print(a)
name=input("name:")
length=len(name)
print(length)
"""
"""
str1=input("ENTRE STRING 1:")
str2=input("Enter string 2:")
concatenate=str1+str2
print(concatenate *5)
"""
def star(i):
    for i in range(1,6):
        print(" "*(5-i)+"*"*(2*i-1))
print(star(6))