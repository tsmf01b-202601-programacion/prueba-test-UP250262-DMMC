# EXAMEN DE RECUPERACIÓN - UNIDAD 2

# IMPORTANTE:
# 1. La salida debe ser ÚNICAMENTE el resultado. No agregues texto extra.
# 2. No modifiques las condiciones del menú (if/elif).
# 3. Usa solo una función print() por ejercicio.

problema = int(input("Número del problema (1-10): "))

if problema == 1:
    # Problema 1
    radio = 15
    pi = 3.1416
    area = pi * (radio ** 2)
    print("El area del circulo es:", area)

elif problema == 2:
    # Problema 2
    codigo = 88
    lote = "LoteB"
    clave_producto = f"prod-{codigo}-{lote.lower()}"
    print(clave_producto)

elif problema == 3:
    # Problema 3
    email = "usuario.upa.edu.mx"
    if "@" in email:
        print("El correo contiene @")
    else:
        print("El correo no contiene @")

elif problema == 4:
    # Problema 4: Convierte todo el texto a MAYÚSCULAS.
    aviso = "el examen termina pronto"
    # Tu código aquí

elif problema == 5:
    # Problema 5: Convierte el string "150.50" a float y luego a entero.
    # Imprime ambos resultados en una sola línea.
    dato = "150.50"
    flotante=float(dato)
    entero=int(flotante)
    print(flotante,entero)

elif problema == 6:
    # Problema 6: Conversión de Temperatura (Celsius a Fahrenheit).
    # C=30. Fórmula: F = (C * 1.8) + 32
    celsius = 30
    fahrenheit=(celsius*1.8)+32
    print("La temperatura en fahrenheit es:",fahrenheit)

elif problema == 7:
    # Problema 7: Extrae los primeros 5 caracteres de la cadena.
    frase = "Programación en Python"
    primeros=frase[:5]
    print(primeros)

elif problema == 8:
    # Problema 8: Calcula la Densidad de un objeto.
    # Masa: 500kg, Volumen: 2m^3. Fórmula: d = m / v
    m = 500
    v = 2
    densidad=(m)/(v)
    print("La densidad de el oibjeto es de:",densidad)

elif problema == 9:
    # Problema 9: Determina si un número es negativo.
    numero = -15
    if numero < 0:
        print("El numero es negativo")
    else:
        print("El numero es positivo")

elif problema == 10:
    # Problema 10: Calcula la Energía Potencial.
    # m=5kg, h=10m, g=9.81. Fórmula: Ep = m * g * h
    m = 5
    h = 10
    g = 9.81
    ep=(m)*(g)*(h)
    print("La energia potencial es:", ep)

else:
    print("Ingresa un número entre 1 y 10.")