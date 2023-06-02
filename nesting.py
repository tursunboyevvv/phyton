#Ro'yxat ichidagi lug'at/bir nechta shaxslar haqidagi 
#malumotlarni consolga chiqarish

navoiy={ 'ism':'Alisher Navoiy','tyil':1441,'vyil':1501,'tjoy':'hirot'}
temur={ 'ism':'amir temur','tyil':1336,'vyil':1405,'tjoy':'shahrisabz'}
buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil','tyil':810,'vyil':870,
           'tjoy':'Buxoro' }

shaxslar=[navoiy,temur,buxoriy]

for shaxs in shaxslar:
    ism=shaxs['ism']
    tyil=shaxs['tyil']
    vyil=shaxs['vyil']
    tjoy=shaxs['tjoy']
    print(f"{ism.title()} {tyil}-yilda {tjoy.title()}da tavallud topgan."
          f"{vyil-tyil} yil umr ko'rgan")