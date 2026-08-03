#task 1
#problem 1
sum=0
for i in range(1,11):
    sum+=i
print ("sum is ",sum )
#-------------------------------------------------------------------------------------------------------------------------
#problem 2
for i in range(1,51):
    if( i % 5!=0):
        print ("Number: ",i)
#-------------------------------------------------------------------------------------------------------------------------
#problem 3
arr={}
print("enter the 5 numbers")
for i in range(0,5):
     x=int(input("enter the number "))
     

     if x==0:
        print("the number is zero")
     elif x >0:
        print("the number is positive")
     else :
        print("the number is negative") 
        #-------------------------------------------------------------------------------------------------------------------------
#task2
# problem 1
word=input("enter the word :")
print(word)
#-------------------------------------------------------------------------------------------------------------------------
#problem 2
numbers=[]
for i in range(1,4):
    x= int(input("enter the number: "))
    numbers.append(x)

maxvalue=max(numbers)
print ("the max is ",maxvalue)  
#-------------------------------------------------------------------------------------------------------------------------
#problem 3
import numpy as np

scores=[]
   
for i in range(1,11):
    x=int(input("enter the score: "))
    scores.append(x)
arr=np.array(scores)
sum=0
for i in arr:
    sum+=i
print("the average is :",float(sum)/10 )        
arr.sort()

print("the lowest score is :",arr[0])
print("the highest score is :",arr[-1])
arr2=np.array(arr)
for i in range(0,10):
    arr2[i]+=5
print(arr2) 
#-------------------------------------------------------------------------------------------------------------------------
#task 3
# problem 1
def leapyear(year):
    if year%4==0 and(year%100!=0 or year%4==0):
        ans=True
    else:
        ans=False 
    print("the answer is",ans)             

leapyear(2024)  
#task 4(bouns)
#problrem 1
counter=0
sentence=input("enter the sentence ")
n=len(sentence)
for i in range(0,n-1):
    if i==0 or sentence[i-1] ==" " :
        if sentence[i]=='a'  or sentence[i]=='u' or sentence[i]=='o' or sentence[i]=='i' or sentence[i]=='e' or sentence[i]=='A' or sentence[i]=='U' or sentence[i]=='O'or sentence[i]=='I'or sentence[i]=='E':
            counter+=1
  

print ("words start with vowels are:",counter)
#-------------------------------------------------------------------------------------------------------------------------
#problem 2
def prime(number):
    ans=True
    for i in range(2,number-1):
        if(number%i==0):
           ans=False
           break
    if ans==False :
        print("the number  is not prime")
    else:
        print("the number is prime")
prime(10)  
#-------------------------------------------------------------------------------------------------------------------------
#problem 3
def maximum(number):
    max=number[0]
    for i in number:
       if(max<i):
          max=i    
    print ("the max in list is :",max)
numbers=[]
n=int(input("enter the number of list "))
for i in range(0,n):
    numbers.append(int(input("enter the number")))
maximum(numbers)    



