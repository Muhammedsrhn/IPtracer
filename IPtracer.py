import requests
from colorama import init, Fore, Style
from time import strftime, sleep
from sys import exit

r = requests.Session()

def get_time():
    date = strftime("%H:%M:%S")
    return (f"{Style.BRIGHT + Fore.CYAN}[{date}]{Style.RESET_ALL}")


def main():
    print(f"""
    {Style.BRIGHT + Fore.RED}  ▄▄ ▄███▄{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}▄▀▀▀▀ ▄▄▄ ▀▀▀▀▄   {Style.BRIGHT + Fore.MAGENTA}Ip Tracer v1{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}█    █   █    █   {Style.BRIGHT + Fore.RED}+-----------------------------------+{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}█    ▀▄▄▄▀    █             {Style.BRIGHT + Fore.YELLOW}Coded by Acemi Hacker{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀{Style.RESET_ALL}    """)
    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}Hangi İp Bulma Yöntemini Kullanmak İstersiniz :{Style.RESET_ALL}\n")
    tmp = (11 * " ")
    print(f"{Style.RESET_ALL}{tmp}{Style.BRIGHT + Fore.MAGENTA}1 > {Style.RESET_ALL + Fore.WHITE}Kendi İp Adresini Tara{Style.RESET_ALL}")
    print(f"{Style.RESET_ALL}{tmp}{Style.BRIGHT + Fore.MAGENTA}2 > {Style.RESET_ALL + Fore.WHITE}Hedef İp Adresini Tara{Style.RESET_ALL}")
    print(f"{Style.RESET_ALL}")
    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[>] {Style.BRIGHT + Fore.WHITE}Seçiminiz:{Style.RESET_ALL}",end="")
    method = input()

    if (int(method != "1" and method != "2")):
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Seçiminiz 1 veya 2 olmalıdır!{Style.RESET_ALL}")
        exit(0)

    if(method=="1"):
        myipaddr()
    elif(method=="2"):
        targetip()


def myipaddr():
    #kendi ip adres bilgilerimizi alıyoruz
    baglanti = r.get("https://ipapi.co/json/")

    #verileri yazdiriyoruz
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}İp : {Style.RESET_ALL}"+baglanti.json()['ip']+"\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Şehir : {Style.RESET_ALL}"+baglanti.json()['city']+"\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Bölge : {Style.RESET_ALL}"+baglanti.json()['region']+"\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Ülke : {Style.RESET_ALL}"+baglanti.json()['country_name']+"\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Ülke_başkenti : {Style.RESET_ALL}"+baglanti.json()['country_capital']+"\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Saat_dilimi : {Style.RESET_ALL}"+baglanti.json()['timezone']+"\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Ülke_Kodu : {Style.RESET_ALL}"+baglanti.json()['country_calling_code']+"\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Para_birimi : {Style.RESET_ALL}"+baglanti.json()['currency_name']+"\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Gsm : {Style.RESET_ALL}"+baglanti.json()['org']+"\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Googel_Maps : https://maps.google.com/?q={Style.RESET_ALL}"+str(baglanti.json()['latitude'])+","+str(baglanti.json()['longitude']))


def targetip():
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Hedef İp Adresi :{Style.RESET_ALL}",end="")
    target=input()
    url="https://ipapi.co/"+target+"/json/"
    baglanti = r.get(url)

    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}İp : {Style.RESET_ALL}"+baglanti.json()['ip'] + "\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Şehir : {Style.RESET_ALL}"+baglanti.json()['city'] + "\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Bölge : {Style.RESET_ALL}" +baglanti.json()['region'] + "\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Ülke : {Style.RESET_ALL}" +baglanti.json()['country_name'] + "\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Ülke_başkenti : {Style.RESET_ALL}" +baglanti.json()['country_capital'] + "\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Saat_dilimi : {Style.RESET_ALL}" +baglanti.json()['timezone'] + "\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Ülke_Kodu : {Style.RESET_ALL}" +baglanti.json()['country_calling_code'] + "\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Para_birimi : {Style.RESET_ALL}" +baglanti.json()['currency_name'] + "\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Gsm : {Style.RESET_ALL}"+baglanti.json()['org'] + "\n")
    print(f"{Style.RESET_ALL}{Style.BRIGHT + Fore.MAGENTA}{Style.BRIGHT + Fore.WHITE}Googel_Maps : https://maps.google.com/?q={Style.RESET_ALL}"+str(baglanti.json()['latitude'])+","+str(baglanti.json()['longitude']))

main()
