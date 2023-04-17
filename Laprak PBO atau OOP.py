# class lingkaran:
    
#     def __init__(self,pi,r): #pi = 3.14 atau 22/7, r = radius
#         self.pi = pi
#         self.r = r
        
#     def luas_lingkaran(self):
#         return self.pi * self.r**2
    
#     def keliling_lingkaran(self):
#         return 2 * self.pi * self.r
    
#     def cetak_luas(self):
#         print('Luas lingkaran =',self.luas_lingkaran())
    
#     def cetak_keliling(self):
#         print('Keliling lingkaran =',self.keliling_lingkaran())
        
# #membuat objek
# Objek_lingkaran = lingkaran(3.14,28)

# #memanggil objek dari kelas lingkaran
# Objek_lingkaran.luas_lingkaran()
# Objek_lingkaran.cetak_luas()

# class lingkaran:
    
#     #mendefinisikan atribut-atribut kelas self.pi = pi dan self.r = r
#     def __init__(self,pi,r): #pi = 3.14 atau 22/7, r = radius
#         self.pi = pi
#         self.r = r
        
#     def luas_lingkaran(self):
#         return self.pi * self.r**2
    
#     def keliling_lingkaran(self):
#         return 2 * self.pi * self.r
    
#     def cetak_luas(self):
#         print('Luas lingkaran =', self.luas_lingkaran())
    
#     def cetak_keliling(self):
#         print('Keliling lingkaran =', self.keliling_lingkaran())
        
# #membuat objek lebih dari satu
# Objek_lingkaran = lingkaran(3.14,28)
# Objek_lingkaran1 = lingkaran(22/7,49)
# Objek_lingkaran2 = lingkaran(3.14,35)

# #memanggil objek dari kelas lingkaran
# Objek_lingkaran.luas_lingkaran()
# Objek_lingkaran1.luas_lingkaran()
# Objek_lingkaran2.luas_lingkaran()

# Objek_lingkaran.keliling_lingkaran()
# Objek_lingkaran1.keliling_lingkaran()
# Objek_lingkaran2.keliling_lingkaran()

# #memanggil metode untuk menampilkan hasil luas & keliling
# Objek_lingkaran.cetak_luas()
# Objek_lingkaran1.cetak_luas()
# Objek_lingkaran2.cetak_luas()

# Objek_lingkaran.cetak_keliling()
# Objek_lingkaran1.cetak_keliling()
# Objek_lingkaran2.cetak_keliling()

#counter

# class PersegiPanjang: #184220033
    
    
#     counter = 0 # <<-- counter merupakan atribut statis
    
#     def __init__(self, p, l):
        
#         # menaikan nilai attribut statis
#         PersegiPanjang.counter += 1
#         # atribut-atribut non-statis
#         self.panjang = p
#         self.lebar = l

#     def ubahPanjang(self, p):
#         self.panjang = p

#     def ubahLebar(self, l):
#         self.lebar = l

#     def hitungLuas(self):
#         return self.panjang * self.lebar

#     def hitungKeliling(self):
#         return 2 * (self.panjang + self.lebar)

#     def cetakLuas(self):
#         print('Luas persegi panjang = %.2f' % self.hitungLuas())

#     def cetakkeliling(self):
#         print('Keliling persegi panjang=% .2f' % self.hitungKeliling())
        
# # Membuat lima objek dari kelas PersegiPanjang
# obj1 = PersegiPanjang(20, 15)
# obj2 = PersegiPanjang(10, 8)
# obj3 = PersegiPanjang(7, 5)
# obj4 = PersegiPanjang(4,2)
# obj5 = PersegiPanjang(9,3)

# # memanggil atribut counter melalui kelas
# print('Total Persegi Panjang =',PersegiPanjang.counter)

# print(obj1.counter)
# print(obj2.counter)
# print(obj3.counter)
# print(obj4.counter)
# print(obj5.counter)
    


# class Club_bola:

#     @staticmethod
#     def liga_indo(a,b):
#         return str(a,b)
    
