import random

bakiye = 100000.0
gr_altin_f = 6500
bist100_f = 11000
euro_f = 55.0
dolar_f = 50.0


gr_altin_adet = 0.0
bist100_adet = 0.0
euro_adet = 0.0
dolar_adet = 0.0
mevduat = 0.0


hafta = 0


def hafta_ilerlet():
    global gr_altin_f, bist100_f, euro_f, dolar_f, mevduat
    gr_altin_f = gr_altin_f*random.uniform(0.98, 1.03)
    bist100_f = bist100_f*random.uniform(0.96, 1.05)
    dolar_f = dolar_f*random.uniform(0.99, 1.02)
    euro_f = euro_f*random.uniform(0.99, 1.02)
    mevduat = mevduat*1.006

def bakiyegoster():
    global bakiye, gr_altin_adet, bist100_adet, euro_adet, dolar_adet, mevduat
    print(f"\nToplam bakiyenizin TL karşılığı = {bakiye+(gr_altin_adet*gr_altin_f)+(bist100_adet*bist100_f)+(euro_adet*euro_f)+(dolar_adet*dolar_f)+(mevduat)} TL\n")
    print(f"Nakit = {bakiye} TL")
    print(f"Gram altın bakiyeniz = {gr_altin_adet} ({gr_altin_adet*gr_altin_f}) TL")
    print(f"Borsadaki bakiyeniz (BIST100) = {bist100_adet*bist100_f} TL")
    print(f"Euro bakiyeniz = {euro_adet} € ({euro_adet*euro_f} TL)")
    print(f"Dolar bakiyeniz = {dolar_adet} $ ({dolar_adet*dolar_f} TL)")
    print(f"Mevduat hesabı = {mevduat} TL")


