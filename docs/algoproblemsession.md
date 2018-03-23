
# Go4Code - Session 3
## Functions and Algorithms
---

## 1. Recap

Previous session included topics:

- _For_ loops
- _While_ loops
- _Boolean_ expressions
- _Lists_
    - Adding elements to a list
    - List indexing
    - Lists slicing

## 2. Dictionaries

- _Dictionaries_ are another type of **data structure**.

- Sometimes in other programming languages, dictionaries will be called _hash maps_.

- Lists store information in a _sequence of ordered data_.

- Dictionaries are _not_ ordered. Instead they work very similarly to, well, dictionaries!

<img src="media/dictionary.png">

In a dictionary, to each word there's an associated description. The definiton of the word _python_ in the Oxford dictionary is:

    programming (noun):
    The process of writing computer programs.
    
In other words, for each word there's some associated data. Python dictionaries associate _values_ with _keys_. The previous Oxford definiton, along with some more definitions, can be programmed in the following way in Python


```python
oxford_dictionary = {"programming" : "The process of writing computer programs.",
                    "python" : "A large heavy-bodied non-venomous snake occurring throughout the Old World tropics, killing prey by constriction and asphyxiation.",
                    "raspberry" : "An edible soft fruit related to the blackberry, consisting of a cluster of reddish-pink drupelets."}
```

Python _dictionaries_ are useful because we can access _values_ using their _keys_.


```python
print("The definition of the word 'programming' is: " + oxford_dictionary["programming"])
```

### Adding _keys_ and _values_ to dictionaries

**key-value pair:** Each piece of data in a dictionary is called a *key-value* pair.

It's very simple to add new key-value pairs to a dictionary. An empty dictionary is created like this:


```python
my_information = {}
```

Add keys and values:


```python
my_information["first_name"] = "Homer"
my_information["last_name"] = "Simpson"
my_information["gender"] = "male"
my_information["IQ"] = 105

# display the information

print("My name is " + my_information["first_name"] + " " + my_information["last_name"] + " and I'm " +
      my_information["gender"] + " and I have an IQ of " + str(my_information["IQ"]))
```

#### Using different types of keys and values

You can use any kind type of data as either a key or a value.


```python
my_dict = {}

my_dict[123] = "A number is the key to this value."

my_dict["A string is the key to this value"] = 123

my_dict["This key points to a list"] = ["This", "is", "a", "list"]
```

### Checking if a _key_ is in a dictionary

To check if a key is in a dictionary, we do the same things as we do with lists.


```python
member_ages = {
    "Mark" : 12,
    "Ishan" : 32,
    "Harjeet" : 16,
    "Armando" : 19,
    "Laura" : 22,
    "Haruki" : 10,
    "Linus" : 25
}

if "Harjeet" in member_ages:
    print("Harjeet is " + str(member_ages["Harjeet"]))
else:
    print("Harjeet is not in the registry.")
    
if "Lukas" in member_ages:
    print("Lukas is " + str(member_ages["Lukas"]))
else:
    print("Lukas is not in the registry.")
```

### Looping through the keys in a dictionary

We loop through the keys in the dictionary the same way we loop through lists.


```python
member_ages = {
    "Mark" : 12,
    "Ishan" : 32,
    "Harjeet" : 16,
    "Armando" : 19,
    "Laura" : 22,
    "Haruki" : 10,
    "Linus" : 25
}

for name in member_ages:
    print(name + " is " + str(member_ages[name]))
```

### Exercises with dictionaries

 - **Problem 1:** Create a dictionary that contains some information about you. It should contain your first name, last name, age and which school you go to.