#     def serieA(a,b):
#         return str(a,b)
    

# print("Club Liga Indo =", Club_bola('Persib','Persija'))
# print("Club Serie A", Club_bola('AC Milan','Juventus'))



# class Identitas_Kota:

#     def __init__(self,kota,kecamatan):
#         self.kota = kota
#         self.kecamatan = kecamatan

# class Identitas_Kota1(Identitas_Kota):
#     pass

# class Identitas_Kota2(Identitas_Kota):
#     pass

# Kota_kec = Identitas_Kota('Bandung','Sukasari')
# Kota_kec1 = Identitas_Kota1('Jakarta','Pademangan')
# Kota_kec2 = Identitas_Kota2('Semarang', 'Sukoharjo')


# print('Kota  =',Kota_kec.kota)
# print('Kota 1 =',Kota_kec.kota)
# print('Kota 2 =',Kota_kec.kota)

# print('Kec  =',Kota_kec.kecamatan)
# class lingkaran:
    
#     def __init__(self,pi,r): #pi = 3.14 atau 22/7, r = radius
#         self.pi = pi
#         self.r = r
        
#     def luas_lingkaran(self):
#         return self.pi * self.r**2
    
#     def keliling_lingkaran(self):
#         return 2 * self.pi * self.r
    
#     def cetak_luas(self):
#         print('Luas lingkaran =',self.luas_lingkaran())
    
#     def cetak_keliling(self):
#         print('Keliling lingkaran =',self.keliling_lingkaran())
        
# #membuat objek
# Objek_lingkaran = lingkaran(3.14,28)

# #memanggil objek dari kelas lingkaran
# Objek_lingkaran.luas_lingkaran()
# Objek_lingkaran.cetak_luas()

# class lingkaran:
    
#     #mendefinisikan atribut-atribut kelas self.pi = pi dan self.r = r
#     def __init__(self,pi,r): #pi = 3.14 atau 22/7, r = radius
#         self.pi = pi
#         self.r = r
        
#     def luas_lingkaran(self):
#         return self.pi * self.r**2
    
#     def keliling_lingkaran(self):
#         return 2 * self.pi * self.r
    
#     def cetak_luas(self):
#         print('Luas lingkaran =', self.luas_lingkaran())
    
#     def cetak_keliling(self):
#         print('Keliling lingkaran =', self.keliling_lingkaran())
        
# #membuat objek lebih dari satu
# Objek_lingkaran = lingkaran(3.14,28)
# Objek_lingkaran1 = lingkaran(22/7,49)
# Objek_lingkaran2 = lingkaran(3.14,35)

# #memanggil objek dari kelas lingkaran
# Objek_lingkaran.luas_lingkaran()
# Objek_lingkaran1.luas_lingkaran()
# Objek_lingkaran2.luas_lingkaran()

# Objek_lingkaran.keliling_lingkaran()
# Objek_lingkaran1.keliling_lingkaran()
# Objek_lingkaran2.keliling_lingkaran()

# #memanggil metode untuk menampilkan hasil luas & keliling
# Objek_lingkaran.cetak_luas()
# Objek_lingkaran1.cetak_luas()
# Objek_lingkaran2.cetak_luas()

# Objek_lingkaran.cetak_keliling()
# Objek_lingkaran1.cetak_keliling()
# Objek_lingkaran2.cetak_keliling()

#counter

# class PersegiPanjang: #184220033
    
    
#     counter = 0 # <<-- counter merupakan atribut statis
    
#     def __init__(self, p, l):
        
#         # menaikan nilai attribut statis
#         PersegiPanjang.counter += 1
#         # atribut-atribut non-statis
#         self.panjang = p
#         self.lebar = l

#     def ubahPanjang(self, p):
#         self.panjang = p

#     def ubahLebar(self, l):
#         self.lebar = l

#     def hitungLuas(self):
#         return self.panjang * self.lebar

#     def hitungKeliling(self):
#         return 2 * (self.panjang + self.lebar)

#     def cetakLuas(self):
#         print('Luas persegi panjang = %.2f' % self.hitungLuas())

