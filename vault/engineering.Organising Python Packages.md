---
id: sblt0je6jawdlli798wvtc8
title: Organising Python Packages
desc: ''
updated: 1679914207736
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