```python
my_dict = {"Name" : "Stephen", "Last Name" : "Hawking", "Age" : 72, "School" : "University of Cambridge"}
```

 
 - **Problem 2:** This problem is a bit harder! Create a program that let's you store the rankings of the members of your club in a dictionary, and then let's you print them all by entering a command _rankings_ (you don't have to print them in order). The program should only allow you to create new entries, if the user tries to enter a name that already exist, the program should say that that's not allowed. Example output of the program:

        Name of member (enter 'rankings' to see all rankings):
        >>> Lukas

        What is the rank of Lukas?
        >>> 1

        Name of member (enter 'rankings' to see all rankings):
        >>> Ishan

        What is the rank of Ishan?
        >>> 2
        
        Name of member (enter 'rankings' to see all rankings):
        >>> Lukas

        Lukas is already in the registry!
        
        Name of member (enter 'rankings' to see all rankings):
        >>> Laura
        
        What is the rank of Laura?
        >>> 2
        
        Name of member (enter 'rankings' to see all rankings):
        >>> rankings
        
        Rankings:
        Lukas - 1
        Ishan - 2
        Laura - 2
        
    To complete this task you should use a _while_-loop.


```python
rankings = {}

while True:
    print("Name of member (enter 'rankings' to see all rankings, or 'quit' to exit):")
    inp = input(">>> ")
    print("")
    
    if inp == "quit":
        break
    elif inp == "rankings":
        for name in rankings:
            print(name + " - " + str(rankings[name]))
        print("")
    else:
        if inp in rankings:
            print(inp + " is already in the registry!")
            print("")
        else:
            print("What is the rank of " + inp + "?")
            rank_inp = int(input(">>> "))
            print("")
        
            rankings[inp] = rank_inp
        
    
```

## 2. Functions

- Loops are one way to avoid repeating code.
- Another way is to use _functions_.
- Functions are a piece of code that does a specific task.
    - We name these functions, e.g. _print_ or _len_.
    - The functions can _return_ values.
    - The functions can take _arguments_.
    - It essentially takes some _input_ (or _arguments_) and returns some _output_.
    
<img src="media/function.png" width="300px">

### Defining a function

The basic structure of a function definition is

    def function_name(argument1, argument2, argument3, ...):
        """Some comments that describe how the function works"""
        # code that does something
        
A lot of functions will also _return_ a value

    def function_name(argument1, argument2, argument3, ...):
        """Some comments that describe how the function works"""
        # code that does something
        return some_value


```python
def adds_two_numbers(number1, number2):
    """Takes two numbers and returns their sum"""
    sum_of_numbers = number1 + number2
    return sum_of_numbers

print(adds_two_numbers(5, 6))
```

### A function that adds elements to a list

What will the following code output?


```python
def list_extender(l):
    """Adds elements to a list"""
    list_length = len(l)
    l.append(list_length)
    
my_list = []
for i in range(10):
    list_extender(my_list)
    
print(my_list)
```

### A function that calls another function

What will the following code output?


```python
def function1():
    n = function2()
    return n*2

def function2():
    n = 5
    return n

print(function1())
print(function2())
```

### Return multiple values

What will the following code output?


```python
def mult_values():
    return ("This is a number: ", 10)

(s, x) = mult_values()

print(s)
print(x)
```

### Function _scope_

What will the following code output?


```python
def function1():
    message = "Hello, this is a message!"
    
function1()
print(message)
```

In programming terminology, we'd say that the variable _message_ is not in the _scope_ of the code outside of the function. The only part of the code where we can actually reference _message_ is inside the body code of the function _function1_.

### Changing different types of variables

What will the following code output?


```python
def change_a_string(s):
    s = s + " world"
    
def change_an_integer(i):
    i = i + 1
    
def change_a_list(l):
    l.append(2)
    l = l + [3, 5, 1]
    
def change_a_dictionary(d):
    d["new key"] = "new value"

my_string = "Hello"
my_int = 5
my_list = [1, 7, 4]
my_dict = { "key" : "value" }

change_a_string(my_string)
change_an_integer(my_int)
change_a_list(my_list)
change_a_dictionary(my_dict)

print(my_string)
print(my_int)
print(my_list)
print(my_dict["new key"])
```

### Exercises with functions

- **Problem 4:** Create a function that takes a list of numbers as its argument, and returns the product of all elements in the list.

  Example output:

      >>> print(products([4, 5, 6]))
      120
      >>> print(products([2, 3, 5]))
      30


```python
def product(nums):
    p = 1
    
    for n in nums:
        p *= n
        
    return p

print(product([4, 5, 6]))
print(product([2, 3, 5]))
```

- **Problem 5:** In Python (and in most other programming languages) each string character has an associated integer value. To get the integer value of a character, we can use the _ord_ function.

      >>> print(ord("a"))
      97
      >>> print(ord("b"))
      98
      >>> print(ord("A"))
      65
     
  *Note: Although not necessary to solve the problem, to learn more about how and why characters have numbers associated to them, Google "ASCII".*
  
  Create a function _numsum_ that takes a string as its argument. Use the _ord_ funciton to find the numerical sum of all the characters in the string and return that value. You should do this by looping through the string and summing the numerical values of the characters into a variable.
  
  Note that the first letter of the alphabet has the value 97, but we want to count it as 1. Therefore you'll have to subtract 96 from it, and all other characters.
  
  Example output:
  
       >>> numsum("Hello")
       52
       >>> numsum("World")
       72
       
  Note that we want to count capital letters and lowercase letters as the same. We can do this by converting our string to lowercase using the _string.lower()_ method.
  
      >>> print("ALL CAPS".lower())
      all caps


```python
def numsum(s):
    n = 0
    s = s.lower()
    
    for c in s:
        n += ord(c) - ord("a") + 1
        
    return n
        
print(numsum("Hello"))
print(numsum("World"))
```

## 3. Implementing a _logging in_ feature

You're probably familiar with the concept of _logging in_, that is, using a username and a password to get into some account (like Facebook, for example). In this section we'll be using the skills that we've learnt so far to build a real practical example of what a program could look like, we'll be building a simple program that lets a user _log in_.

This is the basic output that we'd expect from the program:

    Enter your username (if you don't have an account, enter 'register'):
    >> mark123

    No user with that name!

    Enter your username (if you don't have an account, enter 'register'):
    >> register

    What will your username be?
    >> mark123

    What will your password be?
    >> mypassword

    Enter your username (if you don't have an account, enter 'register'):
    >> mark123

    Enter your password:
    >> password123

    Wrong password!

    Enter your username (if you don't have an account, enter 'register'):
    >> mark123

    Enter your password:
    >> mypassword

    You are now logged in!
    
You should complete this task using your newfound knowledge of _dictionaries_ and _functions_.

### Basic structure

These are the functions that you'll have to implement:


```python
def register_user():
    """Registers a new user"""
    print("What will your username be?")
    username = input()
    print("")

    print("What will your password be?")
    password = input()
    print("")

    # Create the user by adding it to the dictionary "users"
    users[username] = password

def check_user_credentials():
    """Check if user is in system. Should return true if the user succeeds, and false if the user fails."""
    print("Enter your password:")
    password = input()
    print("")

    # Check if password is correct
    if users[inp] == password:
        print("You are now logged in!")
        print("")
        return True
    else:
        print("Wrong password!")
        print("")
        return False
```

Fill in the *while*-loop below, using the functions above, in order to create the program.


```python
users = {}

while True:

    print("Enter your username (if you don't have an account, enter 'register'):")
    inp = input()
    print("")

    if inp == "register":
        register_user()
    elif inp in users:
        if check_user_credentials():
            break
    else:
        print("No user with that name!")
        print("")
```

## 4. A simple game: "Get to the goal"

In this section we'll be creating a simple text-based game called _Get to the goal_. In the game you (marked by an "X") will be moving around on a 2D map, trying to reach the goal (marked by a "G"). This is the expected output of the program:

    X.........
    ..........
    ..........
    ..........
    ..........
    ..........
    ..........
    .......G..
    ..........
    ..........

    Where should the X move (l, r, u, d), enter 'quit' to exit:
    >>> r
    
    .X........
    ..........
    ..........
    ..........
    ..........
    ..........
    ..........
    .......G..
    ..........
    ..........

    Where should the X move (l, r, u, d), enter 'quit' to exit:
    >>> d
    
    ..........
    .X........
    ..........
    ..........
    ..........
    ..........
    ..........
    .......G..
    ..........
    ..........

    Where should the X move (l, r, u, d), enter 'quit' to exit:
    >>> r
    
and after many more moves...

    ..........
    ..........
    ..........
    ..........
    ..........
    ..........
    .......X..
    .......G..
    ..........
    ..........

    Where should the X move (l, r, u, d), enter 'quit' to exit:
    >>> d
    
    Well done! You completed the game!
    
This is quite a hard task, so we'll have to think about how we're going to structure this program, before we try to do it.

### Declaring the necessary variables

What kind of variables do we need to create this program. An obvious example of two variables is that we need to store the position of the player: the position along the *horizontal-axis*, and the position along the *vertical-axis*.


```python
pos_x = 0 # x-coordinate of the player
pos_y = 0 # y-coordinate of the player

map_w = 10 # Width of map
map_h = 10 # Height of map

goal_x = 7 # x-coordinate of the goal
goal_y = 7 # y-coordinate of the goal
```

### Drawing the map

With the variables now defined, let's write a function that can draw the game _"map"_ as depicted in the example output.

*Hint: You should use two nested for-loops that runs through all the coordinates on the game map. The game map should be drawn row-by-row using the print() function, so the trick is to construct these rows of strings using the addition operator "+".*


```python
def draw_map():
    """Draws the game map"""
    for y in range(map_h):

        map_row = ""

        for x in range(map_w):

            if x == pos_x and y == pos_y: # Check if player is at that point, in which case draw the player
                map_row += "X"
            elif x == goal_x and y == goal_y: # Check if goal is at that point, in which case draw the goal
                map_row += "G"
            else: # Otherwise draw empty space (period .)
                map_row += "."

        print(map_row)
```

### Constructing the program

- Now what's left is to write the main body of the program. Since the program should keep on running until the user either wins, or decides to quit, we should use a _while_-loop.

- The two main things you have to make sure you do in the loop is to ask the user for input, and move the "X" depending on what the user answers. Make sure that if the user crosses the boundary of the map, that's dealt with properly.

- You should also make sure that if the user is standing on the goal, we should exit the game and tell the user he/she has won.


```python
while True:

    draw_map()

    print("")

    print("Where should the X move (l, r, u, d), enter 'quit' to exit:")
    inp = input()

    print("")

    if inp == "quit":
        break

    # Move around the player
    if inp == "l":
        pos_x -= 1
    elif inp == "r":
        pos_x += 1
    elif inp == "u":
        pos_y -= 1
    elif inp == "d":
        pos_y += 1

    if pos_x < 0:
        pos_x += map_w
    elif pos_x >= map_w:
        pos_x -= map_w

    if pos_y < 0:
        pos_y += map_h
    elif pos_y >= map_h:
        pos_y -= map_h

    if pos_x == goal_x and pos_y == goal_y:
        print("")
        print("Well done! You completed the game!")
        break

```
