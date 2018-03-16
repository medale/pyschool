% Python Basics
% Statements
% Markus Dale, 2018

# Python - making statements
![](graphics/gallatin_national_forest.jpg)

# if, elif, else - statements/ifs.py
```python
# first condition evaluating to true gets executed
    if count > 10:
        print('big')
    elif count < 10 and count > 5:
        print('medium')
    else:
        print('small')
```

# for loop - break, continue, for/else - statements/fors.py
```python
    countries_to_capitols = country_to_caps()

    capitols_to_countries = {}

    # We want to iterate over all items
    for k,v in countries_to_capitols.items():
        capitols_to_countries[v] = k
```

# while loop - statements/whiles.py
```python
while test:    
   statements    
   if test: break                 # Exit loop now, skip else if present    
   if test: continue              # Go to test at top of loop now
else:    
   statements                     # Run if we didn't hit a 'break'                                  
```
Source(Mark Lutz, Learning Python 5th edition, O'Reilly, 2013)
