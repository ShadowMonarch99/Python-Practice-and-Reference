from collections import deque
n=int(input())
d=deque()
for _ in range(n):
    command,*num=input().split() #here we split the input string into the command and number depending on the white space. Append 2, becomes command=Append and *num=2
    # we used *num instead of num because using an * we set the number of arguments to be taken in a function to be indefinite, ie making it versatile for unknown arguments
    getattr(d, command)(*num)#getattr unpacks the attribute that is in command, ie Append and applies it to d, with num being the argument
print(' '.join(d))    
#print all the numbers in the deque joined by a white space in between
