def trapez(f, a, b, n):
    h = float(b-a) / n #se imparte intervalul in parti egale
    s = 0.0 
    s = s + (h * f(a)) #se calculeaza valoarea functiei de integrat la inceputul intervalului
                       #si se obtine primul 'trapez'
    for i in range(1,n):
        s = s + (2.0 * h * f(a+i*h)) #pentru restul intervalului se obtin restul trapezelor
    s = s + (h * f(b)) #se calculeaza valoarea functiei de integrat la sfarsitul intervalului
    return s/2 #deoarece intervalul este impartit uniform,
                #evaluam functia de mai putine ori
                #dar cu valoare dubla, deci rezultatul asteptat este jumatate
                #complexitatea este data de numarul de diviziuni al intervalului

print('Acest program aproximeaza integrala definita de la a la b din x^2 dupa variabila x')
a = input('a: ')
b = input('b: ')
n = input('numar de diviziuni a intervalului/precizie: ')


print(trapez(lambda x:x**2,a,b,n))

