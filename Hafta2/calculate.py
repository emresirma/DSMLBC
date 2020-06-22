print("""Hesap Makinesi
      
İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi 

""")

x = int(input("Birinci Sayı:"))
y = int(input("İkinci Sayı:"))

işlem =  input("İşlem Numarasını Giriniz:") 

if (işlem == "1"): 
    print("Toplama İşlemi Sonucu: ", x+y)

elif (işlem == "2"):
    print("Çıkarma İşlemi Sonucu: ", x-y)

elif (işlem == "3"):
    print("Çarpma İşlemi Sonucu: ", x*y)

elif (işlem == "4"):
    print("Bölme İşlemi Sonucu: ", x/y)

else:
    print("Yanlış İşlem Değeri Girişi Yaptınız, Tekrar Deneyiniz")
