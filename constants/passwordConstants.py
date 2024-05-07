


import random
import string


def generate_random_string(length):
    # Sadece rakamlardan oluşan bir karakter dizisi oluşturur
    password = string.digits + string.ascii_letters
    # Belirtilen uzunlukta rastgele rakamlardan oluşan bir dizi oluşturur ve birleştirir
    return ''.join(random.choice(password) for _ in range(length))

def generate_random_gmail():
    # 10 karakterlik rastgele bir kullanıcı adı oluşturur
    kullanici_adi = generate_random_string(10)
    # E-posta adresinin domain kısmını belirler
    domain = "@gmail.com"
    # Kullanıcı adı ile domaini birleştirerek tam bir Gmail adresi oluşturur ve döndürür
    return kullanici_adi + domain


randomPassword = generate_random_string(8)

with open("sifreler.txt", "a") as file:
    file.write(randomPassword + "\n")

def get_previous_passwords(filename):
    # Dosyayı okuyarak içeriğini bir liste olarak alıyoruz
    with open(filename, "r") as file:
        oldPassword = file.readlines()
    # Her satırın sonundaki '\n' karakterlerini temizliyoruz
    oldPassword = [password.strip() for password in oldPassword]
    return oldPassword

# 'sifreler.txt' dosyasından önceki şifreleri alıyoruz
oldPassword = get_previous_passwords("sifreler.txt")

# Eğer dosyada önceki şifre yoksa, kullanıcıya bir mesaj gösteriyoruz
if not oldPassword:
    print("Önceki şifre bulunamadı.")
else:
    # Önceki şifreleri ekrana yazdırıyoruz
  firstOldPassword = oldPassword[0]

baseUrl = "https://tobeto.com/giris"
emailInputXpath = "(//*[@class='form-control mt-6'])[1]"
passwordInputXpath = "(//*[@class='form-control mt-6'])[2]" 
emailBoxId = "identifierId"
girisYapButtonCss = ".btn:nth-child(3)"
sifremiUnuttumCss=".d-block"
ePostaXPath = "//*[@id='__next']/div/main/section/div/div/div/input"
gonderCss = ".btn.btn-primary.mt-6.w-100"
gecersizformatmail = "xxx"
gecersizformattext = "• Girdiğiniz e-posta geçersizdir."
yeniSifreXpath = "/html/body/div[1]/div/main/section/div/form/div/div/input[1]"
sifreTekrarXpath = "/html/body/div[1]/div/main/section/div/form/div/div/input[2]"
sifreGonderCss = ".bg-white.px-12.py-12.shadow-lg.text-center"
sifreEslesmediText = "• Şifreler Eşleşmedi"
passwordCSS = "input[name='Passwd']"
validPassword = "235813Q!z"
validemail = "eminecskn314@gmail.com"
inboxFirstMessageXpath = "(//*[@jscontroller='ZdOxDb'])[1]"
firstMessageLinkXpath = "//*[@rel='noopener']"
uyumsuzSifre = generate_random_string(6)
unregisteredMail = generate_random_gmail()
popupCss = ".toast-body"
sifreSifirlamaBasariliText = "• Şifre sıfırlama işlemi başarılı."
alertXpath = "//*[@class='toast-body']"
yeniSifreEskisifreAyni = "• Yeni sifreniz mevcut sifrenizden farkli olmalidir"
fiveDigitPasswords = generate_random_string(5)
gmailUrl = "https://mail.google.com/mail/u/0/#inbox"
afterXpath = "//div[@id='identifierNext']/div/button/span"
nowLoginCss = ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d"
inboxFirstXpath = "(//*[@jscontroller='ZdOxDb'])[1]"
firstMessageXpath = "//*[@rel='noopener']"