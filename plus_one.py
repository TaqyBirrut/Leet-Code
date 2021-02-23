def TambahAkhir (digits):
    hasil = digits[-1]+1
    if hasil >= 10:
        hasil = list(map(int, str(hasil)))
        digits.pop()
        digits.extend(hasil)
        return digits
    else:
        digits.pop()
        digits.append(hasil)
        return digits

def main():
    digits = [9,9]
    print(TambahAkhir(digits))
main()
