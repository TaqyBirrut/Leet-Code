def strStr(haystack, needle):
    for i in (haystack):
        if needle in haystack:
            return (len(needle))
        elif needle not in haystack:
            return ("-1")
        else:
            return("0")

def main():
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))
main()
