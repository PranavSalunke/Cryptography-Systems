
# Cryptography Systems

This code was written for my cryptography class as way to apply the things I learned.
The course itself was a math course, so we learned about the mathematical theory behind the systems such as 
rings, groups, modular arithmetic, etc. The code written here is somewhat specialized to the systems
we discussed in class and may have some variation from the "real" systems used in practice. 
This was for the learning experience (and to send encoded messages to my friends also in the class :) ) 

That said, this is not intended for copying for any other course. Plus, other courses may have variations.
If another student comes across this, I would highly recommend trying to implement these systems on your own.
It's very satisfying once you get it! 

I hard coded everything I needed for class, but I wanted to share this with the public. I found these programs really cool and fun!
So for it to be more useful, I have changed it so that they can be used by the public (you!) through command line arguments or imported into your own programs (essentially making this into a pseudo-library of sorts)! 

All the details of each crypto system, the usage for my programs, and other info can be found below.

I hope you have as much fun playing with this as much as I had making these!

## Contents
- [Crypto Systems in this folder](#crypto-systems-in-this-folder)
- [Other Programs in this folder](#other-programs-in-this-folder)
- [Crypto System Descriptions](#crypto-system-description)
- [Other Program Descriptions](#other-program-description)
- [Usage for command line](#usage-for-command-line)
- [Documentation for use in external programs](#documentation-for-use-in-external-programs)
- [The Example Program](#the-example-program)
- [Bonus Cipher](#bonus-cipher)

## Crypto Systems in this folder
- Affine
    - affine.py
- Affine Matrix
    - affineMatrix.py
- Knapsack
    - knapsack.py
- RSA
    - RSA.py

## Other Programs in this folder
- GCD/Linear Combination
    - gcdLC.py
- Frequency Analysis
    - frequencyAnalysis.py
- Miscellaneous Tools
    - miscTools.py

## Crypto System description
This section will discuss the general idea about how the particular crypto system works

### Affine
key (a,b) gcd(a,b) = 1 and b = length alphabet

### Affine Matrix

### Knapsack

### RSA

## Other Program description

### GCD/Linear Combination 
The GCD is the largest number that evenly divides both numbers.
The Linear Combination is the values *u* and *v* such that GCD = u\*num1 + v\*num2


The calculation for the GCD is done using the [Euclidean Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm). And the Linear Combination is found using the [Extended Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm#Extended_Euclidean_algorithm). 

### Frequency Analysis
Frequency Analysis is the method of analyzing a encoded message with the frequency of the appearance of letters. 
Every language uses certain letters over others. The ordering for English letters can be found [here](https://en.wikipedia.org/w/index.php?title=Letter_frequency#Relative_frequencies_of_letters_in_the_English_language). It starts with `_ETAO..` where `_` is actually a space.

The idea is that in a substitution cypher such as the affine system, the distribution of letters should be the same. So if it is found that `G` is used the most often, it is most likely a space and if `M` comes up the second most, it is probably an `E`. This goes on until everything is re-substituted. Usually this does not reveal the entire message, but it can help when trying to crack it. 

One large set back is there are letters with the same frequency. For instance if `M` and `E` both appeared the most often, we wouldn't know which one to replace with a space. It comes down to guesswork again. In the program I wrote, there is a mode called `humanAssist` when setting the order in which letters appear in the message. More information about it will be in the [Usage for command line](#usage-for-command-line) section below.

More can be read about Frequency Analysis [here](https://en.wikipedia.org/wiki/Frequency_analysis)
### Miscellaneous Tools
These are tools that don't fit in with any particular crypto system. These are not intended for use in the command line. Please refer to to the documentation in the [Documentation for use in external programs](#documentation-for-use-in-external-programs) section. 

## Usage for command line
These programs are created for Python 3 and are intended to be used via the command line
You may me able to run python 3 with the command `python3` or `py -3` on Windows. I will use `py -3` in the examples.
To download Python and view its documentation, refer to [Python's Official Site](https://www.python.org/)
Each of the systems are self contained in their files and have various arguments. The details for these are below. 

Additionally, any of these can be imported with the `import` keyword. The internal functions can be use in your own scripts.

### Affine

### Affine Matrix

### Knapsack

### RSA

### GCD/Linear Combination 
This program will give you the Greatest Common Divisor (GCD) or the Linear Combination or both of two numbers  (num1 and num2
Help message (`py -3 .\gcdLC.py -h`):
```
usage: gcdLC.py [-h] [-f {gcd,lincomb,both}] [-showGcdWork] number1 number2

Program to find the GCD and/or linear combination of two integers using the
euclidean algorithm

positional arguments:
  number1               The first number
  number2               The second number

optional arguments:
  -h, --help            show this help message and exit
  -f {gcd,lincomb,both}, --function {gcd,lincomb,both}
                        If you want the GCD of the two integers or the linear
                        combination or both. Choices: "gcd", "lincomb" "both"
                        (default)
  -showGcdWork          Include this flag to show the work in finding the GCD.
```

Examples:
Just two numbers. This will return the GCD and the Linear Combination of the two numbers
    `py -3 .\gcdLC.py 432 32`

This will return just the GCD of the two numbers. Not specifying any option with the `-f` option will default to the `both` option.
    `py -3 .\gcdLC.py -f gcd 24425 125`

This will show the work to calculate the GCD
    `py -3 .\gcdLC.py -showGcdWork  223 2353`

### Frequency Analysis

### Miscellaneous Tools
This file is not intended for use via the command line. To use the methods, import it into your own project `import miscTools` and refer to to the documentation in the [Documentation for use in external programs](#documentation-for-use-in-external-programs) section. 

## Documentation for use in external programs

All the files have been created to be used in the command line by the above usage or to be imported into your own programs.
Just import the file (the file must be in the same folder) at the top of your python file. For example `import gcdLc`.
Now you have access to the programs methods. Any methods that should not be used throw errors. 

Below are the methods that are accessible, their arguments, what they do, and their return values.

### Affine

### Affine Matrix

### Knapsack

### RSA

### GCD/Linear Combination 
```
gcdLC.py
```

```
findGCD(num1, num2, showGcdWork=False)
```
Takes two integers and returns their Greatest Common Divisor (GCD).
`num1` first integer
`num2` second integer
`showGcdWork` To show the work for finding the GCD or not. If true, prints out to standard output. Default is False.

Example:

```
>>> import gcdLC
>>> x = gcdLC.findGCD(15,100,True)
100 = 6 * 15 + 10
15 = 1 * 10 + 5
10 = 2 * 5 + 0
>>> x
5
>>> y = gcdLC.findGCD(15,100) #usually what you would want to do
>>> y
5
```

```
linearCombination(num1, num2)
```
Takes two integers and finds their linear combination.
`num1` first integer
`num2` second integer

note: `a` is the larger of num1, num2
returns the tuple (gcd, a, b, u, v,)

`u` and `v` as such that
`gcd = u*a + v*b`

Example

```
>>> y = gcdLC.linearCombination(15,100)
>>> y
(5, 100, 15, -1, 7)
>>> 100*-1 + 7*15
5
```

### Frequency Analysis

### Miscellaneous Tools
```
miscTools.py
```

```
bruteForceModInverse(a, m)
```


Takes two integers and returns the modular inverse of `a mod m`. Returns `None` if the modular inverse does not exist. 
`a` integer
`m` modulo (integer)

The modular inverse of an integer , `a`, is an integer `b` such that  `a*b` is congruent to `1 mod m`

This function uses the brute force method of finding the inverse by exhaustively searching for an inverse, `i`,  from `0` to `m` and checking if the `(a*i) mod m = 1`. This function can be very slow for a larger value of `m`. This function was built more for checking the correctness of `modInverse` and for learning.

For practical uses, `modInverse` should be used instead. 

Example:


```
>>> import miscTools
>>> miscTools.bruteForceModInverse(23,840)
767
>>> (767*23)%840 # checking if this is 1
1
```

```
modInverse(a, m)
```
Takes two integers and returns the modular inverse of `a mod m`. Returns `None` if the modular inverse does not exist.
`a` integer
`m` modulo (integer)

Same as `bruteForceModInverse` but it uses the Euclidean Algorithm to find the modular inverse via the `linearCombination` from `gcdLC`.
This function is much faster. 

Example:

```
>>> import miscTools
>>> miscTools.modInverse(23,840)
767
```

```
numbersToLetters(alphabet, numberEncoding)
```

`alphabet` string of the alphabet used for the encoded and plain text messages 
`numberEncoding` string of numbers separated by spaces

All the crypto systems that I implemented assume the encoded message comes in as a string of letters (ex. `HELLO THERE`). The characters depend on the alphabet. For the example the alphabet is `ABCDEFGHIJKLMNOPQRSTUVWXYZ ` with a space after `Z` to create an alphabet of 27 characters. 

However, the numbers can be refereed to by their index as well. For instance `A=0`, `B=1` ...

You may be given the encoded or decoded string as a string of numbers instead and you need to convert it to the string of characters that the programs expect. (ex. `HELLO THERE` could be given as `7 4 11 11 14 26 19 7 4 17 4`)

Returns a string of letters.

Example:

```
>>> import miscTools
>>> msg = "7 4 11 11 14 26 7 14 22 26 0 17 4 26 24 14 20"
>>> miscTools.numbersToLetters(alph,msg)
'HELLO HOW ARE YOU'
```

```
lettersToNumbers(alphabet, message)
```

`alphabet` string of the alphabet used for the encoded and plain text messages 
`numberEncoding` string of letters in the alphabet

The reverse of numbersToLetters. If you want to convert a string of letters to their numeric value.

Returns a string of numbers separated by a space.

Example:

```
>>> import miscTools
>>> alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
>>> msg = "HELLO HOW ARE YOU"
>>> miscTools.lettersToNumbers(alph,msg)
'7 4 11 11 14 26 7 14 22 26 0 17 4 26 24 14 20'
```

## The Example Program
I created an example program `exampleProgram.py` showcasing how these crypto systems can be used in your own programs! 
Just run it in the command line with python 3 `py -3 exampleProgram.py` or `python3 exampleProgram.py`.
The output will be printed out to the console. 

If you like, take a look at how it works and play around with it! 

## Bonus Cipher

All the above Crypto Systems are pretty complex. But I have been interested in such things even years before taking the class that inspired me to make this whole project. [I made one many years ago](https://github.com/PranavSalunke/FirstPythonProjects/blob/master/my%20code/MY%20code.pyw) and it wasn't very well implemented, nor was it very secure. But I was very proud of it when I made it. Younger me would be ecstatic to know that I have grown as a programmer and computer scientist and that I was able to produce a project as detailed and involved as this! 