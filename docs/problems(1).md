### Problem 5 - A game of darts (Hard)

In a real game of darts, a player gets different scores depending on which part
of the board  the dart hits. In a simplified version of the game we'll have
three regions:

<img src="media/problem5-dartboard.png" width="400px"/>

We have an small circular region in the middle of radius _r_, the donut-shaped
of the larger circle excluding the inner circle, and the area outside the
dartboard.

Set _r = 1_ and _R = 5_. Write a program that estimates the probabilities
of a dart landing in each region of the dartboard.

You can use and modify the code from the _Monte Carlo_ simulation to complete
this task.


### Problem 4 - Sorting a list of people by their age

We have a registry of people's ages in our club:

  ages = { "Mark" : 17, "Ishan" : 14, "Harjeet" : 20, "Armando" : 21, "Laura" : 19, "Haruki" : 13,  "Linus" : 21}

and a list of the members

  club_members = ["Ishan", "Laura", "Harjeet", "Mark", "Linus", "Armando", "Haruki"]

Create another version of the _bubble sort_ function called *sort_member_list*
that takes as an argument a list of members, as well as a dictionary that contains
their ages. It should sort the list by age (youngest to oldest). You'll have to use
the dictionary to cross-reference the member's names to their ages.

Example output:

  >>> ages = { "Mark" : 17, "Ishan" : 14, "Harjeet" : 20, "Armando" : 21, "Laura" : 19, "Haruki" : 13,  "Linus" : 21}
  >>> club_members = ["Ishan", "Laura", "Harjeet", "Mark", "Linus", "Armando", "Haruki"]
  >>> sort_member_list(club_members, ages)
  >>> print(club_members)
  ['Haruki', 'Ishan', 'Mark', 'Laura', 'Harjeet', 'Linus', 'Armando']


  ### Problem 3 - Sorting a string in alphabetical order

  Create a version of your _bubble sort_ function that can sort a string in
  alphabetical order. You should use the _ord_ function, that converts a character
  to a number, to measure whether one character is "larger" than another one.

  An important difference between strings and lists is that strings are similar to
  tuples, in the sense that you can't add, remove or change the elements. This
  will cause some complications in your code, and you'll have to find a way
  around  that.

  ### Problem 3 - Sorting a string in alphabetical order

  Create a version of your _bubble sort_ function that can sort a string in
  alphabetical order. You should use the _ord_ function, that converts a character
  to a number, to measure whether one character is "larger" than another one.

  An important difference between strings and lists is that strings are similar to
  tuples, in the sense that you can't add, remove or change the elements. This
  will cause some complications in your code, and you'll have to find a way
  around  that.
