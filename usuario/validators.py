def rut_valido(rut, dv):
    rut = rut.replace('.', '')[::-1] # Revierte el rut
    acc = 0 # Suma total del calculo
    mul = 2 # Multiplicador del digito del rut
    for dig in rut:
        if mul > 7:
            mul = 2
        acc += int(dig) * mul
        mul += 1
    dv_esperado = 11 - acc%11
    if dv_esperado == 11:
        dv_esperado = '0'
    if dv_esperado == 10:
        dv_esperado = 'K'
    return str(dv) == str(dv_esperado)
