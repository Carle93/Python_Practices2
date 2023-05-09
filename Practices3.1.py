def fibonacci (n):
    if n == 0  or n == 1 :
        return (n)
    else :
        return fibonacci (n - 1) + fibonacci (n - 2)
    
print (fibonacci (2))

# Juego : MadLab F-string 
Adj = input("adjetivo:  ")
Verbo1 = input("Verbo:  ")
Verbo2 = input("Verbo:  ")
Sustantivo_plural = input ("sustantivo (plural):  ")

Mad_lab = f" Si me siento {Adj} , puede que tenga que {Verbo1}, para lograr completar la actividades que tengo que {Verbo2} para no procratisnar."
print (Mad_lab)