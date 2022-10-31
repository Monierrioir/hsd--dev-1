"""Üniversite notuna göre harf sistemi(vize%40+final%60)"""




vize=float(input(print("Vize notunu gir: ")))
final=float(input(print("Final notunu gir: ")))
totalMark=vize%40+final%60
print("Notun: ",totalMark)

if totalMark>=90:
 print("Dersten AA aldın.")
elif totalMark>=80:
    print("Dersten AB aldın.")
elif totalMark>=70:
    print("Dersten BA aldın.")
elif totalMark>=60:
    print("Dersten BB aldın.")
elif totalMark<=60:
    print("Dersten kaldın.")






















"""10 ürün bulunan bir markette fiyat ve para üstü hesaplama"""
productList=[1,2,3,4,5,6,7,8,9,10]

balance=50;
sum=0;
userInput=0;
print("Almak istediğiniz ürünlerin adını ekrana giriniz.İşlem bittiğinde ekrana 'stop' yazınız.\nProducts\n",productList)
while userInput !="stop":
 userInput=input("Ürünü yazınız: ")
 if userInput =="stop":
  break
    
 sum+=int(userInput)
balance-=sum
if balance<0 :
 print("Yeterli bakiyeniz bulunmamaktadır.")
else:
       print("Fiyat  toplamı: ", sum)
print("Kalan bakiye:", balance)









