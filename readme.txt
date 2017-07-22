this project is a suorganizer blog project in the Django unleashed book starting at chap 2.
see  myDjangoProject app for another project used for freeform testing as book goes along.

see starting w/ page 14 of book. suorganizer stands for Startup Organizer.  Purpose being a
web application w/ list of startup companies, a blog and a newslink sections writen in Python
and utilizing Django as MVC web framework library.

startup notes:
1) cd to dir where you want to build the project. note windows dir command vs linux ls command to list
2) note in windows cmd window for the django startapp and migrate commands
  use python manage.py xxx vs the book script cmd version of ./manage.py xxx
3) once basic project setup w/ django commands open it in this as a new project and
  assign it python anaconda as the interpreter.  file/settings/project/ -see bootstrap note below

book creates a blog website during the course of the chapters and I am following along

see also the django main website and tutorial. they we very helpful in bootstraping the project
I added the django project to the anaconda library via the File/Settings/Project/ProjectInterpreter
and the small add (plus sign] in place of downloading via pip.

Iam using the command line tool, cd'ing to the correct directory and
using python manage.py [command] vs the book version of ./manage.py to execute scripts
and start the server.  see pg 20 and 24 specifically for starting the server

copy/paste links (in cmd wndo cd to dir of the appropriate project) then run to start localhost web server:
 python manage.py runserver 7777
http://127.0.0.1:7777  [port 8000 is the default for runserver cmd, if not otherwise specified]