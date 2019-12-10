from itertools import permutations 

def bin_xor(s1,s2):
        x1 = []
        y1 = []
        p1 = permutations(s1) 
        for perm in list(p1): 
                x1.append(''.join(perm)) 
        p2 = permutations(s2)
        for perm in list(p2): 
                y1.append(''.join(perm)) 
        f = []
        #print(x1,y1)
        for i in range(len(x1)):
                num1 = int(x1[i],2)
                for j in range(len(y1)):
                        num2 = int(y1[j],2)
                        f.append(num1^num2)

        f = set(f)
        return len(f)


t = int(input())
for _ in range(t):
        x = int(input())
        s1 = input()
        s2 = input()
        print(bin_xor(s1,s2))
