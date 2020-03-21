'''
amazon-interview-questions0

Given a binary array {0,1,1,0,0,1,0,0,1} , sort the array in a way that all zeros come to the left and all the one's come to the right side of the array.
'''

def bin_srt(arr):
    no_ones = sum(arr)

    no_zeros = len(arr) -no_ones

    return [0]*no_zeros+[1]*no_ones

print(bin_srt([0,1,0,1,1,0]))