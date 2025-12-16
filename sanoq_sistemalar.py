def decimal_to_octal(n):
    if n == 0:
        return "0"

    octal = ""
    while n > 0:
        qoldiq = n % 8
        octal = str(qoldiq) + octal
        n //= 8

    return octal


son = int(input("10-lik son kiriting: "))
natija = decimal_to_octal(son)
print("8-lik sanoq sistemasida:", natija)
