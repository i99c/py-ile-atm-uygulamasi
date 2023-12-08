bakiye = 750
sifre = "1234"  

# Şifre kontrolü
#isdigit -> sadece rakamlardan oluşup oluşmadığını kontrol eder.
girilen_sifre = input("Şifrenizi girin (sadece sayılar): ")
if not girilen_sifre.isdigit() or len(girilen_sifre) == 0:
    print("Geçersiz şifre! Program sonlandırılıyor.")
else:
    if girilen_sifre == sifre:
        while True:
            print("Bakiye Sorgulama (a), Para Çekme (b), Para Yatırma (c), Çıkış (d) seçeneklerinden birini girin:")
            secenek = input("Seçenek: ").lower()

            if secenek == "a":
                print(f"Mevcut bakiye: {bakiye} TL")
            elif secenek == "b":
                cekilecek_miktar_str = input("Çekmek istediğiniz miktarı girin:")
                if cekilecek_miktar_str.isdigit():
                    cekilecek_miktar = int(cekilecek_miktar_str)
                    if 0 < cekilecek_miktar <= bakiye:
                        bakiye -= cekilecek_miktar
                        print(f"Yeni bakiye: {bakiye} TL")
                    else:
                        print("Yetersiz bakiye veya geçersiz miktar! İşlem iptal edildi.")
                else:
                    print("Geçersiz miktar! İşlem iptal edildi.")
            elif secenek == "c":
                yatirilan_miktar_str = input("Yatırmak istediğiniz miktarı girin:")
                if yatirilan_miktar_str.isdigit():
                    yatirilan_miktar = int(yatirilan_miktar_str)
                    if yatirilan_miktar > 0:
                        bakiye += yatirilan_miktar
                        print(f"Yeni bakiye: {bakiye} TL")
                    else:
                        print("Geçersiz miktar! İşlem iptal edildi.")
                else:
                    print("Geçersiz miktar! İşlem iptal edildi.")
            elif secenek == "d":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçenek! Lütfen geçerli bir seçenek girin.")
    else:
        print("Yanlış şifre! Program sonlandırılıyor.")
