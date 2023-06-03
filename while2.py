# #while/ro'yxatlar va lug'atlar
buyurtma=[]
n=1
while True:
    savol=f"{n}-mahsulotni kiriting:"
    mahsulot=input(savol)
    buyurtma.append(mahsulot)
    javob=input("Yana mahsulot kiritasizmi(ha/yo'q):")
    if javob=="ha":
        n+=1
        continue
    else:
        break
    #mahsulot va narxi korsatilgan lug'at(input yordamida)
mahsulotlar={}
ishora=True

while ishora:
    mahsulot=input("mahsulotni kiriting:")
    narx=input(f"{mahsulot}ning narxini kiritung:")
    mahsulotlar[mahsulot]=float(narx)

    javob=input("Yana mahsulot qo'shasizmi(ha/yo'q): ")
    if javob=='yoq':
        ishora=False

for mahsulot,narx in mahsulotlar.items():
    print(f"{mahsulot}ning  narxi {narx} so'm ")
    #buyurtma va mahsulotlar solishtirlib borlarining narxi korsatiladi
buyurtmalar=['olma', 'uzum', 'non']
mahsulotlar={'uzum': 10000.0,
 'kartoshka': 4000.0,
 'karam': 2000.0,
 'non': 2800.0,
 'tarvuz': 20000.0}

while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narx=mahsulotlar[buyurtma]
        print(f"{buyurtma} - {narx} so'm")
    else:
        print(f"Bizda {buyurtma} yoq ")
        
    
      
    
    
              
    
    
       
   
    
    