# Bu programda datetime modülünü kullanıcaz
# Porgram kulanıcıdan bir aracın trafiğe çıkış tarihini alır ve servis zamanlarını hesaplar

import datetime

def main():
    """Kullanicidan aracin trafige ciktigi tarihi alir
    O tarihten gunumuze kac gun gectigini hesaplar
    bakim() fonksiyonuna gun sayisini gonderir ve gelen ciktiyi ekrana yazdirir.
    
    """
    date = input("Araciniz hangi tarihte trafige cikti (22/5/2024)")
    date = date.split("/")
    
    today = datetime.datetime.now()
    date_obj = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
    
    difference = (today - date_obj)
    # print(difference) # 1748 days, 20:50:57.182677 çıkan bilgi bu
    # biz bu bilginin içinden days bilgisini alıcaz
    
    days = difference.days
    # print(days) => 1748
        
    print(f"Aracinizin bakim araligi : {bakim(days)}")
    
    
def bakim(day):
    """_summary_

    Args:
        day (int): Aracin trafiğe ciktigi gunden beri gecen sure

    Returns:
        string : arabanin kacinci servis araliginda oldugunu doner
    """
    bir_yil = 365
    if day <= bir_yil:
        return f"1. Servis araligi"
    elif day > bir_yil and day <= (bir_yil*2):
        return F"2. servis araligi"
    elif day > (bir_yil*2) and day <= (bir_yil*3):
        return f"3. servis araligi"
    else:
        return f"Hatali sure."
    
    
if __name__ == "__main__":
    main()
