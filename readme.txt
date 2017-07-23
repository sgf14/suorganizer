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

VCS- git and github note:
1) Git- 07/21/17: note the local git setup was easy enough, just select the VCS menue then 'enable version oontrol...'
and select git. (note that selection goes away after its setup).  then all the files turn green indicating they need to be
committed.  select the project again then right click/git/commit and add a commit note the same way you will push
all commits in future (w/o the 'push' to remote GitHub obviously- that hasnt happened yet.
2) GitHub was a little trickier.  I could not make the PyCharm VCS/Import Into Version Control/Github or the Settings
Github version work out and create the remote 'origin' presence.  kept getting a login failure.
Had to go into local version of Github (the github app on the desktop)
, establish the project in there by creating a new project and referencing/cut paste, this project directory
into that.  then select the Publish link.  Once that is setup you can commit and push to update git and git hub,
the same as all your eclipse projects.
    2.1) To do this you DO NOT setup the project (repository) in GitHub first.  the desktop app does
    that for you.  Im my case I had to delete the online repository I created, but was empty.
    2.2) So unlike Eclipse/Java it doesnt actuaally move the project into its own git directory (and out of workspace).  Pycharm
    leaves the project in the directory as long as you have the right link to you local git dir.