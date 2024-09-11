from gcd import gcd_eight
from twice_remove import remove_twice
from prime_number_gen import gen

def main():
    print("GCD for 8 and some number")
    print(gcd_eight(int(input("Input number for gcd: "))))
    print("Write a code that removes a vowel entered twice in the input string: ")
    print(remove_twice(input("Input string")))
    print("prime number generator")
    print(gen(int(input("Input your number: "))))
    
if  __name__ == "__main__":
    main()