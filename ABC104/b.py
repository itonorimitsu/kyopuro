def judge(string):
    cw = False
    judge = False
    for i in range(2, len(string) - 1):
        if string[i].isupper() and string[i] != 'C':
            judge = True
        elif string[i].isupper() and string[i] == 'C' and cw:
            judge = True
        
        if string[i] == 'C':
            cw = True

    if judge or cw == False:
        return True
    else:
        return False        
    
if __name__ == "__main__":
    s = list(input().strip())
    if s[0] != "A" or s[1].isupper() or s[-1].isupper() or judge(s):
        print('WA')
    else:
        print('AC')
    