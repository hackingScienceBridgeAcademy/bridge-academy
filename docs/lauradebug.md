# Debugging Go4Code markdown & Testing scripts on RPi

## General comments
Make it clear that if you want to override a file the files must be written
exactly the same
filenames should not have spaces
Code blocks sometimes cut off end of code -- see snake line205

## Project Draw a picture
### Markdown
#### Corrections to be made
~~line91 row does not show as italics~~

~~line171 when the user holds the button to blink (make more explicit)~~

#### Suggestions
~~Remind students that python starts/counts from 0~~

~~Split paragraph (line109-line114) up, it can be simplified - maybe give an piece of code~~

~~line145/146 rewrite~~

### RPi testing
no bugs detected

## Project Magic eight ball

### Markdown
#### Corrections to be made
~~When references are made to pressing the joystick on trinket~~

~~explicitly say the user must press enter on keyboard~~

line39-41 should be put either on the homepage on the introduction lecture (NOTE this is found on all the project pages) **Lukas: Why? The skeleton codes are specific for each project.** _referring to comments on trinket account_

~~Rewrite line46-47~~

~~line189 rewrite~~

#### Suggestions
~~line19 change so to therefore~~

~~Rewrite lines 24-26~~

~~line151-153 possibly explain in more detail, could add an example for clarity~~

### RPi testing
~~script doesn't repeat question "ask ball a question after first shake"~~ **Should be fine**

## Project Paint

### Markdown
#### Corrections to be made
~~line89 random #~~

~~Change color to colour~~

~~line167-176 consider rewriting, various grammar mistakes~~

#### Suggestions
~~line94: change to "In this section we will define some variables which we will
use later on"~~

Change variables to cursor_x and cursor_y: easier to read **I try to avoid the underscore as it slows down the typing-speed for the kids**

### RPi testing
no bugs found

## Project MarbleMaze

### Markdown
#### Corrections to be made

Trinket simulator hard to control motion sensor- get supervisor to demonstrate
on their raspberry pi (supervisor should be prepared to do this for all project)

~~line114 make things happen .... change to something more specific~~

~~More information is needed on the functions, for example, what arguments can
they take, how to use them, i.e. does drawWall() place wall in same place
everytime?~~ **Added some more explanations. Although in those sections we only
ask the kids to copy code** _resolved_

Sections are not in order - this will cause confusion **This is unavoidable. The document
explains that we'll jump from section to section, but it is important that the supervisors
are aware of this as well. Maybe Ishan should go through this in the introductory lecture as well.** _resolved_



#### Suggestions
~~Reference yaw and pitch again in Sec 2.1~~

In general the project is quite difficult to follow - Sec 2.2 was a bit confusing

### RPi testing
overall game a bit buggy, ball doesn't always move

pixels flicker

## Project Snake

### Markdown
#### Corrections to be made

~~Slow down speed of game for first trinket example - quite hard to control for first go on trinket~~

~~Colour - need to define RGB e.g 0- 255~~ **This is done in the introductory lecture**
_resolved- may be worth repeating_

~~Code block line205 cuts off end sentence~~

~~Trinket code has full solution (only supposed to be skeleton)~~ **Are you sure? Can you check again?**
_resolved_

#### Suggestions

~~in general harder to follow due to difficulty of script~~

~~Encourage students to test code out after each section - not always clear~~

### RPi testing

Doesn't work - snake lib is not in skeleton folder on RPi config (checked on github)

## Project Countdown Clock

### Markdown
#### Corrections to be made

~~line104: missing 'should'~~

#### Suggestions


### RPi testing
in general works - however numbers flicker
