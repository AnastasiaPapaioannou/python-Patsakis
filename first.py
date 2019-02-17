"""lipon edw einai i sinartisi sumIntervals opou me to return epistrefi to sum
dld to j """
def sumIntervals(a,b,x):
    max=b[0]
    sum=b[0]-a[0]
    for i in range(1,x):
        if(max>a[i]):
            if(max<b[i]):
                sum=sum+b[i]-max
        else:
            sum=sum+b[i]-a[i]
               
        max=b[i]
    return sum
                
""" autos o x einai enas arithmos pou tha mas dwsi o xristis etsi wste
na mporoume na kseroume poses agkiles me arithmous tha dwsi k meta na prosthesei
tous arithmous mesa se auton !"""
x =int(input( "dose ena arithmo opou antistixi ston arithmo ton agkilon:"))
"""o z,l einai metavlites pou eisounte me tn x kai to xrisimopio parakatw
etsi wste na exw kapou apirakti tin timi tou x """
z=x
l=x
""" o f k p einai oi kenoi pinakes opou tha gemisoun me ts times mesa"""
a=[]
b=[]
""" edw kaloume vrogxo epanalipsis gt tha dwsi 2 arithmous epi x fwres """
"""me tin xrisi t append isxoroume ts times stous 2 pinakes"""
for i in range(x):
    t=int(input("dose ena arithmo:"))
    w=int(input("dose akoma ena arithmo:"))
    a.append(t)
    b.append(w)
    
"""taksinomoume ta stoixeia"""
temp=0
temp2=0
for i in range(x):
    for j in range(i+1,x):
         if(a[i]>a[j]):
             temp=a[i]
             temp2=b[i]
             a[i]=a[j]
             b[i]=b[j]
             a[j]=temp
             b[j]=temp2
            
         if(a[i]==a[j]):
             if(b[i]>b[j]):
                 temp=b[i]
                 temp2=a[i]
                 b[i]=b[j]
                 a[i]=a[j]
                 b[j]=temp
                 a[j]=temp2
                 
            
print "diladi i lista mas i opia onomazete->sumIntervals einai autoi oi arithmoi"
for i in range(x):
    print  [a[i],b[i]]
  
j=sumIntervals(a,b,x)
print "telikos  arithmos=",j
