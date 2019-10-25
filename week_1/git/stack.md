# Data Scientist Stack (TheGurus edition)

## OS

### 1. Primary option (default): Linux

#### Why Linux?
* Command Line Interface / Terminal / Shell: Windows is called Windows because of something! (Pedro dixit). Do not expect Windows desktop performance on Linux. For everything else but gaming and MS Office related things (including reporting tools like PowerBI or Tableau), Linux is better.
* Faster: pecially in computers with limited resources.
* Standard for Data Science tasks: heavy workloads runs on powerful servers and never in laptop or desktop computers. Most servers (99%) runs on Linux. Only a few in Windows server.
* Software: installing Open Source software in Linux is easy (`sudo apt install git` vs `install.exe`) and most Data Science related libraries are made for Linux.

#### Distros

As Linux is an open source project, anyone can fork the project and create its own version of the operating system. As a consequence of this, there are thousands of Linux __distros__ out there, each one is intended for a particular purpose/specialization, for example:
* Cibersecurity (Kali Linux)
* Phisics
* Public Administration

There are some 'base' distributions which are used as a foundation to create a lot of different versions and flavors:
* Debian -> Raspbian, Ubuntu
* CentOS & RHEL -> Fedora, Amazon Linux
* Arch -> Manjaro
    
### 2. If you can't use Linux: OSX

At least, you have a fully functional Unix style shell available, and its design is very beautiful...

### 3. Avoid at all cost: Windows

Windows is too far away from the standard. It can be used, but requires lots of knowledge and workarounds to make things happen.

## IDE

A Text Editor and an IDE are not the same.

* Text Editor: as its name says, it is used to edit any kind of text file. Usually support __syntax highlighting__ for a variety of programming languages, config files syntax,
etc. Some of them can be extended using plugins and lie somewhere in between a text editor and an IDE. Famous text editors are:
    * GNU nano
    * GNU Emacs
    * Vim
    * Sublime Text (commercial)
    * Atom
* IDE (integrated development environment): full soport for software development lifecycle, including __version control__, __debugging__, __datasource management__, __web development capabilities__, __deployment__, etc. Some important IDEs for Data Science are:
    * PyCharm
    * Spyder
    * Visual Studio
* Interactive Analytics:
    * Jupyter
    * RStudio

Our choice is __PyCharm__. Its only drawback is that it is a commercial product. Pro version is excellent, although it costs money. Community version is OK for most purposes like simple scripting and local development. For text editors, you should be familiar with at least one CLI based editor like GNU nano or Vim, as there is no graphical interface in a server you access via ssh.

In the next days we'll see other options for specific tasks like DBeaver for SQL.

## Programming Language

There is not a single option here. Everything depends on your purpose: Data Science (this bootcamp) vs Data Engineering. Pedro will talk about this extensively in the future. Today, the `must` for most purposes is Python (not R).

There are lots of options for installing and using Python. Our choice for this point is using __Anaconda Python Distribution along with its excellent environment and package manager, conda__. Do not install it right now, as we will perform this installation in class to avoid common mistakes.
