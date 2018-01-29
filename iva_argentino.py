#Este codigo lo hice para probar algunos conceptos que enseñaste,
#pero es altamente inutil lel 

print("Calculador de IVA Argentino")

monto = input("¿Cual es el dinero total incluyendo las tasas?")

def iva (total):
    result = (21 *  int(total) / 100)
    return result

iva_result = iva(monto)

print("De $", monto, ", $", iva_result, " son de impuestos, k wen pais...")





    