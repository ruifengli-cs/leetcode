Design a CPU alert system.

                                l               r 
TimeStamp indexs in an arry:    0    1     2    3    4     5    6    7     8
Error Rate%:                    55   40    60   65   62    69   45   35    75
Time Period  N
Minimum Error Rate: m
target Time: any number
Out true:  if we can find one time period that contains the target time stamp, return true if all the error rate is >= min error rate.

targettime: 4
period:3
min 60

is the period fixed? Yes
valid period must contain targettime
tiemstamp can be any time.
is timestamp continious increasing?
is target time alwasy within timestamp? we don't know


# APP1: brute force. 
# 1. get all the time period.
# 2. get all valid time period. they contain target time
# 3. loop through them to see each error rate is >= min error rate
# Time: O(n*N) n: len(array) N: time Period Space: O(1)

# APP2: 
# 1. compre if target time with the len(array). if target time > len(array), return False
# 2. use left, right pointers as the window boundry. left will go from target index to the left 

# 2. right continue moves tille it covers target time or it reach N. 
# 3. then move left and right together to see is valid time period should be alarmed.
# 4. if error rate < min_error_rate, store the info in hashmap mapping[index] = False

def send_cpu_alart(array, N, min_err_rate, target_time):
    if target_time >= len(array):
        return False
    left = right = target_time
    step = 0
    left = target_time - N if target_time - N >= 0 else 0
    if target_time - N < 0:
        right += N - target_time
    count = 0
    for i in range(left, right + 1):
        if array[i] >= target_time:
            count += 1
    
    while right < len(array) and left <= target_time:    
        if count == N:
            return True
        if array[left] >= target_time:
            count -= 1
        left += 1
        right += 1
        if array[right] >= target_time:
            count += 1
    return False
