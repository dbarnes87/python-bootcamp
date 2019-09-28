# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '02-Python Statements'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Statements Assessment Test
# Let's test your knowledge!
#%% [markdown]
# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

#%%
st = 'Print only the words that start with s in this sentence'
newlist = st.split()
for item in newlist:
    if item[0] == 's':
        print(item)

#%%
#Code here

#%% [markdown]
# ______
# **Use range() to print all the even numbers from 0 to 10.**

mylist = range(0,11,2)
for num in mylist:
    print(num)

#%% [markdown]
# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

#%%
#Code in this cell
mylist = [x for x in range(1,51) if x%3 == 0]
mylist

#%% [markdown]
# _____
# **Go through the string below and if the length of a word is even print "even!"**

#%%
st = 'Print every word in this sentence that has an even number of letters'


#%%
mylist = st.split()
for word in mylist:
    if len(word) % 2 == 0:
        print(word)
#%% [markdown]
# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

#%%
fblist = range(1,100)
for num in fblist:
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)
#%% [markdown]
# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

#%%
st = 'Create a list of the first letters of every word in this string'


#%%
newlist = [x[0] for x in st.split()]
newlist

#%% [markdown]
# ### Great Job!

