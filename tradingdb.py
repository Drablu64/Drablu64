#!/usr/bin/python3

import time
import random
import mysql.connector as mysql

print("menghubungkan ke server...")
db = mysql.connect(
    host='sql6.freesqldatabase.com',
    user='sql6702296',
    password='8feBkzUrgl',
    database='sql6702296'
)
c = db.cursor()
nama = input("Masukkan nama: ")
passw = input("Masukkan password: ")
while True:
   try:
      q_select = "SELECT uang, hutang FROM trading WHERE nama = %s AND pass = %s"
      c.execute(q_select, (nama, passw))
      row = c.fetchone()
      if row:
        uang, hutang = row
        uang = uang * 18446744073709551615
        break
      else:
        print("akun tidak di temukan, apakah anda ingin membuat akun dengan user dan pass sebelumnya?(y/n)")
        pi = input("masukan pilihan: ")
        if pi == 'y':
           q_insert = "INSERT INTO trading (nama, pass, uang, hutang) VALUES (%s, %s, %s, %s)"
           c.execute(q_insert, (nama, passw, 500 / 18446744073709551615, 0))
           db.commit()
           print("Akun baru berhasil dibuat.")
        elif pi == 'n':
           print("kembali")
        else:
           print("kembali")
   except:
      print("database belum ada, membuat database baru...")
      q_create = "CREATE TABLE trading (nama text, pass text, uang float, hutang int)"
      c.execute(q_create)
      db.commit()

