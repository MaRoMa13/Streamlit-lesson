import math

def is_prime(numero):
    """Verifica si un número es primo"""

    if numero <= 1:
        return False
    for i in range(2,int(math.sqrt(numero) + 1)):
        if numero % i == 0:
            return False
    return True

def main():

    """tiene toda la lógica principal"""

    for i in range(100):
        if is_prime(i):
            print (i, end=' ')
    print()

if __name__ == '__main__':
    main()
