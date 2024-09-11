from gcd import gcd_eight
from twice_remove import remove_twice
from prime_number_gen import gen
from matrix import only_complex
from frac import Frac
import fibonachi

def main():
    # print("GCD for 8 and some number")
    # print(gcd_eight(int(input("Input number for gcd: "))))
    # print("Write a code that removes a vowel entered twice in the input string: ")
    # print(remove_twice(input("Input string")))
    # print("prime number generator")
    # print(gen(int(input("Input your number: "))))
    # print(only_complex([1, 2, 3.0, True, 1+2j], [0+0j,1+6j,3,2,False]))
    # print([i for i in fibonachi.FibSums(int(input("Input N for Fibonachi sums: ")))])
    # print(fibonachi.find_in_fibonachi(int(input("enter your number"))))
    a = Frac(-1,-3)
    print("Sum 1/3 of -1/2")
    a.sum(Frac(1,-2))
    a.print_me()
    print("Multiply of result and 20/100")
    a.multiply(Frac(20,100))
    a.print_me()
    print("Mne len' perevodit' poetomu skaju chto eto obrashenie")
    print(a.obrash())

if  __name__ == "__main__":
    main()