#     def cetakkeliling(self):
#         print('Keliling persegi panjang=% .2f' % self.hitungKeliling())
        
# # Membuat lima objek dari kelas PersegiPanjang
# obj1 = PersegiPanjang(20, 15)
# obj2 = PersegiPanjang(10, 8)
# obj3 = PersegiPanjang(7, 5)
# obj4 = PersegiPanjang(4,2)
# obj5 = PersegiPanjang(9,3)

# # memanggil atribut counter melalui kelas
# print('Total Persegi Panjang =',PersegiPanjang.counter)

# print(obj1.counter)
# print(obj2.counter)
# print(obj3.counter)
# print(obj4.counter)
# print(obj5.counter)
    


# class Club_bola:

#     @staticmethod
#     def liga_indo(a,b):
#         return str(a,b)
    
#     def serieA(a,b):
#         return str(a,b)
    

# print("Club Liga Indo =", Club_bola('Persib','Persija'))
# print("Club Serie A", Club_bola('AC Milan','Juventus'))



# class Identitas_Kota:

#     def __init__(self,kota,kecamatan):
#         self.kota = kota
#         self.kecamatan = kecamatan

# class Identitas_Kota1(Identitas_Kota):
#     pass

# class Identitas_Kota2(Identitas_Kota):
#     pass

# Kota_kec = Identitas_Kota('Bandung','Sukasari')
# Kota_kec1 = Identitas_Kota1('Jakarta','Pademangan')
# Kota_kec2 = Identitas_Kota2('Semarang', 'Sukoharjo')


# print('Kota  =',Kota_kec.kota)
# print('Kota 1 =',Kota_kec.kota)
# print('Kota 2 =',Kota_kec.kota)

# print('Kec  =',Kota_kec.kecamatan)
# class lingkaran:
    
#     def __init__(self,pi,r): #pi = 3.14 atau 22/7, r = radius
#         self.pi = pi
#         self.r = r
        
#     def luas_lingkaran(self):
#         return self.pi * self.r**2
    
#     def keliling_lingkaran(self):
#         return 2 * self.pi * self.r
    
#     def cetak_luas(self):
#         print('Luas lingkaran =',self.luas_lingkaran())
    
#     def cetak_keliling(self):
#         print('Keliling lingkaran =',self.keliling_lingkaran())
        
# #membuat objek
# Objek_lingkaran = lingkaran(3.14,28)

# #memanggil objek dari kelas lingkaran
# Objek_lingkaran.luas_lingkaran()
# Objek_lingkaran.cetak_luas()

# class lingkaran:
    
#     #mendefinisikan atribut-atribut kelas self.pi = pi dan self.r = r
#     def __init__(self,pi,r): #pi = 3.14 atau 22/7, r = radius
#         self.pi = pi
#         self.r = r
        
#     def luas_lingkaran(self):
#         return self.pi * self.r**2
    
#     def keliling_lingkaran(self):
#         return 2 * self.pi * self.r
    
#     def cetak_luas(self):
#         print('Luas lingkaran =', self.luas_lingkaran())
    
#     def cetak_keliling(self):
#         print('Keliling lingkaran =', self.keliling_lingkaran())
        
# #membuat objek lebih dari satu
# Objek_lingkaran = lingkaran(3.14,28)
# Objek_lingkaran1 = lingkaran(22/7,49)
# Objek_lingkaran2 = lingkaran(3.14,35)

# #memanggil objek dari kelas lingkaran
# Objek_lingkaran.luas_lingkaran()
# Objek_lingkaran1.luas_lingkaran()
# Objek_lingkaran2.luas_lingkaran()

# Objek_lingkaran.keliling_lingkaran()
# Objek_lingkaran1.keliling_lingkaran()
# Objek_lingkaran2.keliling_lingkaran()

# #memanggil metode untuk menampilkan hasil luas & keliling
# Objek_lingkaran.cetak_luas()
# Objek_lingkaran1.cetak_luas()
# Objek_lingkaran2.cetak_luas()

