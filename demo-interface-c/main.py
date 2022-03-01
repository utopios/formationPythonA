import ctypes


def use_c_module():
    c_module = ctypes.CDLL('./../projetc/lib1.so')
    a = ctypes.c_float(10.0)
    b = ctypes.c_float(30.0)
    c = ctypes.c_float()
    # a = 10.0
    # b = 30.0
    # c_module.float_add.restype = ctypes.c_float
    # c_module.float_add.argtypes = [ctypes.c_float, ctypes.c_float]
    # result = c_module.float_add(a, b)
    # result2 = c_module.float_add(30.0, 20.0)
    # print(result)
    # print(result2)
    c_module.float_add_ref(ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))
    print(c.value)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    use_c_module()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
