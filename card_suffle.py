dict1={'red':['rA','rK','rQ','rJ','r10','r9','r8','r7','r6','r5','r4','r3','r2','RA','RK','RQ','RJ','R10','R9','R8','R7','R6','R5','R4','R3','R2'],
'black':['bA','bK','bQ','bJ','b10','b9','b8','b7','b6','b5','b4','b3','b2','BA','BK','BQ','BJ','B10','B9','B8','B7','B6','B5','B4','B3','B2']}
list1=[]
list2=[]
list3=[]
list4=[]


import random
a=0
b=25
c=25
z=0
while a<1 :
    z+=1
    print(z)
    m=random.randint(1,2)
    if m==1:
        import random
        u=dict1['red']
        if len(u)>0:
            n=random.randint(0,b)
            if len(list1) !=13:
                list1.append(u[n])
                b-=1
                u.remove(u[n])
            elif len(list2) !=13:
                list2.append(u[n])
                b-=1
                u.remove(u[n])
            elif len(list3) !=13:
                list3.append(u[n])
                b-=1
                u.remove(u[n])
            elif len(list4) !=13:
                list4.append(u[n])
                b-=1
                u.remove(u[n])
    elif m==2:
        import random
        v=dict1['black']
        print(v)
        if len(v)>0:
            p=random.randint(0,c)
            if len(list1) !=13:
                list1.append(v[p])
                c-=1
                v.remove(v[p])
            elif len(list2) !=13:
                list2.append(v[p])
                c-=1
                v.remove(v[p])
            elif len(list3) !=13:
                list3.append(v[p])
                c-=1
                v.remove(v[p])
            elif len(list4) !=13:
                list4.append(v[p])
                c-=1
                v.remove(v[p])
    
    
    if len(list1) ==13 and len(list2) ==13 and len(list3) ==13 and len(list4) ==13:
        a+=1
print(list1,
list2,
list3,
list4)
