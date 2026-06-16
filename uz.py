mevalar = ['olma','nok','apple','banan']
print("Birinchi meva: " , mevalar[2])
narxlar =[1312,2121,2121]
print(narxlar[0] + narxlar[2])


mevalar = ['olma','nok','apple','banan']
mevalar.append('glos')
print(mevalar)


mevalar = ['olma','nok','apple','banan']
mevalar.insert(1,'olma')
print(mevalar)

mevalar = ['olma','nok','apple','banan']
del mevalar[2]
print(mevalar)

mevalar = ['olma','nok','apple','banan']
mevalar.remove('banan')
print(mevalar)


mevalar = ['olma','nok','apple','banan']
bozorliklar =mevalar.pop(0)
print("MEN " +bozorliklar + "sooib oldim")
print("Olinmagn bozorliklar:" , mevalar)


