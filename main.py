from gcd import gcd_eight, gcd_eight_2
from twice_remove import remove_twice
from prime_number_gen import gen
from matrix import only_complex
from frac import Frac
import fibonachi
from descr import Descr
import vect
import determinant

def main():
    print("GCD for 8 and some number")
    print(gcd_eight(int(input("Input number for gcd: "))))
    print("Write a code that removes a vowel entered twice in the input string: ")
    print(remove_twice(input("Input string")))
    print("prime number generator")
    print(gen(int(input("Input your number: "))))
    print(only_complex([1, 2, 3.0, True, 1+2j], [0+0j,1+6j,3,2,False]))
    print([i for i in fibonachi.FibSums(int(input("Input N for Fibonachi sums: ")))])
    print(fibonachi.find_in_fibonachi(int(input("enter your number"))))
    a = Frac(-1,-3)
    print("Sum 1/3 of -1/2")
    a.sum(Frac(1,-2))
    a.print_me()
    print("Multiply of result and 20/100")
    a.multiply(Frac(20,100))
    a.print_me()
    print("Mne len' perevodit' poetomu skaju chto eto obrashenie")
    print(a.obrash())
    b = Descr(((0,0),(0,2),(2,2),(2,0)))
    c = Descr(((0,0),(0,2),(2,2),(2,0)))
    print(f"b = {b.coord}")
    print(f"c = {c.coord}")
    print("Is the descr equal? (b and c)", b.is_equal(c))
    d = Descr(((0,0),(0,1),(1,1),(1,0)))
    print(f"c = {d.coord}")
    print("Is the descr similar? (b and d)", b.is_similar(d))
    print(f"The multiply of vector (1,2,3) and (4,5,6): {vect.multiply((1,2,3),(4,5,6))}")
    print()
    print(determinant.calculate_determinant([[0,2,3],
                                             [1,5,6],
                                             [7,8,9]]))
    print(gcd_eight_2(int(input())))

if  __name__ == "__main__":
    main()