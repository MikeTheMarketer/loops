user_input = int(input("Enter a number: "))
number_counter = 0
calc = 0
for num in range(0,10):
  number_counter += 1
  calc = user_input * number_counter
  print(user_input," X {} = {}".format(number_counter, calc))
print("\n")

list_holder = []
num_holder = 0
for num in range(0,20):
  if (num % 2) == 0:
    num_holder = num ** 2
    list_holder.append(num_holder)
  else:
    num_holder = num ** 3
    list_holder.append(num_holder)
print(list_holder)
print("\n")

user_input_inverter = input("Please enter your word or phrase:")
slice_string = user_input_inverter[::-1]
print(slice_string)
print("\n")

even_list = []
odd_list = []
for num in range(1,201):
  if (num % 2) == 0:
    even_list.append(num)
  else:
    odd_list.append(num)
print(even_list)
print(odd_list)
print("\n")

def count(sequence, item):
  return sequence.count(item)
sequence = [2,3,2,2,2,5,5,5,5,3,2,4,5,2,1,7]
item = 2
print(count(sequence,item))
print("\n")

def digit_sum(n):
  list = [int(x) for x in str(n)]
  counter = 0
  list_sum_new = 0
  for num in list:
    list_sum_new += list[counter]
    counter += 1
  return list_sum_new
    
n = 64566
print(digit_sum(n))
print("\n")

first_number_input = int(input("Enter first number: "))
second_number_input = int(input("Enter second number: "))

def compute(first_number_input, second_number_input):
  
  while(second_number_input):
    first_number_input, second_number_input = second_number_input, first_number_input % second_number_input
    
  return(first_number_input)

print(compute(first_number_input, second_number_input))
print("\n")

for num in range(1,50):
  if (num % 3 == 0) and (num % 5 == 0):
    print("fizzbuzz")
  elif num % 3 == 0:
    print("fizz")
  elif num % 5 == 0:
    print("buzz")
  else:
    print(num)

  

