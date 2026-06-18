#print("Kiritilgan sonning kvadratini qaytarivchi dastur")
#savol = "Istalgan sonni kiritin"
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)


#ism = input("Ismingiz nima?")
#savol = f"Salom {ism.title()}! Yoshiz nechchida? "
#yosh = input(savol)
#yosh = int(yosh)
#height = input("Buyingiz nechchi mtr")
#height = float(height)
#familiya = input("Familyangiz nima?")
#print(f"Hello {familiya.title()}")
print("Kiritilgan sonni kvadratini qaytarivchi dastur")
savol = "Istalgan sonni kritin"
savol += ("Dasturni tuxtatish uchun 'exit' deb yozing:  ")
ishora = True
while ishora:
    qiymat = input(savol)
    
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)** 2)
        
    
