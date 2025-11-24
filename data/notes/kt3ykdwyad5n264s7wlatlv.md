# Private methods
Private methods are those methods which can't be accessed in other class except the class in which they are declared.

- One underscore is to show it is a internal function: `_function_name()`
- Two underscores: the idea is to use double __ to fully disclose methods as private so python will convert them form __private_method to _Myclass__my_private_method and will not let a child class overwrite this method. 