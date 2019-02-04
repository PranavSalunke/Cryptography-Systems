
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
- [Crypto Systems in this folder](#crypto-Systems-in-this-folder)
- [Crypto System Descriptions](#crypto-system-description)
- [Usage for command line](#usage-for-command-line)
- [Documentation for use in external programs](#documentation-for-use-in-external-programs)
- [The Example Program](#the-example-program)

## Crypto Systems in this folder
- GCD/Linear Combination (not really a crypto system)
    - gcdLC.py
- Affine
    - affine.py
- Affine Matrix
    - affineMatrix.py
- Knapsack
    - knapsack.py
- RSA
    - RSA.py

## Crypto System description
This section will discuss the general idea about how the particular crypto system works

### GCD/Linear Combination 
The GCD is the largest number that evenly divides both numbers.
The Linear Combination is the values *u* and *v* such that GCD = u\*num1 + v\*num2


The calculation for the GCD is done using the [Euclidean Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm). And the Linear Combination is found using the [Extended Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm#Extended_Euclidean_algorithm). 

### Affine

### Affine Matrix

### Knapsack

### RSA

## Usage for command line
These programs are created for Python 3 and are intended to be used via the command line
You may me able to run python 3 with the command `python3` or `py -3` on Windows. I will use `py -3` in the examples.
To download Python and view its documentation, refer to [Python's Official Site](https://www.python.org/)
Each of the systems are self contained in their files and have various arguments. The details for these are below. 

Additionally, any of these can be imported with the `import` keyword. The internal functions can be use in your own scripts.
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
### Affine

### Affine Matrix

### Knapsack

### RSA


## Documentation for use in external programs

All the files have been created to be used in the command line by the above usage or to be imported into your own programs.
Just import the file (the file must be in the same folder) at the top of your python file. For example `import gcdLc`.
Now you have access to the programs methods. Any methods that should not be used throw errors. 

Below are the methods that are accessible, their arguments, what they do, and their return values.

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

### Affine

### Affine Matrix

### Knapsack

### RSA

## The Example Program
I created an example program `exampleProgram.py` showcasing how these crypto systems can be used in your own programs! 
Just run it in the command line with python 3 `py -3 exampleProgram.py` or `python3 exampleProgram.py`.
The output will be printed out to the console. 

If you like, take a look at how it works and play around with it! 