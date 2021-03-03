def untung(harga):
  for i in harga:
    minimal = min(harga)
    maksimal = max(harga)
    pMinimal = harga.index(minimal)
    pMaksimal = harga.index(maksimal)
    total = maksimal - minimal

    if pMinimal > pMaksimal:
      del harga[pMaksimal]
  return total


def main():
  harga = [7,1,5,3,6,4]
  print(untung(harga))
main()
