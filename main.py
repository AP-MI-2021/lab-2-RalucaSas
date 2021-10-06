"Problema 13"
def citire_grade():
    """
    citire numar de grade ce urmeaza sa fie convertite
    :return:
    """
    n = int(input("Cititi numarul de grade ce urmeaza sa fie convertite: "))
    return n


def transform_C(n):
    """
    se transforma numarul "n" de grade exprimate in Celsius in celelalte doua
    :param n:
    :return:
    """
    k = n * 1.000000 + 273.15
    f = n * 1.800000 + 32
    print(n, " grade C = ", k, " grade K si ", f, "grade F")


def transform_F(n):
    """
    se transforma numarul "n" de grade exprimate in Fahrenheit in celelalte doua
    :param n:
    :return:
    """
    c = (n - 32) / 1.8000
    k = (n - 32) / 1.8000 + 273.15
    print(n, "grade F =",c," grade C si ",k,"grade K")


def transform_K(n):
    """
    se transforma numarul "n" de grade exprimate in Kelvin in celelalte doua
    :param n:
    :return:
    """
    c = n - 273
    f = (n - 273.15) * 1.8000 + 32
    print(n," grade K =",f,"grade F si ",c,"grade C")

"Problema 14"
def get_cmmmc():
    a = int(input("Introduceti primul numar: "))
    b = int(input("Introduceti al doilea numar: "))
    c = a * b
    r = a % b

    while r != 0:
        d = c / b
        a = b
        b = r
        r = a % b

    print("CMMMC-ul numerelor date este ", d)


"Problema 1"
def is_prime(n):
  if n==2:
     return True
  if n<2:
     return False
  if n%2==0:
      return False
  for i in range(3,n//2+1,2):
      if n%i==0:
         return False
  return True


def get_largest_prime_below(n):
    if n==2:
        return "Nu exista un numar prim mai mic decat numarul introdus!"
    if n<2:
        return "Introduceti o valoare mai mare decat 2!"
    n=n-1
    while is_prime(n) is False:
        n-=1
    return n

def test_get_largest_prime_below():
    assert get_largest_prime_below(14)==13
    assert get_largest_prime_below(21)==19
    assert get_largest_prime_below(3)==2
test_get_largest_prime_below()



while True:
    print("1. Transformarea temperaturii date într-o scară data")
    print("2. Calculeaza CMMMC al n numere date.")
    print("3. Găsește ultimul număr prim mai mic decât un număr dat.")
    print("x. Iesire")

    optiune = input("Dati optiunea: ")
    if optiune == "1":
        """
        Se ruleaza programul ruland fiecare functie de mai sus
        :return:
        """
        n = citire_grade()
        transform_K(n)
        transform_C(n)
        transform_F(n)

    elif optiune == "2":
        a = int(input("Introduceti primul numar: "))
        b = int(input("Introduceti al doilea numar: "))
        print("CMMMC-ul numerelor date este ", b)

    elif optiune == "3":
        n = int(input("Introduceti un numar prim: "))
        is_prime(n)
        get_largest_prime_below(n)
        test_get_largest_prime_below()

    elif optiune == "x":
        break
    else:
        print("Optiune gresita! Reincercati!")
   def main():
  # interfata de tip consola aici

  if __name__ == '__main__':
  main()
