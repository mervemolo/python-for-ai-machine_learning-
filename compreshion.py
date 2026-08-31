# productList={"apple":50,
#              "notebook":15000,
#              "water":15,
#              "phone":45000,
#              "desk":500}
# new_list=[]
# for productName,price in productList.items():
#     if price>500:
#         new_list.append((productName,price))

# print(new_list)

# updated_list=[(productName,price) for productName,price in productList.items() if price>500]
# # print(updated_list)

#Sadece çift sayıların karesini alma

# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_numbers=[]

# def kare_al():
#     for i in numbers:
#         if i % 2 ==0:
#             even_numbers.append(i*i)

#     print(even_numbers)

# kare_al()

# even_numbers=[number*number for number in numbers if number%2==0]
# print(even_numbers)


urunler :dict[str,float]={"kalem":12,
         "silgi":10.5,
         "dolma kalem":35.9,
         "kalemtiras":7.5
         }
# def fiyatlari_isle(urunler: dict[str,float],min_fiyat:float)-> dict[str,float]:
#     return {
#         urun_adi:(urun_fiyati*0.85  if urun_fiyati>min_fiyat else urun_fiyati) for urun_adi,urun_fiyati in urunler.items()
#     }

# print(fiyatlari_isle(urunler,11))

# def fiyatlari_isle(urunler :dict[str,float],min_fiyat)-> dict[str,float]:
#     guncel_fiyatlar=[]
#     for urun_adi,urun_fiyati in urunler.items():
#         if urun_fiyati>min_fiyat:
#             urun_fiyati=urun_fiyati*0.85
#             guncel_fiyatlar.append((urun_adi,urun_fiyati))
#         else:
#            guncel_fiyatlar.append((urun_adi,urun_fiyati))
#     return guncel_fiyatlar
# print(fiyatlari_isle(urunler,11))