def simpson(f, a, b, n):
    if n % 2:
        n = n + 1 # fortam numarul de diviziuni sa fie par
    h = float(b-a)/n
    s = f(a) + f(b)
    for i in range(1, n, 2):
        s = s + 4*f(a + i * h)
    for i in range(2, n-1, 2):
        s = s + 2*f(a + i * h)
    return s * h / 3











a = input('start: ')
b = input('stop: ')
n = input('precizie/nr diviziuni(daca nu este numar par, ii va fi adunat 1): ')
print(simpson(lambda x:x**2, a, b, n))
        
