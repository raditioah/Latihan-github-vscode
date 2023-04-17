# class menu():

#     jumlah_menu = 0
    
#     def __init__(self,nama,asal,peminat):
#         self.nama = nama
#         self.asal = asal
#         self.peminat = peminat
#         menu.jumlah_menu +=1
    
#     def banyak_menu(self):
#         print('Banyaknya menu yang tersedia :', menu.jumlah_menu)

#     def detail_menu(self):
#         print('Nama menu :', self.nama)
#         print('Asal menu :', self.asal)
#         print('Banyaknya peminat menu :', self.peminat) 
    
# c1 = menu('Nasi Padang','Padang','Banyak')
# c2 = menu('Rendang','Padang','Banyak')
# c3 = menu('Gudeg','Jogja','Sedang')

# c1.detail_menu()
# c2.detail_menu()
# c3.detail_menu()
# menu.banyak_menu(menu)

class JamTangan: 

    
    def __init__(self,brand,price,warna):
        self.brand = brand
        self.price = price
        self.warna = warna
        
Aksesoris = JamTangan('ROLEX',1200,'merah')
print('Brand HP =',Aksesoris.brand)
print('Price =',Aksesoris.price)
print('Warna =',Aksesoris.warna)




# class AkseorisPakaian:

#       def __init__(self,barang):
#         self.barang = barang
#         self.jmlh_barang = 1
#         self.harga = 350000
#         self.total_harga = 'Rp.350000'

#       def detail_pembelian(self):
#           print('Nama Barang :', self.barang)
#           print('Jumlah barang :', self.jmlh_barang)
#           print('Harga:', self.harga)
#           print('Total harga :',  self.total_harga)

# NamaBarang = AkseorisPakaian('Sepatu')
# NamaBarang.detail_pembelian()

# class AksesorisPakaian:

#       def __init__(self,barang):
#         self.barang = barang
#         self.jmlh_barang = 1
#         self.harga = 350000
#         self.total_harga = 'Rp.350000'
      
# NamaBarang = AksesorisPakaian('Sepatu')
# print('Nama Barang :', NamaBarang.barang)
# print('Jumlah Barang :', NamaBarang.jmlh_barang)
# print('Harga :', NamaBarang.harga)
# print('Total Harga :', NamaBarang.total_harga)


# class AksesorisPakaian():

#     total_barang = 0
#     def __init__(self,nama_barang,jumlah,harga):
#         self.nama_barang =nama_barang
#         self.jumlah = jumlah
#         self.harga = harga
#         AksesorisPakaian.total_barang +=1

#     def total_yg_dibeli(self):
#         print('Total barang yang dibeli :', AksesorisPakaian.total_barang)
    
#     def detail_barang(self):
#         print('Nama Barang :',  self.nama_barang)
#         print('Jumlah Barang :', self.jumlah)
#         print('Harga :', self.harga)
        

# #definisi objek
# Brg1 = AksesorisPakaian('Sepatu',1,350000)
# Brg2 = AksesorisPakaian('Kemeja',4,2500000)
# Brg3 = AksesorisPakaian('Binder H5',2,32000)

# #pemanggilan
# Brg1.detail_barang()
# Brg2.detail_barang()
# Brg3.detail_barang()
# AksesorisPakaian.total_yg_dibeli(AksesorisPakaian)





