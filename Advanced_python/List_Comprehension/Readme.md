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

-----------------------------------
<b>11. Write a program to create a new list containing positive integers from the original list</b><br>
#### - Input:
num_list = [-30,-20,-10,0,5,10,15,20]<br>
positive_numbers = [num for num in num_list if num > 0]<br>
print(positive_numbers)<br>
#### - Output:
[5, 10, 15, 20]

-----------------------------------
<b>12. Write a program to find the common elements from the two lists.</b><br>
#### - Input:
a = [1,2,3,4,5]<br>
b = [4,5,6,7,8]<br>
common_elements = [num for num in a if num in b]<br>
print(common_elements)<br>
#### - Output:
[4, 5]

-----------------------------------
<b>13. Write a program to find the list of all the numbers from 1 to 100 that are divisible by both 3 and 5.</b><br>
#### - Input:
divisible_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]<br>
print(divisible_by_3_and_5)<br>
#### - Output:
[15, 30, 45, 60, 75, 90]

-----------------------------------
<b>14. Write a program to convert the given string into upper case</b><br>
#### - Input:
str = [‘data engineer’,’data scientist’,’data analyst’,’machine learning engineer’, ‘dba’, ‘cloud engineer’, ‘devops engineer’, ‘cyberark analyst’]<br>
data_jobs = [x.upper() for x in str if x.startswith(‘d’)]<br>
print(data_jobs)<br>
#### - Output:
['DATA ENGINEER', 'DATA SCIENTIST', 'DATA ANALYST', 'DBA', 'DEVOPS ENGINEER']

-----------------------------------
<b>15. Write a program to convert the given string into upper case and starts with d and ends with t</b><br>
#### - Input:
str = [‘data engineer’,’data scientist’,’data analyst’,’machine learning engineer’, ‘dba’, ‘cloud engineer’, ‘devops engineer’, ‘cyberark analyst’]<br>
data_jobs = [x.upper() for x in str if x.startswith("d") and x.endswith("t")]<br>
print(data_jobs)<br>
#### - Output:
['DATA SCIENTIST', 'DATA ANALYST']

-----------------------------------
<b>16. Write a program to create a list of the first letters of each word in a given list of words.</b><br>
#### - Input:
words = ['apple', 'banana', 'cherry', 'date']<br>
first_letters = [word[0] for word in words]<br>
print(first_letters)<br>
#### - Output:
['a', 'b', 'c', 'd']

-----------------------------------
<b>17. From the Given list of tuples representing (name, age), write a list comprehension to create a list of names where age is not None.</b><br>
#### - Input:
people = [('Alice', 17), ('Bob', None), ('Charlie', 20), ('David', None)]<br>
names_with_age = [name for name, age in people if age is not None]<br>
print(names_with_age)<br>
#### - Output:
['Alice', 'Charlie']

-----------------------------------
<b>18. Write a list comprehension to create a list of the lengths of each word in a given sentence.</b><br>
#### - Input:
string = "Data Engineering"<br>
print([len(word) for word in string.split()])<br>
#### - Output:
[4, 11]

-----------------------------------
<b>19. Converting user input strings to uppercase.</b><br>
#### - Input:
user_input = input("enter a list of strings separated by spaces:")<br>
strings=[s.upper() for s in user_input.split()]<br>
print(strings)<br>
#### - Output:
enter a list of strings separated by spaces:python for data engineering<br>
['PYTHON', 'FOR', 'DATA', 'ENGINEERING']

-----------------------------------
<b>19. Converting user input strings to title case(first letter uppercase).</b><br>
#### - Input:
user_input = input("enter a list of strings separated by spaces:")<br>
strings=[s.upper() for s in user_input.split()]<br>
print(strings)<br>
#### - Output:
enter a list of strings separated by spaces:welcome to Python prgramming<br>
['Python', 'For', 'Data', 'Engineering']

-----------------------------------
