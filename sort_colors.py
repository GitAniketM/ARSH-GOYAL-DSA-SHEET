class Solution:
    def sortColors(self, arr: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # lets try to use heap sort
        """Build a max heap. At this point, the largest 
        item is at the top so replace it with the last element reducing the heap size by 1
        Finally, heapify the root of the tree
        Repeat if size > 1"""
        
        # for the given problem i have used HeapSort, through MergeSort, QuickSort also can be used.
        
        def heapify(arr, n, i):
            largest = i  # initialize the root at largest
            l = 2*i + 1
            r = 2*i + 2
            
            if l < n and arr[largest] < arr[l]:
                largest = l
                
            if r < n and arr[largest] < arr[r]:
                largest = r
                
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                
                heapify(arr, n, largest)
                
        
        def heapsort(arr):
            n = len(arr)
            
            for i in range(n//2-1, -1, -1):
                heapify(arr, n, i)
                
            for i in range(n-1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]   #swap
                heapify(arr, i, 0)
                
        heapsort(arr)