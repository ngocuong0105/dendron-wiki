
# 28th B-Day

This year I will celebrate at home - Granger House. [finish investing, no career grinding]

27th birthday I celebrated in a bar in Stratford. [chill + start investing]

26th I celebrated in Whitechapel! [grind year and success]

25th I celebrated at home in Bethnal Green. [grind year]

24th I celebrated in bar Caldo. [grind year]

23rd Oxford

I wish last two years I have made more progress career-wise. Or at least were able to learn more things. I am currently in the trap of being alright. 


# Statically vs Dynamically typed languages

Python is dynamically typed but supports static typing using tools like **mypy**

statically typed languages:

- Java, C++
- require defining explicit definition of the type of the variables
- variables cannot change their type
- type checks are done at compile time (before runtime)

dynamically typed languages:

- Python
- no need to tell type of variables *x=5* , then *x= 'string'*
- one variable can take different types
- type checks done at runtime (a bit slower)
- **type hinting** or **type annotation** *x: int = 5* is just used fo documentation purposes
- you can use static type checker tool like *mypy*


# DataFramely

Data Validation for DataFrames using schema-based approach. Allows you to do type, range, nullability checks at run-time. If they do not pass the program return a SchemaError.

[QuantCo Polars DataFrame Validation Library](https://tech.quantco.com/blog/dataframely)

Python does not support real static type checks. Tools like mypy introduces static type checks but are not able to check the contents of tables/dataframes. 

Pandera is a tool that allows you to:
- define a schema
- do checks on dataframes at runtime
- improve readability on dataframes objects and easier debugging



