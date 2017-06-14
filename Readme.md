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

You also should install manually pip with `python get-pip.py`

### Using Anaconda

Anaconda is a distribution of software and libraries and uses *CONDA* (a package and environment manager) to manage versions and sandbox the environment needed for a python project including python version

+ Download [Anaconda] or
+ Use `wget https://repo.continuum.io/archive/Anaconda3-4.4.0-MacOSX-x86_64.sh`
+ Open a new terminal so you can use the `conda` command
+ Create the environment for an application with `conda create -n <app_name> python=<python_number(2 or 3)>`
+ Activate the environment for the application `source activate <app_name>`
+ Use `conda list` to see the installed libraries and versions for the environment
+ To install new packages or libs on the environment `conda install <dep1> <dep2> ...`
+ It's possible to use a text document to export a project requirements ``
+ To upgrade conda `conda upgrade conda`
+ To upgrade all packages `conda upgrade --all`


### Create an executable from a python script

To create a standalone executable from a python script we use [Pyinstaller]

in the Pyinstaller downloaded folder we need to run:

```
python pyinstaller.py <route to script> --windowed -F
```

Pyinstaller will create an executable for the current SO. In Linux to create a Windows executable we can use ***wine*** with python installed and run

```
wine python pyinstaller.py <route to script> --windowed -F
```  

The executable will be generated on the ***script-name/dist*** folder of Pyinstaller downloaded folder

### List of exercises

#### Personal exercises
+ *hello_word* - simple hello word
+ *rename_files* - using the OS rename files in a folder
+ *words_count* - Use of hash, sorting collections and lists
+ *check_profanity* - read from a file, consume API.
+ *reduce_array* - use the standard library fuction `reduce` to reduce arrays to single value
+ *entertainment_center* - class construction and instance, utf-8 codification, `webbrowser` library use
+ *inheritance* - POO Inheritance concepts and applications.
+ *strings* - string operations.
+ *tuples* - tuples few operations.
+ *dictionary* - hash map operations and file manipulation.
+ *list* - list examples of several operations including sorting, iteration and modification.
+ *prime* - defines whether a number is prime or not.

###### Turtle class samples  
+ *phycocircus* - create a circle with squares
+ *mindstorms* - basic figures
+ *flower* - a rose like figure

#### Google Python exercises
+ *hello* - Main class, system arguments, array splice, string trim.
+ *string1* - Basic string operations as substrings and replace.
+ *string2* - Basic string operations as substrings, find and replace.
+ *list1* - Basic list operations as iteration, sorting and tuples.
+ *list2* - Basic list operations as list merge, list append and list pop and use of reversed() operation.
+ *wordcount* - using dictionary count the frequency of a word in a text.

### Useful links
[Google python class] - free class for people with a little bit of programming experience who want to learn Python. in this repo are included the exercises of the course.

[Udacity Programming Foundations with Python] - Introductory programming class to learn Object-Oriented Programming, a must-have technique to reuse and share code easily. Learn by making projects that spread happiness…

[Coursera An introduction to Interactive Programming in Python] - This two-part course is designed to help students with very little or no computing background learn the basics of building simple interactive applications.

[Python books] - A Python Reading List by Wesley Chun.

[Python official documentation] - Official documentation for both versions.

License
----

MIT License

Copyright (c) 2016 John Tangarife

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Anaconda]: <https://www.continuum.io/downloads>
   [Atom Editor]: <https://atom.io/>
   [Python]: <https://www.python.org/>
   [linter]: <https://atom.io/packages/linter>
   [Google python class]: <https://developers.google.com/edu/python/>
   [Udacity Programming Foundations with Python]: <https://classroom.udacity.com/courses/ud036>
   [Fedora]: <https://getfedora.org/>
   [Coursera An introduction to Interactive Programming in Python]: <https://www.coursera.org/learn/interactive-python-1>
   [Python books]: <http://www.informit.com/articles/article.aspx?p=1849069>
   [Python official documentation]: <https://docs.python.org>
   [Pyinstaller]: <http://www.pyinstaller.org/>
