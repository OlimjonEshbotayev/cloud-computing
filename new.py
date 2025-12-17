def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        qoldiq = n % 2
        binary = str(qoldiq) + binary
        n //= 2

    return binary


son = int(input("10-lik son kiriting: "))
natija = decimal_to_binary(son)
print("2-lik sanoq sistemasida:", natija)