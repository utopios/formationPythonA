import ctypes


def use_c_module():
    c_module = ctypes.CDLL('./../projetc/lib1.so')
    # a = ctypes.c_float(10.0)
    # b = ctypes.c_float(30.0)
    # c = ctypes.c_float()
    # a = 10.0
    # b = 30.0
    # c_module.float_add.restype = ctypes.c_float
    # c_module.float_add.argtypes = [ctypes.c_float, ctypes.c_float]
    # result = c_module.float_add(a, b)
    # result2 = c_module.float_add(30.0, 20.0)
    # print(result)
    # print(result2)
    # c_module.float_add_ref(ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))
    # print(c.value)
    # n = 3
    # v1 = (ctypes.c_int * n) (1, 3, 5)
    # v2 = (ctypes.c_int * n) (3, 5, 6)
    # res = (ctypes.c_int * n)(0,0,0)
    # taille = ctypes.c_int(n)
    # c_module.add_int_vecteur(v1, v2, res, taille)
    # print(res[1])

    #Avec un pointeur
    c_module.fib.restype = ctypes.POINTER(ctypes.c_ulong)
    a = 10
    res = c_module.fib(ctypes.c_uint(a))
    for i in range(10):
        print(res[i])

    c_module.freeme(res)
    #ctypes.cdll.LoadLibrary('msvcrt').free(res)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    use_c_module()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
