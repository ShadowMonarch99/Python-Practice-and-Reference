I found two approaches to this problem.

#1 This is the easy and self explanatory approach
-------------------------------------------------------------------------------------------------------------------------------------------------------
x=int(input())
str=set()
for i in range(x):
    str.add(input())
print(len(str))
-------------------------------------------------------------------------------------------------------------------------------------------------------

#2 This approach makes the above code compact. At first glance it may seem confusing but when you start comparing with #1 its almost identical. We have just omitted the add function 
as well
-------------------------------------------------------------------------------------------------------------------------------------------------------
print(len(set([str(input()) for x in range(int(input()))])))
-------------------------------------------------------------------------------------------------------------------------------------------------------



