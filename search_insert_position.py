def masukcari (nums,target):
	nums.append(target)
	nums.sort()
	hasil = nums.index(target)
	return hasil

def main():
	nums = [1,3,5,6]
	target = 7
	print(masukcari(nums,target))
main()
