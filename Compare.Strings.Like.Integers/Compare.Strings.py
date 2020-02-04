
#!/usr/bin/python3

#Compare 2 Strings as Numbers 
#Returns TRUE if the first number is larger than the second 

def larger_than(a,b):
    if len(a) > len(b):
        return True 
    elif len(a) < len(b):
        return False

    size = len(a)

    for i in range (size):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            return True
        else:
            return False
    return False
    
if __name__ == "__main__": 
    
    a = "129"
    b = "128"

    print(larger_than(a,b))

