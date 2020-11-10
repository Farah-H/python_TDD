# Test Driven Development (TDD)
Is the method of creating tests, then building code which passes the tests, rather than building code and then tests.

![TDD](TDD)

## Why would we use TDD? 
- We know the requirements
- we can make tests based on requirements so any code produced must meet that criteria 
- it's a good way to define acceptance criteria 
- ONE MISTAKE can lead to massive consequences, esp when life is involved. TDD helps us minimise the risk of seding product to production

## Python has several modules that we can use
- pytest
- unitest

## Steps:
- create a file to write our tests 
- we will run the test they will all fail
- create a file to write our code 
- we will refactor and add the code to pass the tests

## Naming Convention for TDD
- file name e.g `simple_calc`
- test file file name e.g `test_simple_calc`

## Steps:
1. Install pytest using the command `pip install pytest` in your terminal