PennApps Main Landing Site
==========================

The main landing site for [pennapps.com](http://pennapps.com) and subsidiary sites. 


Requirements
============

*   SASS (`gem install sass`)
*   jinja2 (`pip install jinja2`)
*   watchdog (`pip install watchdog`)

Setup
=====

To get started, just run `foreman start`. This will create processes that:

- Locate the templates inside of `/templates` and compile them into `./`.
- Automatically recompile templates on change.
- Watch `./stylesheets` for changes and recompile `.scss` files on change.
