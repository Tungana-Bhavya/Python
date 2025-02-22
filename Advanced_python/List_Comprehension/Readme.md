### List Comprehension


<b>1. Write a list comprehension to generate a list of numbers from 1 to 10 using range function. </b><br>
#### - Input:
n=10<br>
lst = [x for x in range(1,n+1)]<br>
print(lst)<br>
#### - Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br>

-----------------------------------
<b>2. Write a list comprehension to generate a new list from a list of numbers.</b><br>
#### - Input:
old_list = [1,2,3,4,5]<br>
new_list = [x for x in old_list]<br>
print(new_list)<br>
#### - Output:
[1, 2, 3, 4, 5]

-----------------------------------
<b>3. Write a list comprehension to generate the squares of the list using range function</b><br>
#### - Input:
lst = [val ** 2 for val in range(5)]<br>
print(lst)<br>
#### - Output:
[0, 1, 4, 9, 6]

-----------------------------------
<b>4. Generating squares of a list from an existing list</b><br>
#### - Input:
old_list = [1,2,3,4,5]<br>
new_list = [val ** 2 for val in old_list]<br>
print(new_list)<br>
#### - Output:
[1, 4, 9, 16, 25]

-----------------------------------
<b>5. Generating Squares of a list using condtional statement</b><br>
#### - Input:
old_list = []<br>
new_list = [val ** 2 for val in range(50) if val%2==0 and val > 20)<br>
print(new_list)<br>
#### - Output:
[24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

-----------------------------------
<b>6. Generating a list of odd numbers between 20 and 50</b><br>
#### - Input:
lst = []<br>
new_lst=[x for x in range(50) if x%2!=0 and x>20]<br>
print(new_lst)<br>
#### - Output:
[21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

-----------------------------------
<b>7. Write a program to print list of odd numbers from 1 to 10</b><br>
#### - Input:
n = 10<br>
odd_numbers = [x for x in range of n if x%2!=0]<br>
print(“odd numbers is:”,odd_numbers)<br>
#### - Output:
odd numbers is: [1, 3, 5, 7, 9]

-----------------------------------
<b>8. Write a program to convert Nested list into a single list</b><br>
#### - Input:
nested_lst = [[1,2,3],[4,5,6],[7,8,9]]<br>
flattened_lst = [x for sublist in nested_lst for x in sublist]<br>
print(flattened_lst)<br>
#### - Output:
 [1, 2, 3, 4, 5, 6, 7, 8, 9]

-----------------------------------
<b>9. Write a program to convert Nested list containing duplicate values into a single list</b><br>
#### - Input:
nested_list = [[1,2,4],[4,5,6],[7,8,9]] <br>
single_list = [x for j in nested_list for x in j]<br>
print(single_list)<br>
#### - Output:
[1, 2, 4, 4, 5, 6, 7, 8, 9]

-----------------------------------
<b>10. Write a program to flatten a mixed nested list</b><br>
#### - Input:
nested_lst = [[1,2,3],[‘python’],[6,’language’,8]]<br>
single_lst = [x for var in nested_list for x in var]<br>
print(single_lst)<br>
#### - Output:
[1, 2, 3, 'python', 6, 'language', 8]


