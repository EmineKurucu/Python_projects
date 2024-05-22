def main():
    print("Bu uygulama kilo ve boy bilgilerinizi alarak boy-kilo endeksinizi hesaplayacak.")
    name = input("Adiniz : ")
    surname = input("Soyadiniz : ")
    
    try : # sayısal değer girilmesini denetledik
        height = float(input("Boyunuz(m) : "))
        weight = float(input("Kilonuz(kg) : "))
    except :
        print("Gecerli degerler giriniz. ")
        
    if height <= 0 or weight <= 0: # 0'a bölüm ve kilonun 0 olmasını denetledik
        print("Hata: Boy veya kilo 0 girilemez")
        return 
    bm_index = body_mass_index(height, weight)
    

    if bm_index <= 18.4: 
        print(f"Vucut kitle indexiniz : {bm_index:.2f}.")
        print("Sonuç : Zayif")
    elif bm_index <= 24.9: 
        print(f"Vucut kitle indexiniz : {bm_index:.2f}.")
        print("Sonuc = Normal")
    elif bm_index <= 29.9:
        print(f"Vucut kitle indexiniz : {bm_index:.2f}.")
        print("Sonuc = Fazla Kilolu")
    elif bm_index <= 34.9 :
        print(f"Vucut kitle indexiniz : {bm_index:.2f}.")
        print("Sonuc : Sisman(obez)")
    else:
        print("Hata: Girilen degerler gecerli aralikta degil.")

def body_mass_index(hg , kg ):
    return kg / (hg**2)

if __name__ == "__main__":
    main()
