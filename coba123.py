
nama=input("ketikkan nama : ")
print(nama)
def luas():
	panjang=int(input("masukkan panjang : "))
	lebar=int(input("masukkan lebar : "))
	luasnya=panjang*lebar
	print("luasnya adalah ",panjang," x ",lebar," = ",luasnya)
hitung=input('apakah mau menghitung luas (y/n) ?')
if hitung=="y":
	luas()
else:
		pass