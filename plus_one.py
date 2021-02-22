def TambahAkhir (digits):
    hasil = digits[-1]+1
    digits.pop()
    digits.append(hasil)
    return digits

def main():
    digits = [1,2,3]
    print(TambahAkhir(digits))
main()