while True:
    print("\n\nİşlemler:")
    print("1. Yatırım yap")
    print("2. Varlıkları nakde çevir")
    print("3. Bakiye ve varlıkları göster")
    print("4. Hafta ilerlet")
    print("0. Çıkış1")
    secim = input("İşlem seçin: ")

    if secim == "1":
        while True:
            print("\nYatırım yapılabilecek alanlar:\n")
            print(f"1. Gram altın ({gr_altin_f})")
            print(f"2. BIST100 ({bist100_f})")
            print(f"3. Euro ({euro_f})")
            print(f"4. Dolar ({dolar_f})")
            print(f"5. Vadeli hesaba para yatır (Haftalık %0,6)")
            print("0. Geri")
            y_secim = input("\nSeçiminiz: ")

            print("\n")

            if y_secim == "1":
                print(f"Gram altın bakiyeniz = {gr_altin_adet}")
                print(f"TL bakiyeniz = {bakiye} TL, {(bakiye/gr_altin_f):.2f} gram altın alabilirsiniz.")
                while True:
                    islemhacmi = float(input(f"Altın fiyatı = {gr_altin_f} TL\n\nKaç gram altın almak istiyorsunuz? (Çıkmak için '0' tuşlayınız) : "))
                    if islemhacmi*gr_altin_f <= bakiye:
                        bakiye = bakiye-(islemhacmi*gr_altin_f)
                        gr_altin_adet += islemhacmi
                        print("İşlem başarıyla gerçekleşti!\n")
                        print(f"Yeni gram altın bakiyesi = {gr_altin_adet}\n")
                        print(f"Yeni bakiye = {bakiye} TL")
                        break
                    elif islemhacmi < 0:
                        print("\n\n!!!Negatif değer giremezsiniz!!!\n\n")
                    elif islemhacmi == 0:
                        break
                    else:
                        print("\n\n!!!Yetersiz bakiye!!!\n\n")
            elif y_secim == "2":
                print(f"Borsadaki paranız = {bist100_adet*bist100_f}")
                print(f"TL bakiyeniz = {bakiye} TL")
                while True:
                    islemhacmi = float(input(f"BIST100 fiyatı = {bist100_f} TL\n\nBorsaya kaç TL yatırmak istiyorsunuz? (Çıkmak için '0' tuşlayınız) : "))
                    if islemhacmi <= bakiye:
                        bakiye = bakiye-islemhacmi
                        bist100_adet += (islemhacmi/bist100_f)
                        print("İşlem başarıyla gerçekleşti!\n")
                        print(f"Borsadaki yeni tutar = {bist100_adet*bist100_f} TL\n")
                        print(f"Yeni bakiye = {bakiye} TL")
                        break
                    elif islemhacmi < 0:
                        print("\n\n!!!Negatif değer giremezsiniz!!!\n\n")
                    elif islemhacmi == 0:
                        break
                    else:
                        print("\n\n!!!Yetersiz bakiye!!!\n\n")
                break                
            elif y_secim == "3":
                print(f"Euro bakiyeniz = {euro_adet} €")
                print(f"TL bakiyeniz = {bakiye} TL , {(bakiye/euro_f):.2f} euro alabilirsiniz.")
                while True:
                    islemhacmi = float(input(f"Euro fiyatı = {euro_f} TL\n\nKaç euro almak istiyorsunuz? (Çıkmak için '0' tuşlayınız) : "))
                    if islemhacmi*euro_f <= bakiye:
                        bakiye = bakiye-(islemhacmi*euro_f)
                        euro_adet += islemhacmi
                        print("İşlem başarıyla gerçekleşti!\n")
                        print(f"Yeni Euro bakiyesi = {euro_adet} €\n")
                        print(f"Yeni bakiye = {bakiye} TL")
                        break
                    elif islemhacmi < 0:
                        print("\n\n!!!Negatif değer giremezsiniz!!!\n\n")
                    elif islemhacmi == 0:
                        break
                    else:
                        print("\n\n!!!Yetersiz bakiye!!!\n\n")
                break
            elif y_secim == "4":
                print(f"Dolar bakiyeniz = {dolar_adet} $")
                print(f"TL bakiyeniz = {bakiye} TL , {(bakiye/dolar_f):.2f} dolar alabilirsiniz.")
                while True:
                    islemhacmi = float(input(f"Dolar fiyatı = {dolar_f} TL \n\nKaç dolar almak istiyorsunuz? (Çıkmak için '0' tuşlayınız) : "))
                    if islemhacmi*dolar_f <= bakiye:
                        bakiye = bakiye-(islemhacmi*dolar_f)
                        dolar_adet += islemhacmi
                        print("İşlem başarıyla gerçekleşti!\n")
                        print(f"Dolar bakiyesi = {dolar_adet} $\n")
                        print(f"Yeni bakiye = {bakiye} TL")
                        break
                    elif islemhacmi < 0:
                        print("\n\n!!!Negatif değer giremezsiniz!!!\n\n")
                    elif islemhacmi == 0:
                        break
                    else:
                        print("\n\n!!!Yetersiz bakiye!!!\n\n")
                break
            elif y_secim == "5":
                print(f"Vadeli hesap bakiyeniz = {mevduat} TL")
                print(f"TL bakiyeniz = {bakiye} TL")
                while True:
                    islemhacmi = float(input(f"Haftalık faiz oranı = %0,6 \n\nVadeli hesaba kaç TL yatırmak istiyorsunuz? (Çıkmak için '0' tuşlayınız) : "))
                    if islemhacmi <= bakiye:
                        bakiye = bakiye-islemhacmi
                        mevduat += islemhacmi
                        print("İşlem başarıyla gerçekleşti!\n")
                        print(f"Vadeli hesaptaki yeni tutar = {mevduat} TL\n")
                        print(f"Yeni bakiye = {bakiye} TL")
                        break
                    elif islemhacmi < 0:
                        print("\n\n!!!Negatif değer giremezsiniz!!!\n\n")
                    elif islemhacmi == 0:
                        break
                    else:
                        print("\n\n!!!Yetersiz bakiye!!!\n\n")
                break     
            elif y_secim == "0":
                break
            else:
                print("Geçersiz seçim!\n\n")
       
    elif secim == "2":
        print("Para çekme menüsü yapılacak")
        bakiyegoster()
        print("\nHangi varlığınızı nakde çevirmek istersiniz?\n")
        print("")
        while True:
            bakiyegoster()
            print("\nHangi varlığınızı nakde çevirmek istersiniz?\n")
            print(f"1. Gram altın adet: {gr_altin_adet} ({gr_altin_f} TL)")
            print(f"2. Borsa: {bist100_adet*bist100_f} TL")
            print(f"3. Euro : {euro_adet} € ({euro_f} TL)")
            print(f"4. Dolar : {dolar_adet} $ ({dolar_f} TL)")
            print(f"5. Vadeli hesap (Haftalık %0,6)")
            print("0. Geri")
            y_secim = input("\nSeçiminiz: ")

            print("\n")

            if y_secim == "1":
                print(f"Gram altın bakiyeniz = {gr_altin_adet}")
                while True:
                    islemhacmi = float(input(f"Altın fiyatı = {gr_altin_f} TL \n\nKaç gram altın satmak istiyorsunuz? (Çıkmak için '0' tuşlayınız) : "))
                    if islemhacmi <= gr_altin_adet:
                        bakiye = bakiye+(islemhacmi*gr_altin_f)
                        gr_altin_adet -= islemhacmi
                        print("İşlem başarıyla gerçekleşti!\n")
                        print(f"Yeni gram altın bakiyesi = {gr_altin_adet}\n")
                        print(f"Yeni bakiye = {bakiye} TL")
                        break
                    elif islemhacmi < 0:
                        print("\n\n!!!Negatif değer giremezsiniz!!!\n\n")
                    elif islemhacmi == 0:
                        break
                    else:
                        print("\n\n!!!Yetersiz bakiye!!!\n\n")
            elif y_secim == "2":
                print(f"Borsadaki paranız = {bist100_adet*bist100_f}")
                while True:
                    islemhacmi = float(input(f"BIST100 fiyatı = {bist100_f} TL \n\nBorsadan kaç TL çekmek istiyorsunuz? (Çıkmak için '0' tuşlayınız) : "))
                    if islemhacmi <= bist100_adet*bist100_f:
                        bakiye = bakiye+(islemhacmi*bist100_f)
                        bist100_adet -= (islemhacmi/bist100_f)
                        print("İşlem başarıyla gerçekleşti!\n")
                        print(f"Borsadaki yeni tutar = {bist100_adet*bist100_f} TL\n")
                        print(f"Yeni bakiye = {bakiye} TL")
                        break
                    elif islemhacmi < 0:
                        print("\n\n!!!Negatif değer giremezsiniz!!!\n\n")
                    elif islemhacmi == 0:
                        break
                    else:
                        print("\n\n!!!Yetersiz bakiye!!!\n\n")
                break                
            elif y_secim == "3":
                print(f"Euro bakiyeniz = {euro_adet} €")
                while True:
                    islemhacmi = float(input(f"Euro fiyatı = {euro_f} TL \n\nKaç euro satmak istiyorsunuz? (Çıkmak için '0' tuşlayınız) : "))
                    if islemhacmi <= euro_adet:
                        bakiye = bakiye+(islemhacmi*euro_f)
                        euro_adet -= islemhacmi
                        print("İşlem başarıyla gerçekleşti!\n")
                        print(f"Yeni Euro bakiyesi = {euro_adet} €\n")
                        print(f"Yeni bakiye = {bakiye} TL")
                        break
                    elif islemhacmi < 0:
                        print("\n\n!!!Negatif değer giremezsiniz!!!\n\n")
                    elif islemhacmi == 0:
                        break
                    else:
                        print("\n\n!!!Yetersiz bakiye!!!\n\n")
                break
            elif y_secim == "4":
                print(f"Dolar bakiyeniz = {dolar_adet} $")
                while True:
                    islemhacmi = float(input(f"Dolar fiyatı = {dolar_f} TL \n\nKaç dolar satmak istiyorsunuz? (Çıkmak için '0' tuşlayınız) : "))
                    if islemhacmi <= dolar_adet:
                        bakiye = bakiye+(islemhacmi*dolar_f)
                        dolar_adet -= islemhacmi
                        print("İşlem başarıyla gerçekleşti!\n")
                        print(f"Dolar bakiyesi = {dolar_adet} $\n")
                        print(f"Yeni bakiye = {bakiye} TL")
                        break
                    elif islemhacmi < 0:
                        print("\n\n!!!Negatif değer giremezsiniz!!!\n\n")
                    elif islemhacmi == 0:
                        break
                    else:
                        print("\n\n!!!Yetersiz bakiye!!!\n\n")
                break
            elif y_secim == "5":
                print(f"Vadeli hesap bakiyeniz = {mevduat} TL")
                while True:
                    islemhacmi = float(input(f"Haftalık faiz oranı = %0,6 \n\nVadeli hesaptan kaç TL çekmek istiyorsunuz? (Çıkmak için '0' tuşlayınız) : "))
                    if islemhacmi <= mevduat:
                        bakiye = bakiye+islemhacmi
                        mevduat -= islemhacmi
                        print("İşlem başarıyla gerçekleşti!\n")
                        print(f"Vadeli hesaptaki yeni tutar = {mevduat} TL\n")
                        print(f"Yeni bakiye = {bakiye} TL")
                        break
                    elif islemhacmi < 0:
                        print("\n\n!!!Negatif değer giremezsiniz!!!\n\n")
                    elif islemhacmi == 0:
                        break
                    else:
                        print("\n\n!!!Yetersiz bakiye!!!\n\n")
                break     
            elif y_secim == "0":
                break
            else:
                print("Geçersiz seçim!\n\n")
    elif secim == "3":
        bakiyegoster()

    elif secim == "4":
        haftasec = int(input("Kaç hafta ilerlemek istiyorsunuz? : "))
        if haftasec <= 0:
            haftasec = int(input("Lütfen pozitif bir değer girin!"))

        ilerlenecekhafta = hafta+haftasec
        while hafta < (ilerlenecekhafta):
            hafta_ilerlet()
            hafta += 1
        print(f"\n{haftasec} hafta ilerlendi. Güncel hafta: {hafta}\n")
        bakiyegoster()

    elif secim == "0":
        print("Çıkış yapılıyor. İyi günler!")
        break
    else:
        print("Geçersiz seçim!\n\n")