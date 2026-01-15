def subtrair(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os valores devem ser números inteiros ou decimais.")

    return a - b