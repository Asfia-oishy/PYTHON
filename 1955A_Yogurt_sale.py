# yogurt sale

T = int(input())

for _ in range(T):
    n,a,b = map(int,input().split())
    per_piece = n*a
    
    if n==1:
        print(a)

    elif n==2:
        print(min(per_piece,b))
    else:
        c= int(n/2)

        if n%2==0:
            prom = b*c
            

            
        else:
            prom = b*c + a
           
        print(min(per_piece,prom))
        
        

            


        
        
            
    
