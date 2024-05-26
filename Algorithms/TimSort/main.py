def GetMinrun(n):
	r = 0
	while n >= 64:
		r |= n & 1
		n >>= 1
	return n + r

print(GetMinrun(2222222))