def recursive_ackermann(a,b):
    ackermann_result = 0
    if( a==0 ):
        ackermann_result = b + 1
    elif( b==0 ):
        ackermann_result = recursive_ackermann(a-1,1)
    else:
        ackermann_result = recursive_ackermann(a-1,recursive_ackermann(a,b-1))
    return ackermann_result

print(recursive_ackermann(1,1))
# 3
