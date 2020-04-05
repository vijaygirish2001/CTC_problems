'''
Stack of Boxes: You have a stack of n boxes, with widths w1 , heights h i, and depths di . The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height, and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
'''
import numpy as np

class box:

    # Representation of a box
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

def largest_height(lst_bx):

    def is_valid(lst_bx, i, btm_ind):
        if lst_bx[i].h<=lst_bx[btm_ind].h and lst_bx[i].w <= lst_bx[btm_ind].w and lst_bx[i].d<=lst_bx[btm_ind].d:
            return True
        return False
    def create_stack(lst_bx,btm_ind, stack_height):
        if btm_ind in stack_height:
            return stack_height[btm_ind]
        max_height = 0
        for i in range(btm_ind+1, len(lst_bx)):
            if is_valid(lst_bx,i, btm_ind):
                hei = create_stack(lst_bx,i, stack_height)
                max_height = max(max_height,hei)

        max_height += lst_bx[btm_ind].h
        stack_height[btm_ind] = max_height
        return max_height



    srt_ind = np.argsort([i.h for i in lst_bx])

    lst_bx  = [lst_bx[i] for i in srt_ind[::-1]]

    print(lst_bx[-1].d)

    stack_height = {}

    hei = 0
    for i in range(0,len(lst_bx)):
        height = create_stack(lst_bx,i, stack_height)
        hei = max(hei,height)

    return hei


boxes = []

boxes.append(box(4,12,32))
boxes.append(box(1,2,3))
boxes.append(box(2,5,6))


hei = largest_height(boxes)

print(hei)



