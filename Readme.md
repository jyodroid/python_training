# Python learning

This repository is a compilation of python exercises in the road of learning

### Tech

* [Python] - version 2.7 and 3.5. Python is a programming language that lets you work quickly and integrate systems more effectively.
* [Atom Editor] - A hackable text editor for the 21st Century
* [Fedora] - Linux redhat based operative system. version 25

And some Atom plugins

### Installation

Fedora already has python 2 and python 3 installed and you can se with the command

+ `ls /usr/bin/python*`

but we want to switch between version easily depending project so from the resulting list with the previous command we install alternatives with versions we will use

+ `sudo alternatives --install /usr/bin/python python /usr/bin/python3.5 1`
+ `sudo alternatives --install /usr/bin/python python /usr/bin/python2.7 2`

to alternate between alternatives `sudo alternatives --config python` then select the number of the version you will use.

for development on ***atom editor***:

+ Install linter plug-in `apm install linter`
+ then install Python Linter package to show error on atom editor
  + install flake8  `pip install flake8`
  + install flake pep25 `pip install flake8-pep257`


+ Install linter for flake8 atom plug-in`apm install linter-flake8`
+ Install autocomplete for phyton `apm install autocomplete-python`
+ run examples with `python example_name.py`

### List of exercises

+ *hello_word* - simple hello word
+ *rename_files* - using the OS rename files in a folder
+ *words_count* - Use of hash, sorting collections and lists
+ *check_profanity* - read from a file, consume API.
+ *reduce_array* - use the standard library fuction `reduce` to reduce arrays to single value
+ *entertainment_center* - class construction and instance, utf-8 codification, `webbrowser` library use
+ *inheritance* - POO Inheritance concepts and applications

###### Turtle class samples  
+ *phycocircus* - create a circle with squares
+ *mindstorms* - basic figures
+ *flower* - a rose like figure

### Useful links
[Google python class] - free class for people with a little bit of programming experience who want to learn Python. in this repo are included the exercises of the course.

[Udacity Programming Foundations with Python] - Introductory programming class to learn Object-Oriented Programming, a must-have technique to reuse and share code easily. Learn by making projects that spread happiness…

License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Atom Editor]: <https://atom.io/>
   [Python]: <https://www.python.org/>
   [linter]: <https://atom.io/packages/linter>
   [Google python class]: <https://developers.google.com/edu/python/>
   [Udacity Programming Foundations with Python]: <https://classroom.udacity.com/courses/ud036>
   [Fedora]: <https://getfedora.org/>
