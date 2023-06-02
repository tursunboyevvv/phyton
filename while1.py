# while/takrorlanuvchi savollar
savol = "Sevgan kitobingizni kiriting"
savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

while True:
    kitob = input(savol)
    if kitob == 'exit':
        break
print('Rahmat!')

#muzeyga chipta narxlari yoshga bog'liq

savol="Yoshingizni kiriting: "
while True:
    qiymat=input(savol)
    if qiymat=='exit'or qiymat=='quit':
        break
    yosh=int(qiymat)
    
    if yosh<7:
        narx=2000
        
    elif 7<=yosh<18:
        narx=3000
        
    elif 18<=yosh<65:
        narx=10000
    else :
        narx=0
    
    if narx==0:
        print("Sizga chipta bepul!")
    else :
        print(f"Chipta {narx} so'm")
        
        
        
       
   
    
    