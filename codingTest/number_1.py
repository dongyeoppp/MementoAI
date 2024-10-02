# 1번 문제) 제일 작은 수 제거하기

def min_number_delete(arr):
    arr.sort(reverse=True)
    arr.pop()
    if arr == []:
        return -1
    else:
        return arr 

result1 = min_number_delete([4,3,2,1])
print(result1) # [4,3,2] 출력 

result2 = min_number_delete([10])
print(result2) # -1 출력 


