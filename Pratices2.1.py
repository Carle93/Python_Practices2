#Ciclo con while 
x = 55
print (x)
while x < 80: 
    print (x)
    x += 3
    
def mostrar_mensaje ():
    print ("Hola mundo")
mostrar_mensaje ()

def mostrar_suma ( x, y) :
    print (x + y)
mostrar_suma (25,35)

print(mostrar_mensaje ())
print (mostrar_suma(50,5))

def mostrar_suma ( x, y) :
    return x + y
resultado = mostrar_suma (4,5)
print (resultado)