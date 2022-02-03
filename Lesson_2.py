x = 2
y = x * x
y
# one line to swap x and y
x,y = y, x

# strings can be concatenated together as well

hi = "hello there"
name = "daxiang"
greet = hi + " " + name

# operations on strings
3*"daxinag"

# you can slice a string with a call such as s[i:j], which gives you a portion of string s from index i to index j - 1 (note it is j - 1!!)
s = 'Python is Fun!'
s[1:5]

# test if element is in a string or any collection
"thon" in "Python"
"noh" in "Python"

# if the index is negative, it means the element location when counting backwards, try this:
s = "hello"
s[:-1]
# when the step is negative, it means it is counting backwards
s[::-1]

# input and output
x = 1
print(x)
x_str = str(x)
print(x_str)
print("my fav num is", x, ".", "x = ", x)
# concatenate all argument
print("my fav num is " + x_str + ". " + "x = " + x_str)

# the input() function take whatever you type, and you can store it in a variable
text = input("type something")

print(text)

text*3
# however note that it take everything as str, so you need to convert it if you want a number
number = int(input("type a number"))
print(number*3)