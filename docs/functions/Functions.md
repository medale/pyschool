% Python Basics
% Functions
% Markus Dale, 2018

# Python - organizing code
![](graphics/sand_flower.jpg)

# Functions
* code reuse
* minimize repetition (DRY principle - don't repeat yourself)
* procedural programming

# Types of functions
* Built-in functions (no import necessary): `len(str), open, sorted, map`...
* Core module functions: 
     * `import math, os`
     * `math.sqrt(), os.getcwd()`...
* Third party module functions:
     * Must be installed, e.g. `pipenv install requests`
     * `import requests`
     * `response = requests.get("http://docs.python.org")`
* User-defined - def, lambda

# Named functions - learning/functions/defs.py
* a def function definition is an object with a name
* function is not executed until called at runtime

```python
def function_name(arg1, arg2):
   statements
   return result
   

def foobar(arg1):
   if arg1 > 100:
      return 'foo'
   else:
      return 'bar'
```

# Functions are first-class objects - learning/functions/first_class_objects.py
* def 'name' assigns 'name' as a reference to the function object
* Can assign new reference name
* Can pass functions to other functions as arguments
* Can return a function from a function
     