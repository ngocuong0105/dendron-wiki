---
id: sblt0je6jawdlli798wvtc8
title: Organising Python Packages
desc: ''
updated: 1752699589497
created: 1679913366145
---
[blog](http://blog.habnab.it/blog/2013/07/21/python-packages-and-you/)

```
project_name/__init__.py
project_name/__main__.py
project_name/application.py
project_name/test/__init__.py
project_name/test/test_application.py
project_name/test/util.py
project_name/util.py
```

**Use absolute imports only (implcit relative imports in python 3 are NOT recommended)**

In all your files in the project:
```python
from project_name.util import *
```

**Don’t modify sys.path from code in your package**

**Don’t make your project root a package**

**Don’t set PYTHONPATH to try to make it go**


# Creating packages

- use the src layout
```
bulquant/
  src/
    bulquant/
      ...code...
  tests/
  examples/
  docs/
  setup.py
```

- flat layout
```
bulquant/
  bulquant/      # Module/package code here
  tests/
  examples/
  docs/
```

1. Prevents Import Bugs in Development With a flat layout, if you run pytest or scripts from the project root, Python can "find" your package accidentally because it's in the same dir as your test file, not because it's correctly installed via pip.

From the top-level (bulquant/), run:
`pip install -e src`

then you can import bulquant