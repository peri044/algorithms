# Binary search algo to find x in a sorted array

def binarysearch(input, check_num, start_index, end_index):
    
    for i in range(start_index, end_index):
        m = int(start_index+end_index/2)
        print (input[m])
        if input[m]==check_num:
            return True
        elif input[m] <=check_num:
            search = binarysearch(input[m+1:end_index], check_num, 0, len(input[m:end_index]))
            return search
        elif input[m] >=check_num:
            search = binarysearch(input[start_index:m], check_num, 0, len(input[start_index:m]))
            return search
            
if __name__=='__main__':
    search = binarysearch([2, 9, 12, 15, 18], 15, 0, 5)
    print (search)