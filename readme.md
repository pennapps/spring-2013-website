PennApps 2012 Main Landing Site 
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

To build the sass run `sass --watch sass:css`. This will watch the `./sass` folder
for changes and automatically recompile the sass files into `./css`.

Pushing to Production
=====================

* `ssh-copy-id pennapps@pennapps.com` (passwordless ssh)

* `git remote add production ssh://pennapps@pennapps.com/home/pennapps/2012f/site.git` (adds new endpoint for pushing`

* `git push -u web master`
