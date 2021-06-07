## Assignment #4: Conditionals and iteration

### 2. Prime numbers

Write a Python program called [prime.py](prime.py) that takes a single integer *n*, provided by the user, and stores in the
variable result, `True` when it is a prime number, and `False` otherwise.

### 3. Fizz buzz

Write a Python program called [fizzbuzz.py] which “plays” a version of the known game *FizzBuzz*, over a sequence of integers from 0 to an integer n provided by the user.

The program should build a string result with each number in the sequence separated by a space. However:

- If the number is a multiple of 3, appends the word "Fizz" instead
- If the number is a multiple of 5, appends the word "Buzz" instead
- If the number is both a multiple of 3 and 5, nothing is done

For example, for `n=7`, the final string should be `1 2 Fizz 4 Buzz Fizz 7`

### 4. Triangles

Write a program called [triangle.py](triangle.py) that checks if a triangle is equilateral, isosceles or scalene, with the 3 sides provided by the user, each one in a different `input()` statement.

The variable result is computed accordingly (`Equilateral`, `Isosceles`, `Scalene`), and must be equal to `Not a triangle`, when the sides given do not form a valid triangle.

### 5. Joining 2 numbers

Write a program called [concatenate.py](concatenate.py) that, given two numbers *n1* and *n2* provided by the user (each one in a
different `input()` statement) produces a new number result by joining both of them, in the order they are given.

For example, if the numbers given are `n1=23` and `n2=567`, the resulting number `result=23567`.

You are not allowed to use to use string manipulation (for example string concatenation).

### 6. Palindrome integers

Write a program called [capicua.py](capicua.py) that, given an integer in the variable *num*, provided by the user, computes its
reverse (the number with the digits by the reverse order).

The variable result is a string computed as:

-  `<num> is a palindrome.`, when the original number and its reverse are equal
-  `<num> is not a palindrome.`, otherwise
  
You are not allowed to use string manipulation (for example string concatenation).
