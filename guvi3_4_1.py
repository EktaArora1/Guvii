def findMaxProduct(arr, n): 
	ans = -float('inf') 
	maxvalue = 1
	minvalue = 1

	for i in range(0, n): 
		if arr[i] > 0: 
			maxvalue = maxvalue * arr[i] 
			minvalue = min(1, minvalue * arr[i]) 

		elif arr[i] == 0: 
			minvalue = 1
			maxvalue = 0
		elif arr[i] < 0: 
			prevMax = maxvalue 
			maxvalue = minvalue * arr[i] 
			minvalue = prevMax * arr[i] 
		ans = max(ans, maxvalue) 
		if maxvalue <= 0: 
			maxvalue = 1
	return ans 
if __name__ == "__main__":
    n=int(input())
    arr = list(map(int,input().split())) 
    print(findMaxProduct(arr, n)) 
