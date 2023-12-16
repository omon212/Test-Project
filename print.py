a = "HeLlO WoRlD"

print(a.upper())  # Hamma harfni katta qilib beradi
print(a.lower())  # Hammasini kichik qilib beradi
print(a.find('l'))  # Icgida nechta harf borligini bilib beradi
print("".join(a))  # Har bir harfdan keyingi o`zgaruvchini string ga qoshib beradi
print("Hello, {}!".format("Sharifjon"))  # f-string ni shogirdi
print(a.capitalize())  # Stringning birinchi harfini katta qilib, qolgan harflarni kichik qiladi
print(a.casefold())  # Barcha harflarni kichik qilib beradi
centered_a = a.center(20)
print(centered_a)  # Ozgaruvchini ortaga qo'yib beradi
print(a.count('l'))  # Stringda berilgan element nechtada uchraganligini chiqarib beradi
print(a.endswith("D"))  # Ozgaruvuchning oxiri shu element bilan tugalganini tekshirib beradi
print(a.expandtabs())  # Ozgaruvuchga probel qo'yib beradi
print(a.format_map({'name': 'Dunyo'}))  # Dictni shogirti
print(a.index('l'))  # Stringda berilgan elementning nechinchi indexda turishi
print(a.isalnum())  # Matnda faqat harflar va raqamlar bo'lsa True qaytaradi, aks holda False
print(a.isalpha())  # Matnda faqat harflar bo'lsa True qaytaradi, aks holda False
print(a.isdecimal())  # Matnda faqat raqamlar bo'lsa True qaytaradi, aks holda False
print(a.isdigit())  # Matnda faqat raqamlar bo'lsa True qaytaradi, aks holda False
print(a.isidentifier())  # Matn identifikator (o'zgaruvchi nomi) bo'lishi mumkin bo'lgan qiymat bo'lsa True qaytaradi, aks holda False
print(a.islower())  # Barcha harflar kichik bo'lsa True qaytaradi, aks holda False
print(a.isnumeric())  # Matnda faqat raqamlar mavjud bo'lsa True qaytaradi, aks holda False
print(a.isprintable())  # Matnda chop etilishi mumkin bo'lgan belgilar mavjud bo'lsa True qaytaradi, aks holda False
print(a.isspace())  # Matnda faqat bo'sh joy belgilari mavjud bo'lsa True qaytaradi, aks holda False
print(a.istitle())  # Matn sarlavha formatida (title case) yozilgan bo'lsa True qaytaradi, aks holda False
print(a.isupper())  # Barcha harflar katta bo'lsa True qaytaradi, aks holda False
