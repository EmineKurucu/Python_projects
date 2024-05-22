def main():
    email = input("Email : ")
    parola = input("Parola: ").rstrip()
    
    if isMail_correct(email):
        if isParola_correct(parola):
            print("Giris basarili")
        else:
            print("Parolaniz yanlis.")
            print("Tekrar deneyiniz.")
    else :
        print("Email adresiniz yanlis.")
        print("Tekrar deneyiniz.")
        
def isMail_correct(kullanici_maili):
    dogru_mail  = "email@deneme.com"
    if (kullanici_maili == dogru_mail):
        return True
    else:
        return False
    
def isParola_correct(kullanici_parolasi):
    dogru_parola = "abc007"
    if (kullanici_parolasi == dogru_parola):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
