'''
This question is designed to help you get a better understanding of basic heap operations.
You will be given queries of  types:

" " - Add an element  to the heap.
" " - Delete the element  from the heap.
"" - Print the minimum of all the elements in the heap.
NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

Input Format
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

no_of_queries = int(input())

heap = []

for i in range(no_of_queries):
    query = input().split()

    if int(query[0]) == 1: # add an element
        element = int(query[1])
        heap.append(element)
        # CHeck if parent is thr
        sz = len(heap)
        parent = (sz-1)//2
        current = sz-1
        #print(query, heap, parent , current)
        while heap[parent] > heap[current]:
            heap[parent],  heap[current] = heap[current],  heap[parent]

            current = parent
            parent = current//2

    elif int(query[0]) == 2:
        ind_delete = heap.index(int(query[1]))

        heap[ind_delete] = heap[-1]
        heap.pop(-1)

        s=len(heap)

        def remove_(ind_delete,s):
            if ind_delete<s//2:
                if heap[ind_delete] > heap[ind_delete*2] or \
                heap[ind_delete] > heap[ind_delete*2+1]:
                    if heap[ind_delete*2]< heap[ind_delete*2+1]:
                        heap[ind_delete*2], heap[ind_delete]= heap[ind_delete], heap[ind_delete*2]
                        remove_(ind_delete*2,s)
                    else:
                        heap[ind_delete*2+1], heap[ind_delete]= heap[ind_delete], heap[ind_delete*2+1]
                        remove_(ind_delete*2+1,s)



            else:
                return

        remove_(ind_delete,s)
    elif int(query[0]) == 3:
        print(heap[0])
