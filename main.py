# Activity 1
# num= int(input("Enter a number:"))
# result=0
# temp=num
# while temp !=0:
#     digit=temp%10
#     result=result+digit**3
#     temp=temp//10

# print(result)

# if num==result:
#     print(num,"is an amstrong number")
# else:
#     print(num,"is not an amstrong number")
# Activity 2
def prinfactor(no):
    for i in range(1,no+1):
        if no%i==0:
            print(i)

no= int(input("Enter a number:"))
prinfactor(no)