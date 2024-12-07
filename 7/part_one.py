from get_input import get_input

#check if values can end up in given result 
def calc (equation_res, mid_result, arr, index):
    if index==len(arr) :
        if mid_result==equation_res:
            return True
        return False
    
    if mid_result>equation_res:
        return False
    
    ret_with_plus=calc(equation_res, mid_result+arr[index],arr,index+1)
    ret_with_mul=calc(equation_res, mid_result*arr[index],arr,index+1)
    if ret_with_plus or ret_with_mul:
        return True
    return False


#calc final result
final_result=0
input=get_input()

for equation_res, values in input.items():
    if calc(equation_res, values[0], values, 1):
        final_result+=equation_res
print(final_result)


