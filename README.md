PennApps Main Landing Site 
------------------------------------

Being the main landing site for [pennapps.com](http://pennapps.com) and subsidary sites. 


Requirements
============

*   SASS (gem install sass)
*   jinja2 (pip install jinja2)
*   (optional) watchdog (pip install watchdog)

Setup
=====

To build the jinja templates, simply run 'python build.py'. This will locate the
templates inside of `/templates` and compile them into `./`. If you install
watchdog, you can also run 'python build.py --watch' to automatically recompile
templates on change.

To build the sass run `sass --watch stylesheets`. This will watch the `./stylesheets` folder
for changes and automatically recompile the .scss files.
