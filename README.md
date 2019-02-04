
# Cryptography Systems

This code was written for my cryptography class as way to apply the things I learned.
The course itself was a math course, so we learned about the mathematical theory behind the systems such as 
rings, groups, modular arithmetic, etc. The code written here is somewhat specialized to the systems
we discussed in class and may have some variation from the "real" systems used in practice. 
This was for the learning experience (and to send encoded messages to my friends also in the class :) ) 

That said, this is not intended for copying for any other course. Plus, other courses may have variations.
If another student comes across this, I would highly recommend trying to implement these systems on your own.
It's very satisfying once you get it! 

I hard coded everything I needed for class, but I have changed it so that they can be used by the public through
command line arguments or imported into your own programs (essentially making this into a pseudolibrary of sorts)! 

## Contents
- [Crypto Systems in this folder](#crypto-Systems-in-this-folder)
- [Crypto System Descriptions](#crypto-system-description)
- [Usage/Documentation](#usage)

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

## Crypto System Description
This section will discuss the general idea about how the particular crypto system works

### GCD/Linear Combination 
The GCD is the largest number that evenly divides both numbers.
The Linear Combination is the values *u* and *v* such that GCD = u\*num1 + v\*num2


The calculation for the GCD is done using the [Euclidean Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm). And the Linear Combination is found using the [Extended Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm#Extended_Euclidean_algorithm). 

### Affine

### Affine Matrix

### Knapsack

### RSA

## Usage/Documentation
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

