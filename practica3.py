
# 1.- Definir una funcion que reciba como parametro una lista de strings de ciudades
#   y retorne la misma lista pero con los elementos en mayusculas.
"""
def Mayus_lis(ciudades):
    ciudadMays = []
    for ciudad in ciudades:
        ciudadMays.append(ciudad.upper())
    return ciudadMays

ciudades = ["Cuapiaxtla", "Tecamachalco", "Tepeaca"]
ciudades = Mayus_lis(ciudades)
print(f"Las cuidades en mayusculas son: \n \t{ciudades}")


# 2.- Agregar las anotaciones de tipo a la funcion antes declarada.
from typing import Sequence, Tuple

def Mayus_lis(ciudades: Tuple[str, ...]) -> Sequence:
    ciudadMays = []
    for ciudad in ciudades:
        ciudadMays.append(ciudad.upper())
    return ciudadMays

ciudades = ["Mexico", "Peru", "España"]
ciudades = Mayus_lis(ciudades)
print(f"Las cuidades en mayusculas son: \n \t{ciudades}")


# 3.- deninir la siguiente lista -> nombres = ["maria", "juan", "pedro"]
#   Usando recursion, definir una funcion que imprima un mensaje de bienvenida
#   para cada uno de los nombres de la lista.
# Tip: El caso base es cuando tenemos una lista vacia(terminamos la recursion aqui) 
def mensaje(nombres):
    if len(nombres) == 0:
        return
    print(f"\tBienvenido {nombres[0]}")
    mensaje(nombres[1:])

nombres = ["maria", "juan", "pedro"]
mensaje(nombres)


# 4.- Definir la siguiente lista:
# dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
# Usar la funcion lambda y la funcion map() para truncar los elementos a los primeros
#   5 caracteres. Imprimir en consola el resultado
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
dias_semana = list(
    map(lambda dia: dia[:5], dias_semana)
)
for d in dias_semana:
    print(f"\t {d}")


# 5.- Usando la lista del ejercicio anterior.
#   Usar la funcion lambda y la funcion filter para "filtrar" todos los elementos
#   que contengan el caracter "a" en el elemento(dia de la semana).
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
dias_semana = list(
    filter(lambda dia: "a" in dia, dias_semana)
)
for d in dias_semana:
    print(f"\t {d}")

# 6.- Realizar el ejercicio 4 pero usar listas de comprension en lugar de lambdas.
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
dias_semana = [dia[:5] for dia in dias_semana]
for d in dias_semana:
    print(f"\t {d}")



# 7.- Realizar el ejercicio 5 pero usar listas de comprension en lugar de lambdas.
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
dias_semana = [dia for dia in dias_semana if "a" in dia]
for d in dias_semana:
    print(f"\t {d}")



# 8.- definir una funcion "suma(a, b)" que reciba dos parametros de tipo entero y retorne la suma
#   de estos dos numeros. Definir un decorador "@doble" para que la funcion retorne
#   el doble del resultado, es decir, suma(3, 5) debera retornar un valor de 16( (3+5)*2 )
def doble(func):
    def wrapper(*args):
        res = func(*args)
        return (res * 2)

    return wrapper
@doble
def suma(a: int, b: int):
    return (a + b)
print(f"La suma de dos enteros, el resultado al doble es: {suma(2, 4)}")

"""
from typing import Union
import sys


def get_maximum_crossing_subarray(A: tuple, low: int, mid: int, high: int) -> Union[int, int, float]:
    """
    Return the contiguos sub array using a midpoint to saparate A into 2 subarrays.
    :param A: (tuple) array where we search the max sub array.
    :param low: (int) the low index of A where we must search.
    :param mid: (int) The mid of the array.
    :param high: (int) The high index of A where we must search.
    :return: (tuple) tuple where 3 values, the first 2 values are the
    low and high index of the maximum sub array found and the 3th value is 
    the sum maximum sub array sum.
    :rtype: Union(int, int, float)
    """
    left_sum = -sys.maxsize
    sum = 0
    index_left = mid
    for i in range(mid, low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            index_left = i

    right_sum = -sys.maxsize
    sum = 0
    index_right = mid
    for j in range(mid + 1, high + 1, 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            index_right = j

    return (index_left, index_right, left_sum + right_sum)


def get_maximum_subarray(A: tuple, low: int, high: int) -> Union[int, int, float]:
    """
    Return the contiguos sub array of A whose value
    have the largest sum. This function apply the method
    divide and conquer(recursive function).
    :param A: List of integers.
    :param low: The lowest index of A.
    :param high: The highest index of A.
    :return: (tuple) tuple with the low and high index of the new sub array
    that containt the largest sum. for example for the array A=[1, 3, -5, 6, 9]
    the tuple returned will be (3, 4, 15) where 3 and 4 and the index of the subarray
    A[3:4] and the 15 is the sum of the subarray A[3:4].
    Notice that the array A must be a power size of 2 to ensure that n/2 is an integer.
    :rtype: Union[int, int, float]
    """
    id_left, id_right, suma = get_maximum_crossing_subarray(A, low, 2, high)
    return int((id_right+1)/2), (id_right+1), suma
    #pass # <here the definition of the function.>



if __name__ == "__main__":
    """
    all the list the first element is the index 0 and the last
    index is the A.length - 1
    """
    A = [1, 3, -3, -4, -3, 3, 3, 4]
    #A = [1, 3, -5, 6, 9]
    low_index, high_index = 0, len(A) -1
    idx_low, idx_high, sum = get_maximum_subarray(A, low_index, high_index)
    max_subarray = A[idx_low:idx_high]
    print(f"the maximum sub array of {A} is {max_subarray} with the idx [{idx_low}:{idx_high}] and the sum is {sum}" )