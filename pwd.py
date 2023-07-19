#Password Generator Project
import random #import the random module

#Define letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= 10 #You can change the number of letters you want
nr_symbols = 3 #You can change the number of symbols you want
nr_numbers = 3 #You can change the number of numbers you want

length = nr_letters + nr_symbols + nr_numbers #compute the full length of the password
values = [letters, numbers, symbols] #Put all possible characters in a single array
pwd = "" #Iteratively add characters to this variable pwd

for n in range(0, length):
  row = random.randint(0, len(values) - 1) #random integer to specify the chosen array in this iteration (numbers, letters or symbols)
  col = random.randint(0, len(values[row]) - 1) #random integer to choose a character in the chosen array

  pwd += values[row][col] #Add the chosen character to pwd

  #Then, deduct 1 from the number of remaining possible choices from an array (By default, letters can be chosen 10 times, symbols and numbers 3 times)
  #If the nr_(...)  becomes 0(zero) remove it from values
  if row == 0:
    nr_letters -= 1
    if nr_letters == 0:
      values.remove(letters)
  elif row == 1:
    nr_numbers -= 1
    if nr_numbers == 0:
      values.remove(numbers)
  else:
    nr_symbols -= 1
    if nr_symbols == 0:
      values.remove(symbols)

print(pwd) #Print the generated password to the console

#The end...

