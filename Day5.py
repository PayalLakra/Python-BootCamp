'''
Topics to be Covered:
- For loops
- Inbuilt functions - sum,max
- Password Generator
-
-
'''
#Loops - to repeat a process untill a certain condiiton is not met.
#Loops - allows us to execute multiple times the same code.
fruits = ["APPLE","MANGO","PEAR","PAPAYA","BANANA"] 
for i in fruits:
    print(i)

student_score = [12,43,53,21,45,78,43,78,43,89,34,67,89,54,25,25,78] 
total = sum(student_score)     # an inbuilt function to perform summation
print(total)

#sum function
sum =0
for score in student_score:
    sum += score
print(sum)    #this is how the sum function is created but as it is inbuilt we can use it anytime with just one keyword sum.

max = 0
for score in student_score:
    if score > max:
        max = score     # Note that only 1 = is used here
print(max)