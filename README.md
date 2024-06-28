# PythonLearning

A collection of simple python projects.

## anagramsearch.py

Program that searches a file for anagrams of a given word, printing the results in alphabetical order.

## anagramsets.py

Program that asks the user to enter a word length and a filename. The program will search the *EnglishWords.txt* file for sets of words that are that length and are anagrams of each other, and will write the results to a file with the given filename. Duplicates are not allowed and words are alphabetical by first word. These words are of arbitrary size, and not just pairs.

## breakup.py

A program that accepts a sentence as input and that outputs it as a comma-separated list of lowercase words with a full-stop at the end.

## bulletin.py

A simple BBS (Bulletin Board System) that stores written messages, files (text) and can display them.

```
Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:
>>>
```

## calendar_month.py

An attempt at creating a calendar generator. Given a month and year, generate the calendar for that month.

## column.py

A column implementation of *row.py*.

## convert.py

Converts a given 24 hour short-format time into a long format 12 hour time.

```
Enter the date and time (yyyy-mm-dd hh:mm):
>>> 2021-04-09 04:33
4:33 am on the 9th of April '21
```

## cupcake.py

Determines whether food is safe to eat.

A simple model of an expert system -  simple variant of artificial intelligence. An introduction to decision trees.

## cylinder.py

Calculates the volume of a cylinder given integer values for its diameter and height.

## encrypt.py

Program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a).

## energy.py

Calculates energy based on the equation...

$E = mc^2$

## extract.py

Converts string data from a weather sensor into weather data using functions.

```
Data is given as...
... BEGIN temp_press:Xcoordinate,Ycoordinate emanetiS END ... 

The program converts to...
Location: Sitename 
Coordinates: Ycoordinate Xcoordinate 
Temperature: temp C 
Pressure: press hPa 
```

## grid.py

Generates a 6$\times$7 grid containing a sequence of numbers - the beginning of which, is specified by the user.

## gridio.py

Allows a user to input integer values and query a 2-dimensional array of size 9$\times$9. Given an xy coordinate pair, returns the value at that position in the grid.

## histogram.py

Takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT:
    • fail < 50%
    • 50% ≤ 3rd < 60%
    • 60% ≤ lower 2nd < 70%
    • 70% ≤ upper 2nd < 75%
    • 75% ≤ first

```
Enter a space-separated list of marks:
>>> 88 90 75 76 92 78 98 100 81 70 70 73 74 72 73 72 66 67 60 63 65 62 64 60 52 50 55 56 54 56 57 58 59 50 42 40 40 34 23 43 42 32
1 |XXXXXXXXX
2+|XXXXXXX
2-|XXXXXXXX
3 |XXXXXXXXXX
F |XXXXXXXX
```

## leapYear.py

Determines whether a given year is a leap year.

Leap condition:

- Must be divisible by 400 or...

- Must be divisble by 4 but not by 100.

## mymath.py

Program that calculates the number of k-permutations oh n terms.

## numberutil.py

Used in *testnumberutil.py*.

## pairs.py

That uses a recursive function to count the number of pairs of consecutive characters in a string. Pairs of characters cannot overlap.

## palindrome.py

Used in *testpalindrome.py*.

## palindromeprimes.py

Program that uses recursive functions to find all palindromic primes between two integers N, M, supplied as input. (start and end points are included).

## perfect.py

Determines whether a given number is a *perfect number*.

Perfect number...

- Positive integer

- Equal to the sum of its proper divisors.

## pig_latin.py

Accepts a sentence and converts it to *Pig Latin*.

## printmonth.py

Given a month name and a start day - produces a calendar for that month in a 6$\times$7 grid. Ignores leap years and assumes February has 28 days.

```
Enter the name of a month (e.g. January, ..., December):
>>> July
Enter the start day (1 for Monday, ..., 7 for Sunday):
>>> 2
July
Mo Tu We Th Fr Sa Su
   1  2  3  4  5  6 
 7  8  9 10 11 12 13 
14 15 16 17 18 19 20 
21 22 23 24 25 26 27 
28 29 30 31
```

## rabbit.py

ASCII Art.

## references.py

A text formatting program to manipulate given references into standardised ones.

## row.py

An introduction to text formatting. Prints a sequence of 7 numbers starting at the user-specified value. Numbers are printed right-justified with a field width of 2.

## secret_2.py

A classic guess the number program.

The user guesses numbers guided by prompts for each in correct guess which converges to a secret number.

## spam.py

Generates a personalised spam message using a template.

## testnumberutil.py

A *doctest* file to test statement and path coverage of *numberutil.py*.

## testpalindrome.py

Contains a set of tests to achieve path coverage in *palindrome.py*.

## time.py

Validates time entrys.

## tracer.py

Program that accepts a python file as input and...

- Adds trace statements at the beginning of each function.

- Removes trace statements if the file supplied contains any.

## triangle.py

Calculates the area of a triangle - given the 3 lengths of sides - using *Heron's Formula*.

**Heron's Formula**

$Area = \sqrt {s \times (s-a)\times(s-b) \times (s-c)}$

$Where...~~s = \frac{a+b+c}{2}$

## vectormath.py

Performs basic vector calculations in 2 dimensions.

Supported calculations

- Obtain magnitude.

- Vector addition

- Scalar Multiply

- Dot product

- Cross product
