
#foydalanuvchininng ismi, tel  raqami ,
# emailini qabul qilib,lug'at korinishida qaytaruvchi funksia

def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {'ism':ism,
              'familiya':familiya,
              'tyil':tyil,
              'yoshi':2020-tyil,
              'tjoy':tjoy,
              'email':email,
              'telefon':tel}
    return mijoz

print("Mijoz haqida ma'lumotlarni kiriting.")
mijozlar =[]
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob!='ha':
        break

print("Mijozlar:")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
          f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")


#3 ta sondan eng kattasini qaytaruvchi dastur

def kattasi(x,y,z):
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max

kattasi(12,33,3)
 
   
#tub sonlarni topubchi dastur

def tub_sonlar_top(min,max):    
    tub_sonlar = []    
    for n in range(min,max+1):
        tub = True
        if (n==1):
            tub = False
        elif(n==2):
            tub = True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
                
    return tub_sonlar

tub_sonlar_top(1,20)

#fibonachchi sonlariini qaytaruvchi dastur

def fibonacci(n):
    sonlar=[]
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1] + sonlar[x-2])
            
    return sonlar

            
    
    
    
              
    
    
       
   
    
    