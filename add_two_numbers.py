def addtwonums (l1,l2):
    #Membuat l1 menjadi int dan di balik
    l1Balik = l1[::-1]
    l1Str = [str (l1Balik) for l1Balik in l1Balik]
    a_l1Str = "".join(l1Str)
    l1Int = int(a_l1Str)
    
    #Membuat l2 menjadi int dan di balik
    l2Balik = l2[::-1]
    l2Str = [str (l2Balik) for l2Balik in l2Balik]
    a_l2Str = "".join(l2Str)
    l2Int = int(a_l2Str)

    #Menjumlah list
    totalInt = l1Int + l2Int
    #Membuat list menjadi int
    totalList = [int(x) for x in str(totalInt)]

    return totalList[::-1]

def main():
    l1 = [2,4,3]
    l2 = [5,6,4]
    print(addtwonums (l1,l2))
main()
