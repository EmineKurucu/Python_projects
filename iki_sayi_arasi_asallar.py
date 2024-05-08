# Gönderilen iki sayı arasındaki tüm asal sayıları bulun

def asal_bul(num1, num2):
    asal_sayilar = []
    
    # Bir sayı 2'den kendisine kadar hiçbir sayıya bölünmüyorsa asaldır
    for num in range(num1 , num2):
        for say in range(2, num):
            if num % say != 0: # bu durumda sayı asal sayıdır
                asal_sayilar.append(num)
            break
    
    print(asal_sayilar)
            
def main():
    print("Bu program girdiğiniz iki sayi arasindaki tum asal sayilari bulur.")
    say1 = int(input("Araligin baslangic degerini giriniz : "))
    say2 = int(input("Araligin bitis degeini giriniz : "))
    
    print("Belirlediginiz araliktaki asal sayilarin listesi soyledir : ")
    print(asal_bul(say1, say2))
    
if __name__ == "__main__":
    main()

        
            