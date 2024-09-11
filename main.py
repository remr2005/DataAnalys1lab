import gcd
from twice_remove import remove_twice

def main():
    print("GCD for 8 and some number")
    print(gcd.gcd_eight(int(input("Input number for gcd"))))
    print("Write a code that removes a vowel entered twice in the input string.")
    print(remove_twice(input("Input string")))
    
if  __name__ == "__main__":
    main()