def panjangakhir(s):
	x = s.split()
	return(len(x[-1]))

def main():
	s = "Hello World"
	print(panjangakhir(s))
main()
