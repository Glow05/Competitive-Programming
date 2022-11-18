#User function Template for python3
#Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.

class Solution: 
    def select(self, arr, i):
        # code here
        max = arr[0]
        index = 0
        for i in range(1, len(arr)):
            if arr[i] > max:
                max = arr[i]
                index = i
        return index
        
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends 
#