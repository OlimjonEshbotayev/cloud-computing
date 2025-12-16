def decimal_to_hexadecimal(n):
    if n == 0:
        return "0"

    belgilar = "0123456789ABCDEF"
    hex_son = ""

    while n > 0:
        qoldiq = n % 16
        hex_son = belgilar[qoldiq] + hex_son
        n //= 16

    return hex_son


son = int(input("10-lik son kiriting: "))
natija = decimal_to_hexadecimal(son)
print("16-lik sanoq sistemasida:", natija)
