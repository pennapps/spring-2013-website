PennApps 2012 Main Landing Site 
------------------------------------

Being the main landing site for [pennapps.com](http://pennapps.com) and subsidary sites. 


Requirements
============

*   SASS
*   jinja2

Setup
=====

To build the jinja templates, simply run 'python build.py'. This will locate the
templates inside of `/templates` and compile them into `./`.

To build the sass run `sass --watch sass:css`. This will watch the `./sass` folder
for changes and automatically recompile the sass files into `./css`.
