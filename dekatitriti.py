""" snartisi mas opou elegxi to sum, k prostheti an den kseperasi to y
kai tote epistrefi to teliko sum stn sinartisi, dld to (ahham), alla edw se polles
periptosis otan kanoume taksinomisi tn pinaka se auksousa den perni swstes times
giauto ksana kanoume to pinaka k fthinousa k elegxoume ta 2 sum p dimiourgounte,
stn auksouna taksinomisa k stn fthinousa k oti einai pio megalo to kanoume
return """
def maxDistance(a,x,y):
    sum1=0
    sum2=0
    for i in range(x):
        if(sum1+a[i]<=y):
            sum1=sum1+a[i]
        
    temp=0
    for i in range(x-1):
        for j in range(i+1,x):
            if(a[i]>a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                
    for i in range(x):
        if(sum2+a[i]<=y):
            sum2=sum2+a[i]
            
    if(sum2>sum1):
        return sum2
    else:
        return sum1
  


x =int(input( "dose ton arithmo x opou einai o arithmos ton diastimatos apostasis p tha dwsis: "))
a=[]
for i in range(x):
    t=int(input("dose apostasi:"))
    while(t<=0):
        t=int(input("lathos apostasi , dwse neo arithmo: "))

    a.append(t)

y=int(input("dose ena arithmo: "))
while(y<0):
    print "lathos arithmos"
    y=int(input("dwse thetiko: "))
print "y=", y
""" ta taksinomoume etsi wste na pari tn megalitero arithmo k meta na prostheti
tous mikroterous, taksinomisi kata auksousa seira"""
temp=0
for i in range(x-1):
    for j in range(i+1,x):
        if(a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp

for i in range(x):
    print a[i],

""" kaloume sinartisi me ton pinaka (a), ton airthmo ton diastaseon k tn
thetiko"""

ahham=maxDistance(a,x,y)



print " to megalitero athroisma diastaseon opou den ksepersnoun to y=",y
print "einai to =",ahham