Alp = {}
while True:
   uang = uang / 18446744073709551615
   q_auto = "UPDATE trading SET uang=%s WHERE nama=%s"
   q_autoh = "UPDATE trading SET hutang=%s WHERE nama=%s"
   c.execute(q_autoh, (hutang, nama))
   c.execute(q_auto, (uang, nama))
   db.commit()
   uang = uang * 18446744073709551615
   
   if -9000 <= uang < 0:
      print("anda mendapatkan bantuan dana dari bank karena bangkrut")
      hutang = hutang + 11000
      uang = 500
   elif uang <= -9001:
      print("anda bangkrut dan bank tidak bisa memberi dana bantuan")
      q_hapus = "DELETE FROM trading WHERE nama=%s"
      c.execute(q_hapus, (nama,))
      db.commit()
      db.close()
      break
      
   if hutang > 11001:
      uang = uang + sum(Alp.values())
      if uang >= 11001:
         Alp.clear()
         print("anda terpaksa menjual semua barang anda untuk membayar hutang")
         uang = uang - hutang
         hutang = 0
      elif -999999999 < uang <= 11001:
         print("anda bangkrut dan bank tidak akan memberi bantuan karena anda terlilit hutang bank")
         break
   print()
   print("pilih aksi")
   print("1. tampilkan profil")
   print("2. beli item")
   print("3. jual item")
   print("4. pinjam uang")
   print("5. keluar")
   print("6. hapus data akun")
   p = input("masukan pilihan: ")
   if p == '1':
      print()
      fuang = "{:,}".format(int(uang))
      fhutang = "{:,}".format(hutang)
      print("uang:", fuang)
      print("hutang:", fhutang)
      print("inventory:")
      for key, value in Alp.items():
         fvalue = "{:,}".format(value)
         print(f"- {key.capitalize()} : {fvalue}")
         
   elif p == '6':
      print("penghapusan data sedang berjalan....")
      q_hapus = "DELETE FROM trading WHERE nama=%s"
      c.execute(q_hapus, (nama,))
      time.sleep(4)
      db.commit()
      db.close()
      break
   elif p == '5':
      print("inventory tidak akan di simpan tolong jual semua isi dari inventory anda terlebih dulu sebelum keluar")
      print("anda yakin ingin keluar?(y/n)")
      pp = input("masukan pilihan: ")
      if pp == 'y':
         db.commit()
         db.close()
         break
   elif p == '2':
      aa = random.randint(1, 10)
      jj = random.randint(1, 10)
      mm = random.randint(1, 15)
      ss = random.randint(1, 12)
      print()
      print("0. kembali")
      print("1. apel harge:", aa)
      print("2. jeruk harga:", jj)
      print("3. melon harga:", mm)
      print("4. semangka harga", ss)
      print("99. custom barang(harga acak)")
      p2 = input("masukan pilihan: ")
      if p2 == '1':
         a = input("mau beli berapa apel: ")
         try:
            if int(a) > 0:
               ht = int(a) * aa
               uang = uang - ht
               try:
                  Alp['apel'] = Alp['apel']+int(a)
               except:
                  Alp['apel'] = int(a)
            else:
               print("tidak dapat membeli barang")
         except:
            print("masukan angka")
      elif p2 == '2':
         j = input("mau beli berapa jeruk: ")
         try:
            if int(j) > 0:
               ht = int(j) * jj
               uang = uang - ht
               try:
                  Alp['jeruk'] = Alp['jeruk']+int(j)
               except:
                  Alp['jeruk'] = int(j)
            else:
               print("tidak dapat membeli barang")
         except:
            print("masukan angka")
      elif p2 == '0':
         print("berhasil kembali")
      elif p2 == '3':
         m = input("mau beli berapa melon: ")
         try:
            if int(m) > 0:
               ht = int(m) * mm
               uang = uang - ht
               try:
                  Alp['melon'] = Alp['melon']+int(m)
               except:
                  Alp['melon'] = int(m)
            else:
               print("tidak dapat membeli barang")
         except:
            print("masukan angka")
      elif p2 == '4':
         s = input("mau beli berapa semangka: ")
         try:
            if int(s) > 0:
               ht = int(s) * ss
               uang = uang - ht
               try:
                  Alp['semangka'] = Alp['semangka']+int(s)
               except:
                  Alp['semangka'] = int(s)
            else:
               print("tidak dapat membeli barang")
         except:
            print("masukan angka")
      elif p2 == '99':
         print()
         print("masukan nama dan jumlah barang yang akan anda beli")
         cc = input("nama barang: ")
         hc = random.randint(1, 11)
         print("barang memiliki harga", hc)
         j = input("jumlah barang: ")
         try:
            if int(j) > 0:
               print("anda akan membeli", j, cc, "dengan harga", hc)
               print("y/n?")
               cp = input("masukan pilihan: ")
               if cp == 'y':
                  ht = int(j) * hc
                  uang = uang - ht
                  Alp[cc] = int(j)
                  print("berhasil membeli", j, cc)
               elif cp == 'n':
                  print("berhasil kembali")
            else:
               print("tidak dapat membeli barang")
         except:
            print("masukan angka")
         
   elif p == '3':
      aj = random.randint(1, 10)
      jl = random.randint(1, 10)
      mj = random.randint(1, 15)
      sj = random.randint(1, 12)
      print()
      print("0. kembali")
      print("1. apel harga:", aj)
      print("2. jeruk harga:", jl)
      print("3. melon harga:", mj)
      print("4. semangka harga:", sj)
      print("99. custom barang:")
      p3 = input("masukan pilihan: ")
      if p3 == '1':
         a = input("mau jual berapa apel: ")
         jt = int(a) * aj
         try:
            if int(a) <= Alp['apel']:
               Alp['apel'] = Alp['apel']-int(a)
               uang = uang + jt
            else:
               print("anda tidak memiliki barang yang dibutuhkan")
         except:
            print("anda tidak memiliki barang yang dibutuhkan")
      elif p3 == '2':
         j = input("mau jual berapa jeruk: ")
         try:
            jt = int(j) * jl
            if int(j) <= Alp['jeruk']:
               Alp['jeruk'] = Alp['jeruk']-int(j)
               uang = uang + jt
            else:
               print("anda tidak memiliki barang yang dibutuhkan")
         except:
            print("anda tidak memiliki barang yang dibutuhkan")
      elif p3 == '0':
         print("berhasil kembali")
      elif p3 == '3':
         m = input("mau jual berapa melon: ")
         try:
            jt = int(m) * mj
            if int(m) <= Alp['melon']:
               Alp['melon'] = Alp['melon']-int(m)
               uang = uang + jt
            else:
               print("anda tidak memiliki barang yang dibutuhkan")
         except:
            print("anda tidak memiliki barang yang dibutuhkan")
      elif p3 == '4':
         s = input("mau jual berapa semangka: ")
         try:
            jt = int(s) * sj
            if int(s) <= Alp['semangka']:
               Alp['semangka'] = Alp['semangka']-int(s)
               uang = uang + jt
            else:
               print("anda tidak memiliki barang yang dibutuhkan")
         except:
            print("anda tidak memiliki barang yang dibutuhkan")
      elif p2 == '99':
         print("masukan nama dan jumlah barang yang akan anda jual")
         cc = input("nama barang: ")
         j = input("jumlah barang: ")
         hj = random.randint(1, 11)
         print("anda akan menjual", j, cc, "dengan harga", hj)
         print("y/n?")
         cp = input("masukan pilihan: ")
         if cp == 'y':
            try:
               if int(j) <= Alp[cc]:
                  ht = int(j) * hj
                  uang = uang - ht
                  Alp[cc] = Alp[cc] + int(j)
                  print("berhasil menjual", j, cc)
               else:
                  print("anda tidak memiliki barang yang dibutuhkan")
            except:
               print("anda tidak memiliki barang yang dibutuhkan")
         elif cp == 'n':
            print("berhasil kembali")
      
   elif p == '4':
      print("0. kembali")
      print("1. 500 uang (200% bunga)")
      print("2. 1000 uang (100% bunga)")
      print("3. 5000 uang (20% bunga)")
      print("4. 10000 uang (10% bunga)")
      print("5. bayar hutang")
      p4 = input("Masukan pilihan: ")
      if p4 == '1':
         uang = uang + 500
         hutang = hutang + 500 * 3
      elif p4 == '2':
         uang = uang + 1000
         hutang = hutang + 1000 * 2
      elif p4 == '3':
         uang = uang + 5000
         hutang = int(hutang + 5000 * 1.2)
      elif p4 == '4':
         uang = uang + 10000
         hutang = int(hutang + 10000 * 1.1)
      elif p4 == '0':
         print("berhasil kembali")
      elif p4 == '5':
         if hutang <= 0:
            print("anda tidak memiliki hutang")
         
         elif hutang > 0:
            print("anda memiliki hutang sebesar", hutang, "di bank")
            bh2 = input("ingin melunasi berapa: ")
            try:
               bh = int(bh2)
               if bh <= hutang:
                  uang = uang - bh
                  hutang = hutang - bh
                  print("berhasil membayar hutang")
               elif bh > hutang:
                  uang = uang - hutang
                  hutang = hutang - hutang
                  print("berhasil membayar hutang")
            except:
               print("masukan angka")