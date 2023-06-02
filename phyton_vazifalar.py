#7- dars vazifa
#ismlar=["Javohir","Farruh","Alloshukur"]
#print(ismlar[0],"ertaga futbolga borasizmi?")
#print(ismlar[1], "bugun kvant fizikasidan qaysi mavzu o'tildi")

#t_shaxslar=["Beruniy", "Amir Temur", "Alisher Navoiy"]
#z_shaxslar=["Bill Gates" , "Elon Musk" , "Messi"]

#shaxs1=t_shaxslar.pop(1)
#shaxs2=z_shaxslar.pop(2)

#8-dars vazifa

#davlat=["Usa","Russia","China","Canada" ]
#print(davlat)
#jsonlar=list(range(120,1200,2))
#print(jsonlar)
#taomlar=["osh","manti","lavash","somsa","katlet"]
#print(taomlar)

#9-dars for sikl operatori
#ismlar=["jamol","sohib","kozim","maston","farruh"]
#for ism in ismlar:
   # print("Assalamu alaykum", ism)
#n=len(ismlar)
#n=str(n)
#print("kod",n, " marta takrorlandi")

#tsonlar=list(range(10,100,2))
#kublar=[]
#for t in tsonlar:
    #kublar.append(t**3)
    
#print(tsonlar)
#print(kublar)

#odamlar=[]
#s=input("Bugun nechta odam bilan uchrashdingiz?")
#s=int(s)
#for n in range(s):
   # odamlar.append(input(f"{n+1}-uchrashgan odamingiz kim?"))
#print(odamlar)

#10-dars if va else

cars=["toyota","mazda","hyundai","gm","kia" ]
for car in cars:
    if car!="gm":
        print(car.title())
    else:
        print(car.upper())

login=input("loginingizni kiriting:")
if login=="admin":
    print("Xush kelibsiz Admin!.Foydalnaauvchilar ro'yxatini ko'rasizmi?")
else:
    print("Xush kelibsiz",login)
    
son1=int(input("Birinchi sonni kiriting:"))
son2=int(input("Ikkinchi sonni kiriting:"))
if son1==son2:
    print("sonlar teng")
else:
    print("sonlar teng emas") 

son=int(input("Istalgan sonni kiriting:"))
if son>0:
    print("Ushbu son musbat!")
else:
    print("Ushbu son manfiy!")
    
son=int(input("Istalgan sonni kiriting:"))
if son>0:
    print("Ushbu sonning ildizi",son**0.5 ,"ga teng")
else:
    print("Iltimos musbat son kiriting!")
    
  ##11-dars if elif else 
n=int(input("Juft sonni kiriting:"))
if n in range(0,1000000,2):
    print("rahmat")
elif n in range(1,1000000,2):
    print("kechirasiz bu toq son")

yosh=int(input("Yoshingiz nechida?"))
if yosh<5 or yosh>65:
    print("Siz uchun kirish tekin!")
elif yosh<18:
    print("Chiptan narxi -10000so'm")
elif yosh>18:
    print("Chipta narxi-20000 so'm") 
    
x=float(input("birinchi son:"))
y=float(input("ikkinchi sonni kiriting:"))
if x>y:
    print("x > y")
elif x==y:
    print("x=y")
else:
    print("x<y")
mahsulotlar=["olma","shakar","yog'","karam","piyoz","kartoshka","chesnok","uzum","anor","baliq" ]
savat=[]
m=input("nechta mahsulot olasiz:")
m=int(m) 
   
for n in range(m):
    savat.append(input( f"{n+1} - tanlagan maxsulotingiz:"))
    print(savat)
bor_mahsulotlar=[]
mavjud_emas=[]
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print("dokonimizda quyidagi mahsulotlar yoq")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
        print("siz soragan barchasi bizda bor")
#lugatlar
otam={
      'ism':'sulaymonov otabek',
      't_yil':1979,
      't_joy':'qorakol'
      }   
print(f"{otam['ism']} {otam['t_yil']} ") 



dp={
    'ispania':'madrid','fransia':'parij','rossia':'moskva',
    'belgia':'brussel','polsha':'warshava','nigeria':'abuja'
     }
d=input("istalgan davlatingizni kiriting:")
p=dp.get(d)
if p==None:
    print("bunday malumot yoq")
else:
    print(f"{d} ning poytaxti {p} shahri")




 
    
    
