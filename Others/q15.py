def largestRectangleArea( heights):
    stack = [-1]
    maxArea = 0

    for i in range(len(heights)):
        # we are saving indexes in stack that is why we comparing last element in stack
        # with current height to check if last element in stack not bigger then
        # current element
        #print(i,stack)
        print(stack)
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            lastElementIndex = stack.pop()
            print( heights[i], heights[lastElementIndex],i, stack)
            maxArea = max(maxArea, heights[lastElementIndex] * (i - stack[-1] - 1))
        stack.append(i)

    # we went through all elements of heights array
    # let's check if we have something left in stack
    while stack[-1] != -1:
        print(stack,':')
        lastElementIndex = stack.pop()
        maxArea = max(maxArea, heights[lastElementIndex] * (len(heights) - stack[-1] - 1))

    return maxArea



print(largestRectangleArea( [2,1,5,6,2,3]))