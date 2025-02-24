#### Filter Function

- The filter function is a built-in python function that processes an iterable based on a specified condition, returning a new iterable that includes only the elements for which the condtion is true. <br>
- The filter function in python works with iterables like string, list, tuple, set, dictionaries and so on.<br>
- The syntax of filter function includes two arguments: a function and an iterable. The function takes one argument and returns a boolean value while iterable can be list, set, or any other type that we want to filter.<br>


#### Syntax:
The syntax of filter function is:<br>
filter(function, iterable)

<b>1. Program to print Positive and Negative numbers by applying Filter function(without lambda)</b><br>
#### - Input:<br>
def is_positive(num):<br>
  return num > 0<br>
def is_negative(num):<br>
  return num < 0<br>
numbers = [1, 2, -3, -2, -4, -6, 3, 4]<br>
positive_numbers = list(filter(is_positive, numbers))<br>
negative_numbers = list(filter(is_negative, numbers))<br>
print("Positive numbers is:", positive_numbers)<br>
print("Negative numbers is:", negative_numbers)<br>
#### - Output:<br>
Positive numbers is: [1, 2, 3, 4]<br>
Negative numbers is: [-3, -2, -4, -6]

<b>2. Program to print Positive and Negative numbers by applying Filter function(with lambda)</b><br>
#### - Input:<br>
numbers = [1, 2, -3, -2, -4, -6, 3, 4]<br>
positive_numbers = list(filter(lambda x: x>0, numbers))<br>
negative_numbers = list(filter(lambda x: x<0, numbers))<br>
print("Positive numbers is:", positive_numbers)<br>
print("Negative numbers is:", negative_numbers)<br>
#### - Output:<br>
Positive numbers is : [1, 2, 3, 4]<br>
Negative numbers is: [-3, -2, -4, -6]
