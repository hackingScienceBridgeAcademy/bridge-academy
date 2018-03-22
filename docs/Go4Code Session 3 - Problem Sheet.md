# Go4Code Session 2 - Problem Sheet

### Problem 1 - Cake party

A successful party should have enough cakes for everyone to eat. The correct
cake-to-person ratio is 0.2 (e.g. there should be 1 cake for every five people).

Write a function called *is_there_enough_cake* that returns a Boolean value
depending on whether there's enough cake in the party! The function should
take two integers as arguments, *num_of_people_* and *num_of_cakes*.

Example output:

    >>> is_there_enough_cake(2, 10)
    True
    >>> is_there_enough_cake(5, 1)
    True
    >>> is_there_enough_cake(6, 1)
    False
    >>> is_there_enough_cake(11, 2)
    False

_Note:_
If you're using an older version of Python, like version 2.7, you have to be
wary of dividing integers! Use _float_ to convert integers to floating-point
numbers.

### Problem 2 - Create your own dictionary

Write a program that lets you provide you create your own dictionary.

The program should ask whether you want to add a new word, or whether you want to look up a word you've already defined. You should also have the option of seeing the whole dictionary.

The program should give an error if the user asks for a word that isn't in the dictionary.

Example output:

	Do you want to look up a word ('lookup'), define a new word ('define') or see the whole dictionary ('dictionary')?
	>>> define

	What's the word?
	>>> python

	What's your definition?
	>>> Python is a programming language (and a genus of snake).

	The word 'python' is now defined.

	What's the word?
	>>> jazz

	What's your definition?
	>>> Jazz is a genre of music, often involving saxophones and trumpets.

	The word 'jazz' is now defined.

	Do you want to look up a word ('lookup'), define a new word ('define') or see the whole dictionary ('dictionary')?
	>>> lookup

	What word do you want to look up?
	>>> python

	python:
	Python is a programming language (and a genus of snake)

	Do you want to look up a word ('lookup'), define a new word ('define') or see the whole dictionary ('dictionary')?
	>>> programming

	The word 'programming' is not in the dictionary!

	Do you want to look up a word ('lookup'), define a new word ('define') or see the whole dictionary ('dictionary')?
	>>> dictionary

	python:
	Python is a programming language (and a genus of snake)

	jazz:
	Jazz is a genre of music, often involving saxophones and trumpets.

### Problem 3 - Tic Tac Toe (Hard)

Create a program that lets you play Tic Tac Toe! Example output:

		Game:
		...
		...
		...

		Player X - row:
		>>> 1
		Player X - column:
		2

		Game:
		.X.
		...
		...

		Player O - row:
		>>> 1
		Player O - column:
		3

		Game:
		.XO
		...
		...

		Player X - row:
		>>> 1
		Player X - column:
		3

		There's already a tac there!

		Game:
		.XO
		...
		...

		Player X - row:
		>>> 2
		Player X - column:
		2

		Game:
		.XO
		.X.
		...

		Player O - row:
		>>> 2
		Player O - column:
		3

		Game:
		.XO
		.XO
		...

		Player X - row:
		>>> 3
		Player X - column:
		2

		Game:
		.XO
		.XO
		.X.

		Player X wins!

### Problem 4 - Adding step-counter to _Get to the goal_

Modify the code for the _Get to the goal_ game from Session 3 (you can find the code in the DropBox folder containing all the course material), so that the game keeps track of how many steps the player has taken. When the player reached the goal, the game should say how many steps it took to get there.

### Problem 5 - Fibonacci series (Hard)

These are the first nine numbers in the Fibonacci series:

    1, 1, 2, 3, 5, 8, 13, 21, 34 ...

Each number in the series is the sum of the previous two. Using a _for_-loop
generate the first 100 numbers in the Fibonacci series.

### Problem 6 - Recursive Functions: Summing numbers (Hard)

Create a function that takes an integer N as an argument, and returns the sum of
the numbers. Sounds easy? Well you probably know how to do it using a _for_
loop, but this time try doing it using a _recursive function_.

A function is _recursive_ if it calls itself inside its own body code. Here's
an example of a function that will print out each letter of a string line-by-line.

  def print_letter_by_letter_recursively(a_string):
    if len(a_string) == 0: # Exit if the string is empty.
      return

    print(a_string[0]) # Print first letter of the string
    a_string2 = a_string[1:] # Slice the string, skipping the first letter.

    print_letter_by_letter_recursively(a_string2) # Recursively call the function again with the shortened function.

Output:

    >>> print_letter_by_letter_recursively("Hello World")
    H
    e
    l
    l
    o

    W
    o
    r
    l
    d

Can you figure out a way to create a function *sum_recursively(n)* that returns
the sum of the numbers from 1 to *n*?

### Problem 7 - Recursive Functions: Fibonacci series (Very Hard)

Try problem 7 again, but this time do it using a _recursive function_. This is
quite a hard problem, so try Googling for some help. Even if you can't figure
out how to implement the function yourself, it's a worthy intellectual task
to just understand how it could be done (there's a lot of examples of this
code online).

The function should be called _fib_, and it should take an integer as its
argument. _fib(0)_ should return the first element of the series, _fib(1)_
the second, and so on.

After you've written the function, use it to print out the first 20 numbers
of the series.

Example output:

  >>> for i in range(20):
  ...    print(fib(i))
  1
  1
  2
  3
  5
  8
  13
  21
  34
  55
  89
  144
  233
  377
  610
  987
  1597
  2584
  4181
  6765

### Problem 8 - Fully-fledged version of _Get to the goal_ (Extremely hard)

Are you ready to be challenged? The following task is _very_ difficult, and will
necessitate not only using all the things you've already learnt, but also finding
new knowledge (through either reading a Python book, or by Googling).

In this problem, you'll be creating a fully-fledged game, similar in setup to the
one made in Session 3.

The game map is now a lot more complicated:

		.....|.....?.......H..........|.............................
		..!..|..........?.............|.....!..........?............
		.....|.....!...............!..|.......................G.....
		.H...|............============|.............................
		.....|.?..........H...........|.................!...........
		.....\======\.......|.........|......=======================
		............|..!....|......?..|.............................
		|...........|.......|.........|.......?.....................
		|.....?.....\==========\......|..........................!..
		|......................|......|=====================........
		|..?...................|......|...........?.................
		|..................H...|......|......H......................
		|............!.........|......|.......................!.....
		==============\........|......|......=======================
		|.............|...............................!....!........
		|.............|............?...........H...........!...!....
		|.............|.....H.........?......===============\....!..
		|...?....|....\========.............................|.......
		|........|..................!............!..........|..?.?..
		|...X....|.........................!...........H....|.......
		=========|==========================================|..?..?.

The player is till marked by "X", and the goal by "G", but now there are a lot of other factors at play. The player now has a _health_ bar and a _score_.

 - The "?" are the _runners_, they move around randomly along the map. If the player catches one, the score increases.
 - The "!" are the _attackers_, they too move around randomy along the map. If they stand next to the player, the player will lose one health point.
 - The "H" are the health packages. If a player moves on top of one, one health point will be regained.

As previously, if the player gets to "G", the game is won.

If you don't feel like you're at the level where you can complete this task yet,
don't worry! An alternative exercise would be to just read through the solution
to this problem, and trying to understand how the code works.
