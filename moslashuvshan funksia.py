#istalgancha sonlarning kopaytmasini hisoblovchi f-ya
def multiply(*sonlar):
    kopaytma=1
    for son in sonlar:
        kopaytma*=son
    return kopaytma
print(multiply(23,34,21,32,23))

#**kwarg yordamida istalgancha lugatni funksiyaga qoshish

def talaba_info(ism,familiya,**other_info):
    other_info['ism']=ism
    other_info['familiya']=familiya
    return other_info

talaba=talaba_info('Javohir','Toshqorgonov',tyil=2001,fakultet='fizika',yonalish='fizika')

print(talaba)




            
    
    
    
              
    
    
       
   
    
    