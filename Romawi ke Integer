def romawi(s):
  rom = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
  total = 0
  sementara = 0
  sebelum = 0

  for i in range (len(s)):
      sementara = rom[s[i]]
      if sementara > sebelum:
          total = total + sementara - 2 * sebelum
      else:
          total += sementara
      sebelum = sementara
  return total
  
 def main():
  s = "IV"
  print(romawi(s))
main()
