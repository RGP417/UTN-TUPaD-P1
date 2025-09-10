#Ejercicio 6: Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#	55% del promedio de sus tres calificaciones parciales.
#	30% de la calificación del examen final.
#	15% de la calificación de un trabajo final.

#p1 = float(input('ingrese su calificación del primer parcial: '))
#p2 = float(input('ingrese su calificación del segundo parcial: '))
#p3 = float(input('ingrese su calificación del tercer parcial: '))
#examen = float(input('ingrese la calificación de su examen final: '))
#trabajo = float(input('ingrese la calificación de su trabajo final: '))
#calificacion_final = (((p1+p2+p3)/3)*0.55)+(examen*0.30)+(trabajo*0.15)
#print('su calificación final es de: ' +str(calificacion_final))

#Ejercicio 7: Conversión de divisas
#Un programa que lea un monto en dólares y lo convierta a pesos colombianos, argentinos y #euros usando tasas de cambio fijas definidas en el código.

#dolares=float(input('Bienvenido al banco /n ingrese la cantidad de dólares que quiera cambiar y le mostraremos las ofertas por otras monedas '))
#pes_col_cambio=1100.0
#pes_argentino_cambio = 1300.0
#eur_cambio = 0.9
#print('Podemos ofrecerle los siguientes montos por su dinero: \npesos colombianos: ' + str(dolares*pes_col_cambio) + '\npesos argentinos: ' + str(dolares*pes_argentino_cambio) + '\nEuros: '+ str(dolares*eur_cambio))

#Ejercicio 8: Viaje en auto
#Un auto consume 8 litros cada 100 km. El usuario ingresa la distancia en km y el precio de la gasolina por litro.
#El programa debe calcular:

#cuántos litros se necesitan,

#cuánto costará el viaje,

#y cuántas horas tardará si la velocidad promedio es de 90 km/h.


#kilometros = float(input('ingrese la cantidad de Kilómetros que se planea viajar: '))
#precio = float(input('ingrese el valor de la gasolina por litro: '))
#litros = kilometros*0.08
#valor_viaje = precio*litros
#print('se consumirán ' + str(litros)+ 'litros de combustible y tendrán un costo de: ' + str#(valor_viaje)+'.')

#Ejercicio 9: Préstamo bancario
#Un cliente solicita un préstamo que deberá pagar en 12 meses con interés fijo mensual del 2%.
#El usuario ingresa el monto solicitado, y el programa debe calcular:

#el monto total a devolver,

#el valor de cada cuota mensual.

prestamo = float(input('Bienvenido al banco ¿cuanto desea que le prestemos? (risa malvada)'))
contador = 1
total= 0
mes = prestamo/12
while contador <=12:
    mes = mes + (mes*0.2)
    print('En su cuota n° '+str(contador)+' usted deberá abonar '+str(round(mes, 2)))
    total = total + mes
    contador += 1
print('En total deberá abonar: '+ str(round(total,2)))

