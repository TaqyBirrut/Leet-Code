def buangelement(nums,val):
	newlist = []
	for i in nums:
		if i == val:
			continue
		else:
			newlist.append(i)
	return newlist

def main():
	nums = [3,2,2,3,4,4]
	val = 3
	print(buangelement(nums,val))
main()
