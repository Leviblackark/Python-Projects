for fizz in range(1, 101):
    if fizz % 3 == 0 and fizz % 5 == 0:
        fizz = "FizzBuzz"
    elif fizz % 3 == 0:
        fizz = "Fizz"
    elif fizz % 5 == 0:
        fizz = "Buzz"
    print(fizz)