import os
urun_list = []
urun_fiyat_list = []
while True:
    while True:
        urun_giris = input("Ürün Ekle (durmak için stop yazin): ").lower()
        if urun_giris in urun_list:
            print("bu ürün zaten ekli!\n")
        else:
            break
    if urun_giris=="stop":
        break
    else:
        while True:
            try:
                urun_fiyat = int(input("Ürün fiyati ekle: "))
                break
            except:
                print("lütfen bir fiyat giriniz! ör: 30\n")
        urun_list.append(urun_giris)
        urun_fiyat_list.append(urun_fiyat)

urun_fiyat_name_list = list(zip(urun_list,urun_fiyat_list))
print("----ÜRÜNLER----")
for urun,fiyat in urun_fiyat_name_list:
    print(f"Ürün: {urun.capitalize()} | Fiyat: {fiyat}₺")

print("\n")

toplam = 0
while True:
    while True:
        urun_sec = input("Ürün adı: ").lower()
        if urun_sec in urun_list:
            while True:
                try:
                    urun_adedi = int(input("Ürün adedi: "))
                    break
                except:
                    print("lütfen bir sayi giriniz!\n")
                

            price = ""
            for urun,fiyat in urun_fiyat_name_list:
                if urun_sec == urun:
                    print(f"{urun_adedi} adet {urun} fiyati : {fiyat*int(urun_adedi)}₺")
                    toplam+=fiyat*int(urun_adedi)
  
            break
        else:
            print("bu urun mevcut değil\n")
    
    cevap = input("Alişverişe devam etmek ister misiniz? (y/n): ").lower()
    if cevap == "n":
        break
    print("\n")

print("\n")
print(f"Toplam: {toplam}₺")

while True:
    odeme = int(input("Öde: "))
    if odeme<toplam:
        print("Yetersiz Bakiye")
    elif odeme==toplam:
        print("Alişveriş için teşekkürler")
        break
    elif odeme>toplam:
        paraustu = odeme-toplam
        print(f"Para üstünüz -> {paraustu}₺")
        print("Alişveriş için teşekkürler")
        break

<<<<<<< HEAD
=======
print("\nAlişveriş biti!")
>>>>>>> 7261060d845b1fb9fdcbc89d63853ef7497f41e3
os.system("pause")
