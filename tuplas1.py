#Las tuplas se definen una sola vez y son inmutables
t=('Alvaro','Chirou','Estudiantes',10,[1,2,8],10,-80)

#Podemos imprimir un elemento segun su posicion
print(t[0])
print(t[1])

#Podemos conocer la longitud (cantidad de elementos que tiene)
print(len(t))

#Podemos conocer la ubicación de algún elemento buscado, por ejemplo
# Quiero saber en que posición se encuentra el texto 'Estudiantes'
print(t.index('Estudiantes'))

#Puede contar las veces que aparece un elemento
#Por ejemplo, cuantas veces aparece el número 10
print(t.count(10))

#No funciona append en las tuplas
t.append('a')