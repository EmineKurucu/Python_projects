def main():
    print("Sizden istenen notlari giriniz."
          "Bu program ortalamaniza karsilik gelen 0-5 arasindaki notunuzu hesaplayacak")
    
    while True:
        try:
            yazili1 = float(input("1. yazili notunuzu giriniz: "))
            if yazili1 > 100 or yazili1 <0: 
                raise ValueError("Hata: Sinav notu 100'den buyuk veya 0'dan kucuk olamaz.")
            yazili2 = float(input("2. yazili notunuzu giriniz : "))
            if yazili2 > 100 or yazili2 <0: 
                raise ValueError("Hata: Sinav notu 100'den buyuk veya 0'dan kucuk olamaz.")
            sozlu = int(input("Sozlu nutunuzu giriniz : "))
            if sozlu > 100 or sozlu <0: 
                raise ValueError("Hata: Sozlu notu 100'den buyuk veya 0'dan kucuk olamaz.")
            break; 
        except ValueError:
            print("Hata: Gecerli bir deger giriniz : ")
        except Exception as e:
            print(f"Hata : Beklenmedik bir hata oluştu {e}.")
            
    print(f"Ortalamaniz : {ortalama_hesaplama(yazili1, yazili2, sozlu):.2f}")
    ortalama = ortalama_hesaplama(yazili1, yazili2, sozlu)
        
        
    print(f"Not : {Not_hesaplama(ortalama)}" )
        

            
        
def ortalama_hesaplama(yaz1, yaz2, soz):
    return (yaz1 + yaz2 + soz) / 3

def Not_hesaplama(ort):
        # değer aralığını bulucaz
        if ort <= 24:
            return 0
        elif ort <= 44:
            return 1
        elif ort <= 54:
            return 2
        elif ort <= 69:
            return 3
        elif ort <= 84:
            return 4
        else :
            return 5
            
if __name__ == "__main__":
    main()
    
