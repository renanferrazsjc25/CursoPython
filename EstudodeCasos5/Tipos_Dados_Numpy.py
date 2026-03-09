import numpy as np
# Numpy interfere o tipo de dado automaticamente

arr_inteiros = np.array([1, 2, 3])
print('Tipo de dado (inteiros):', arr_inteiros.dtype)

# Numpy interfere o tipo de dado automaticamente

arr_floats = np.array([1.0, 2.0, 3.0])
print('Tipo de dado (inteiros):', arr_floats.dtype)

# Mas podemos especificar o tipo de dado durante a criação do array

arr_float = np.array([1, 2, 3], dtype=np.float64)
print('Tipo de dado (float64):', arr_float.dtype)
print('Array_float:', arr_float)


# Conversao para int64

arr_int = arr_float.astype(np.int64)
print('Tipo convertido:', arr_int.dtype)
print('Array convertido:', arr_int)
