nombre_apell = input('ingrese su nombre y apellido separados: ')
edad = int(input('Ingrese su edad: '))
promedio = float(input('ingrese su promedio: '))
ingresos_fam = float(input('ingrese sus ingresos familiares: '))

if edad >= 18 and edad <=100:
    if promedio>=6 and promedio<=10:
        if ingresos_fam <300000 and ingresos_fam>0:
            print(f'Beca completa')
        elif ingresos_fam >=300000 and ingresos_fam<=600000:
            print(f'Media Beca')
        elif ingresos_fam<0:
            print(f'Debió colocar la verdad')
        else:
            print(f'Rechazado')
    elif promedio <0 or promedio > 10:
        print(f'Debió colocar la verdad')
    else: 
        print(f'rechazado')
else:
    print('Es esa su edad realmente?')