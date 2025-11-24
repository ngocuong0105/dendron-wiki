
# Merging Feature
1.1 Summary points on merging feature:
- Given cashflows for diifferent products - aggregate them to get a summary report
    e.g NPV -> weighted mean on accounts
    e.g Discount rate -> harmonic mean
    - These reports are used in the decision making to decide which programs are
        worth  pursuing and which not 
    -  Monitoring the risk the bank is taking when giving credits
- It follows ETL process: extract data from parquet files; transform data by
combination functions
- Load data in OneFlow workflow to produce automatic excel report

1.2  We heavylift the database (parquet files), the dispatching manually in python. Not like Django Flask frameworks where everything is checked this is getting the correct request, is it from the write url etc. 
- Created additive dispatching for computing 200+ fields each using different type of  combining function( yaml file combination  functions mapping field -> function) (name mapping algo tailor to Principles of Computer System Design Book) From book notes: Frequent name-mapping algorithms:
- Table lookup
- Recursive lookup
- Multiple lookup

1.3 Main benefit is that they are additive no need for refactoring endless if else statements. When add in another Field or Dunction
Read more about that in SICP Chapter 2 Python version page 52, Type dispatching. In your case the dispatching is the merging function for the different CFS and CRM fieldds
1.4 Challenges: How to handle so many fields=business metrics -> scaled using static 
dispatch mapping and message passing.
- Unit tests did not prove enough covarege for the combination functions
- Integration tests with realistic data showed a lot of mismatches and errors in our combining functions. Though unit tests tried to capture edge cases etc, realistic data turned out to be much messier than we expected.
- Thus for T-C feature we will create the feature and do integration tests in parallel.

# T-C feature
2.1 Given  test and control data sets return reports of the differences between the two
- Used to test hypothesis , e.g. control data are logtime users test are new clients, see how 
they behave

2.2 Created  Directory for Dispatiching (imrovement on the previous feature) yaml to paralize   

when new dispatches and messegaes were created across different people
This direcotry of dispatching grouped similar fields = summary statistics/business metrics!
2.3 Introduced test driven developement, before relied only on unit tests, now create integration tests alongside the feature. Reasoning for using it is because OneFlow is a data tool and heavilyt relies on the data. If it is messy, tests fail more easily. Alot of edge cases to mke sure OneFlow does the right computation

Benefits: 
reduced debugging effort – when test failures are detected, having smaller units aids in tracking down errors.

2.4 applied Incremental developement:
- Unit testing : when you test a module in isolation, you can be confident that any bug you find is in that unit – or
maybe in the test cases themselves.
-Regression testing : when you’re adding a new feature to a big system, run the regression test suite as often as
possible. If a test fails, the bug is probably in the code you just changed.

# Performance improvements

- joblib parralel for program level runs
- numba improvements to targeted calculations (math decorator)


# Convocation

Organise Data all hands event for data uk. Fun fair theme with stalls. Increase team effectiveness. Outcome teams. Program increments.


# Other

- Data expo [presentation](https://drive.google.com/drive/folders/1VT4c2V9zxzlYeKot3dV6I4j-HhLwcE7f) of OneFlow
- PUG talk, python users group ML [presention](https://drive.google.com/drive/folders/1VT4c2V9zxzlYeKot3dV6I4j-HhLwcE7f)

 Approaches when developing a feature:
1. develop feature + unit tests
    then create intergation test
2. develop feature +unit test + create integration test ( Test-driven development 
    parallelize inegration test while developing a feature
    Not realying only on unit tests only
3. Github flow vs GitFlow we are moving from one to the other
4. Docusourus tool for static web pages
5. .env file lets you customize the individual working environment variables.
    Using environment variables  common practice during Development not a healthy 
    practice to use with Production.
    - in .enf file: add secrets, passwords, FEATURE FLAGS
    E.g if sharing codebase with the users we can have our own local .env where the     
    feature flag is turned on. Hoever in production(the users) do not have this feature
    turned on.
- PM stuff:
Follow Agile principles by using tools such as Jira and Confluence Enforcing the scrum rituals (sprint planning/retrospective, daily huddles, and customer demos). 

- Building system: infrastructure, storage, network protocols

---

**Behave** is a python library that enforces behaviour driven developement BDD which is an extension of TDD.

As we all know in TDD we write tests first and then   develop  individual functions in the code

BDD is the same but it acts on the level of features rather than functions.
So in BDD users and developers writetest cases in English so  that non-programmers can understand.
And only then developers start writing code

Involves users/BA-s and non-technical people can participate in the implementation process

Writes tests using normal language - allows users to write tests

FEATURES files are written by users

Advantages
Allow users to be in the developement process + instead of writing feature spec and requirements, they write test directly. 

Disadvantage is that it might take more BA-s time and given that tehy are already quite busy it might not be optimal

If we use behave it will probably worth it only for some integration tests
and do not use it for all unit tests which

---

Recoveries liquidation array = money we recover when our clients go in default

I compute RLA for each account using only matrix operations avoiding loops.  After making 100 runs each with 3k account the speed up is 46\%. $O(N^3)$ problem I did using one loop and for each iteration of the loop I use matrix operations.

```python
liquid_array_per_id =
            np.outer(co_pop1, padded_pop1_non_debt_sale)
            + np.outer(co_pop2, padded_pop2_non_debt_sale)
            + np.outer(co_pop3, padded_pop3_non_debt_sale)
            + window_multiply(debt_sale_prop * np.array(co_pop1),sale_price)
```
#### Time complexity

Assume we have `N` accounts, `S` statements and `CO` statements since charge off. The output contains for each account (`N` in total) and each statement (`S` in total) a liquidation array of size (`CO`). Hence the output is with dimension `N x S x CO` and just writing the output would require `O(N x S x CO)` runtime (i.e. that is the minimum runtime required).

Our RLA computation as we saw above calls two main functions which have non-constant run time - `np.outer(co_pop1, padded_pop1_non_debt_sale)` and `window_multiply(debt_sale_prop * np.array(co_pop1), sale_price)`

`co_pop1` is with dimension `S` and `padded_pop1_non_debt_sale` is with dimension `CO`,  hence  `np.outer(co_pop1, padded_pop1_non_debt_sale)` costs `O(S x CO)`.

`debt_sale_prop` is with dimension `CO` and hence `window_multiply(debt_sale_prop * np.array(co_pop1), sale_price)` costs `O(S x CO)`

Since we call these two functions **for each account**,  the total runtime is `O(N x S x CO)` which is the minimum achievable.
Thus, in terms of orders of growth, this is the fastest possible computation. Note the old RLA version was also `O(N x S x CO)`  but had a very large constant factor because of using multiple nested for loops.


# Key words

numba, jit decorator, dask, docosaurous, Agile, behave driven developement, cash flows, valuations, 