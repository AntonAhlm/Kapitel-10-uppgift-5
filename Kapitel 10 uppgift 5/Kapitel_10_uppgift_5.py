
def nettopris(tal1):
    if tal1<500:
        tal2=tal1
        print("Nettopris:",tal2)
    if tal1>=500 and tal1<1000:
        tal2=tal1*0.98
        print("Nettorpis: ",tal2) 
    if tal1>=1000:
        tal2=tal1*0.95
        print("Nettopris: ",tal2)



a=int(input("Bruttopris:"))
nettopris(a)