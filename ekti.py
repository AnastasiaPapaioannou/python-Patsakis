""" kaloume tn sinartiai opou kani print ts times t pinaka (string a)"""
def print11( a,x):
    for i in range(x):
        print a[i]
        "\n"
""" edw einai i sinartisi opou an stn thesi auti iparxi X k elegxoi ta giro
koutakia, ta auksani kata ena"""
def find_value(a,i,j,x,y):
    if(i-1>=0 and j-1>=0 and a[i-1][j-1]!="X" ):
        t=int(a[i-1][j-1])
        t=t+1
        ps=list(a[i-1])
        ps[j-1]=str(t)
        a[i-1]=ps
    if (i-1>=0 and j>=0 and a[i-1][j]!="X"):
        t2=int(a[i-1][j])
        t2=t2+1
        ps=list(a[i-1])
        ps[j]=str(t2)
        a[i-1]=ps
    if( i-1>=0 and j+1<y and a[i-1][j+1]!="X"):
        t3=int(a[i-1][j+1])
        t3=t3+1
        ps=list(a[i-1])
        ps[j+1]=str(t3)
        a[i-1]=ps
    if( j-1>=0  and a[i][j-1]!="X"):
        t4=int(a[i][j-1])
        t4=t4+1
        ps=list(a[i])
        ps[j-1]=str(t4)
        a[i]=ps
    if( j+1<y and a[i][j+1]!="X"):
        t5=int(a[i][j+1])
        t5=t5+1
        ps=list(a[i])
        ps[j+1]=str(t5)
        a[i]=ps
    if( j-1>=0 and i+1<x and a[i+1][j-1]!="X"):
        t6=int(a[i+1][j-1])
        t6=t6+1
        ps=list(a[i+1])
        ps[j-1]=str(t6)
        a[i+1]=ps
    if( i+1<x and a[i+1][j]!="X"):
        t7=int(a[i+1][j])
        t7=t7+1
        ps=list(a[i+1])
        ps[j]=str(t7)
        a[i+1]=ps
    if( j+1<y and i+1<x and a[i+1][j+1]!="X"):
        t8=int(a[i+1][j+1])
        t8=t8+1
        ps=list(a[i+1])
        ps[j+1]=str(t8)
        a[i+1]=ps
x=int(input( "dose tin x distasi orthogoniou="))
y=int(input( "dose tin y distasi orthogoniou="))
while(y==x):
    y =int(input("lathos arithmos!ORTHOFONIO THELOUME!!"))
a=["" for i in range(x)]
for i in range(x):
    for j in range(y):
        a[i]+=str(j)

b =int(input( "dose tin to plithos ton vomvon="))
for i in range(b):
    c =int(input( "dose tin sintetagmeni x="))
    f =int(input( "dose tin sintetagmeni y="))
    a[c]=a[c].replace(str(f),"X")
""" o loso p mpeni se sxolia auti i sinartisi einai gt to ekana print gia na
parakoloutho tous arithmosu an douleui swsta i askisi 
print11(a,x)
"""
""" edw elegxo pou den iparxi i timi X opou i timi X antistixoi stin thesi
tis vomvas kai opou den iparxi X tha valoume=0 kai srn panw sinartisi tha
to auksani kata +1"""
for i in range(x):
    for j in range(y):
        if(a[i][j]!="X"):
            a[i]=a[i].replace(a[i][j] ,"0")
            
""" o loso p mpeni se sxolia auti i sinartisi einai gt to ekana print gia na
parakoloutho tous arithmosu an douleui swsta i askisi 
print11(a,x)
"""
"""edw kaloume tn sinartisi fin value opou elegxoi an iparxi X ston pinaka
(string a) kai tha kani ts aparetites praksis"""
for i in range(x):
    for j in range(y):
        if(a[i][j]=="X"):
            find_value(a,i,j,x,y)
"""kaloume t sinartisi"""
print11(a,x)
        """efkolos sinsdiasmos einai gia x=3 y=4, arithmos vomvon=3,
x=0,y=0 . x=1,y=3, x=2, y=3"""
