#Funksiyalar mavzusi
#1
def tyiltop(ism, yosh):
    
    '''foydalanuvchidan yoshi va ismini sorab , uning tugilgan yilinii topib murojat qilamiz'''
    print(f"{ism.title()} {2023-yosh}-yilda tug'ilgan")
    
tyiltop('abdulmumin',23)
    
#2
def kub_kv_top(son):
    '''sonnning kubi va kvadratini topadigan f-ya (foydalanuvchidan soragan holda)'''
    print(f"{son}ning kvadrati {son**2}ga teng,kubi esa {son**3} ga teng")

kub_kv_top(12)

#3
def juft_or_toq(son):
    '''juft yoki toqlikni aniqlovchi f-ya'''
    if son%2:
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")
        
juft_or_toq(234342122)

#4
def taqqosla(son1,son2):
    '''taqqoslovchi funksiya'''
    if son1>son2:
        print(f"{son1} soni {son2} sonidan katta")
    elif son2>son1:
        print(f"{son2} soni {son1} sonidan katta")
    else:
        print("sonlar teng")

taqqosla(12, 12)
#5
def bolinish_belgilari(son):
    '''foydalanuvchi kiritgan son,malum oraliqdagi sonlardan qaysilariga
    qoldiqsiz  bolinishini chiqarib beradigan f_ya'''
    for n in range(1,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bolinadi")

bolinish_belgilari(48)


        


    
    
              
    
    
       
   
    
    