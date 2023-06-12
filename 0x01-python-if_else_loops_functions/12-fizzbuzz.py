#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print(f"Fizz", end=" ")
        elif i % 5 == 0:
            print(f"Buzz", end=" ")
        elif i % 5 == 0 and i % 3 == 0:
            print(f"FizzBuzz", end=" ")
<<<<<<< HEAD
        else:
            print(f"{i}", end=" ")
=======
	else:
	    print(f"{i}", end=" ")
>>>>>>> b25027e37b281be2cafa5a0ee823af01919dd7ce
