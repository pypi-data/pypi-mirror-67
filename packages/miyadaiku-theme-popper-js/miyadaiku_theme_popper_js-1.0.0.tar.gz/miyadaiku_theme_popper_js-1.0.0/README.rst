
Popper.js files for miyadaiku static site generator
========================================================

Provides `Popper.js 1.16.1 <https://github.com/FezVrasta/popper.js/>`__ files.


Installation
-------------------

Use pip command to install Popper.js. 

::

   $ pip3 install miyadaiku_theme_popper_js


Configuraion
----------------------


In your config.yml file of your project, add following configuration at `themes` section.

::

   themes:
     - miyadaiku_theme_popper_js    # <---- add this line


Usage
----------------------

Add following code to your template files.

::

   <!-- include Popper.js -->
   {{ popper_js.load_js(page) }}