# Objek_lingkaran.cetak_keliling()
# Objek_lingkaran1.cetak_keliling()
# Objek_lingkaran2.cetak_keliling()

#counter

# class PersegiPanjang: #184220033
    
    
#     counter = 0 # <<-- counter merupakan atribut statis
    
#     def __init__(self, p, l):
        
#         # menaikan nilai attribut statis
#         PersegiPanjang.counter += 1
#         # atribut-atribut non-statis
#         self.panjang = p
#         self.lebar = l

#     def ubahPanjang(self, p):
#         self.panjang = p

#     def ubahLebar(self, l):
#         self.lebar = l

#     def hitungLuas(self):
#         return self.panjang * self.lebar

#     def hitungKeliling(self):
#         return 2 * (self.panjang + self.lebar)

#     def cetakLuas(self):
#         print('Luas persegi panjang = %.2f' % self.hitungLuas())

#     def cetakkeliling(self):
#         print('Keliling persegi panjang=% .2f' % self.hitungKeliling())
        
# # Membuat lima objek dari kelas PersegiPanjang
# obj1 = PersegiPanjang(20, 15)
# obj2 = PersegiPanjang(10, 8)
# obj3 = PersegiPanjang(7, 5)
# obj4 = PersegiPanjang(4,2)
# obj5 = PersegiPanjang(9,3)

# # memanggil atribut counter melalui kelas
# print('Total Persegi Panjang =',PersegiPanjang.counter)

# print(obj1.counter)
# print(obj2.counter)
# print(obj3.counter)
# print(obj4.counter)
# print(obj5.counter)
    




# class Club_bola(): #184220033

#     Jumlah_klubbola = 0 #ini merupakan atribut statis
#     def __init__(self,klub_bola,negara):
#         self.klub_bola = klub_bola
#         self.negara = negara
    
#         Club_bola.Jumlah_klubbola += 1 #berfungsi untuk menambah nilai dari Jumlah_klubbola

    
#     #untuk menampilkan output dengan cara didalam
#     def detail_klub_bola(self):
#         print('Klub Bola =', self.klub_bola)
#         print('Asal Klub = ', self.negara)

    
#     #Untuk menampilkan total klub bola
#     def Total_klub_bola(self):
#         print('Total Klub Bola :', Club_bola.Jumlah_klubbola)

# #Membuat objek   
# obj_klubbola = Club_bola('Persib','Indonesia')
# obj_klubbola1 = Club_bola('Sevilla','Spanyol')

# #Memanggil method dari kelas Club_bola
# print(obj_klubbola.Jumlah_klubbola)
# print(obj_klubbola1.Jumlah_klubbola)

# Club_bola.Total_klub_bola(Club_bola)
# obj_klubbola.detail_klub_bola()
# obj_klubbola1.detail_klub_bola()







class Identitas_Kota: #Ini Super Class atau induk

    def __init__(self,kota,kecamatan):
        self.kota = kota
        self.kecamatan = kecamatan

    def informasi_kota_kecamatan(self):
        print('Kota',self.kota, 'kecamatan nya adalah', self.kecamatan)


        

class Identitas_Kota1(Identitas_Kota): #Ini sub class atau anak dari induk

    def informasi_kota_kecamatan(self):
        print('Kota',self.kota, 'kecamatan nya adalah', self.kecamatan)


#membuat objek
obj = Identitas_Kota('Bekasi','Pademangan')
obj1 = Identitas_Kota1('Cimahi','Setiamanah')
obj2 = Identitas_Kota1('Surakarta', 'Sukoharjo')



#memanggil metode dari kelas Identitas Kota
# print('Kota 1 =',obj.kota)
# print('Kota 2 =',obj1.kota)

# print('Kec  =', obj.kecamatan)
# print('Kec 1  =', obj.kecamatan)

#obj.informasi_kota_kecamatan()
obj.informasi_kota_kecamatan()

obj1.informasi_kota_kecamatan()
obj2.informasi_kota_kecamatan()












