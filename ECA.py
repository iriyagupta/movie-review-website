def cellular_automaton(s,num,row):
    pattern={}
    pattern_list=['...','..x','.x.','.xx','x..','x.x','xx.','xxx']
    n=len(s)
    for i in range(7,-1,-1):
        if num/(2**i) == 1:
            pattern[pattern_list[i]]="x"
            num = num-2**i
        else:
            pattern[pattern_list[i]]="."
            
    for j in range(0,row):
        new=""
        for i in range(0,n):
            st=s[i-1]+s[i]+s[(i+1)%n]
            new=new+pattern[st]
        s=new
    return new
            
    
print cellular_automaton('.x.x.x.x.', 26, 5)
>>> .....x...
print cellular_automaton('.x.x.x.x.', 250, 3)
>>>> xxx.x.xxx
print cellular_automaton('...x....', 69, 4)
>>> .x.x...x
    
    
