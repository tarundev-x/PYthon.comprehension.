#list com5prehension
#l1=[]
#for i in range(11):
   # if i%2==0:
     #  l1.append(i)
#print(l1)
#[0, 2, 4, 6, 8, 10]


#res_list=[ i for i in range(1,11)]
#res_list=[ i for i in range(1,11) if i%2==0]
#5print(res_list)

res_list=[ i for i in range(1,11) if i%2==0]
print(res_list)

#Comprehension-List,Set,Dictionary,Generic
'''
Create an empty list and add even numbers in that list.
The range of evennumbers is 1 to 10
'''
#without ListComprehension
L1_even=[]
for i in range(1,11):
#even number verification
if i%2==0:
#Add number to even list
L1_even.append(i)



# print the list
print"Even List"
print L1_even #[2, 4, 6, 8, 10]



#Creating list with first 10 natural numbers using ListComprehension
res_list=[i for i in range(1,11)]
print "List Comprehension" #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print res_list



#Create a list with even numbers and range is 1 to 10
#List Comprehension-[expression for if]



res_evenlist=[i for i in range(1,11) if i%2==0 ]
print "even_list"
print res_evenlist









#1 2 6 8 10 12 14 16 18 20







''' first i value is fetched and then check the condition
if the condition is true then i is returned to expression
otherwise simple ignore i and next i value is fetched
from the for loop'''









'''
List Comprehension
Creating a new list from the existing list or from the
iterable objects using single step-ListComprehension



Syntax:List Comprehension
[expression/outputvariable for in iterableobject filter/ifcondition]
'''
