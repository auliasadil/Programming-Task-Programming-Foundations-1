#aksesoris untuk tampilan awal
def aksesoris1():
    print('~' * 70)

#aksesoris setelah membuka file 
def aksesoris2():
    print('-' * 167)

def aksesoris3():
    print('-')
    
#Untuk mengecek berkas tersebut ada atau tidak
def cek_berkas(berkas):
    import csv
    try:
##        with open('C:\\Users\dell\AppData\Local\Programs\Python\Python37-32\\budaya.csv', newline='') as csvfile:
        with open(berkas, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        return True
    
    #Jika file tidak ditemukan, maka program akan mengharuskan user untuk memasukkan file lagi
    except FileNotFoundError:
        print('Berkas tidak ditemukan, silahkan coba lagi.')
        return False

#Untuk mempermudah semua simulasi dari program ini
def PRO_GAMER_MOVE(data_budaya):
    aksesoris2()
    print('Perintah CARINAMA')
    aksesoris3()
    carinama('*', data_budaya)
    aksesoris3()
    carinama('Rendang', data_budaya)
    aksesoris3()
    carinama('Samba', data_budaya)
    aksesoris2()
    print('Perintah CARITIPE')
    aksesoris3()
    caritipe('Makanan', data_budaya)
    aksesoris3()
    caritipe('break dance', data_budaya)
    aksesoris2()
    print('Perintah CARIPROV')
    aksesoris3()
    cariprov('Aceh', data_budaya)
    aksesoris3()
    cariprov('Timor timor', data_budaya)
    aksesoris2()
    print('Perintah STAT')
    aksesoris3()
    stat(data_budaya)
    aksesoris2()
    print('Perintah STATTIPE')
    aksesoris3()
    stattipe(data_budaya)
    aksesoris2()
    print('Perintah STATPROV')
    aksesoris3()
    statprov(data_budaya)
    aksesoris2()
    print('Perintah TAMBAH')
    aksesoris3()
    tambah('Orange Justice Dance;Tarian;Fortnite;www.progamer.com', data_budaya)
    aksesoris3()
    tambah('Orange Justice Dance:Tarian;Fortnite;www.progamer.com', data_budaya)
    aksesoris3()
    tambah('Rendang;Tarian;Fortnite;www.progamer.com', data_budaya)
    aksesoris3()
    carinama('*', data_budaya)
    aksesoris2()
    print('Perintah UPDATE')
    aksesoris3()
    update('Orange Justice Dance;Breakdance;Fortnite;www.progamer.com', data_budaya)
    aksesoris3()
    update('Random:tes:tes:tes', data_budaya)
    aksesoris3()
    update('Flosh Dance;Tarian;Amerika;www.america.com', data_budaya)
    aksesoris3()
    carinama('*', data_budaya)
    aksesoris2()
    print('Perintah HAPUS')
    aksesoris3()
    hapus('Orange Justice Dance', data_budaya)
    aksesoris3()
    hapus('Flosh Dance', data_budaya)
    aksesoris3()
    carinama('*', data_budaya)

#untuk mengekstrak berkas menjadi list of list
def ekstrak_berkas(berkas):
    import csv
    with open('C:\\Users\dell\AppData\Local\Programs\Python\Python37-32\\budaya.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        data_budaya = [datum_budaya for datum_budaya in spamreader]
    banyak = len(data_budaya)
##    print('Terimpor', banyak, 'baris.')
    aksesoris2()
    
    #silahkan diprint untuk melihat hasilnya
##    print(data_budaya)
    
    return data_budaya

#fungsi ini menjadikan program dapat mencari sebuah warisan budaya yang diinginkan
def carinama(objek, data_budaya):

    #menggunakan dictionary untuk mempermudah pencarian
    dict_nama = {nama:[tipe,prov,referensi] for nama,tipe,prov,referensi in data_budaya}
##    print(dict_nama)

    #jika input user adalah '*' maka program akan menampilkan semua warisan budaya yang ada di file
    if objek == '*':
        for datum in data_budaya:
            print(', '.join(datum))
    #input(objek) dikapitalisasi huruf awalnya untuk berjaga-jaga jika user tidak menggunakan penulisan yang benar
    elif objek.capitalize() in dict_nama:
        print(objek.capitalize(), ', '.join(dict_nama[objek.capitalize()]), sep = ', ')

    #jika warisan budaya yang diinginkan tidak ada
    else:
        print('Warisan budaya tersebut tidak ada dalam berkas ini.')

#fungsi ini menjadikan program dapat menampilkan semua warisan budaya sesuai tipe yang diinginkan
def caritipe(objek, data_budaya):
    tipe = [budaya for budaya in data_budaya if objek.capitalize() in budaya]
    banyak = len(tipe)
    if banyak > 0:
        for i in tipe:
            print(', '.join(i))
        print('*Ditemukan', banyak, objek + '*')
    else:
        print('Tipe tidak ditemukan dalam berkas ini.')

#fungsi ini menjadikan program dapat menampilkan semua warisan budaya sesuai provinsi yang diinginkan
def cariprov(objek, data_budaya):
    prov = [budaya for budaya in data_budaya if objek in budaya]
    banyak = len(prov)
    if banyak > 0:
        for i in prov:
            print(', '.join(i))
        print('*Ditemukan', banyak, 'warisan budaya*')
    else:
        print('Budaya provinsi tersebut tidak ditemukan dalam berkas ini. Pastikan penulisan huruf kapital pada nama provinsi tersebut.')

#fungsi ini menampilkan jumlah warisan budaya yang ada di file tersebut
def stat(data_budaya):  
    banyak = len(data_budaya)
    print('Terdapat', banyak, 'warisan budaya.')

#fungsi ini menampilkan statistik dari yang terbanyak hingga tersedikit berdasarkan tipe yang ada di file tersebut 
def stattipe(data_budaya):

    #menggabungkan semua list of list menjadi list
    list_kata = [a for i in data_budaya for a in i]
    data = []
    for datum in data_budaya:

        #menjadikan tuple antara banyak tipe tersebut dan tipenya
        tup_tipe = list_kata.count(datum[1]), datum[1]
        if tup_tipe not in data:
            data.append(tup_tipe)

    #karena banyak tipe ada di paling kiri, sehingga bisa diurutkan berdasarkan hal tersebut 
    data.sort()
    #dan setelah itu dibalik sehingga yang paling besar ada di depan
    data.reverse()

    #membuat list yang dengan tuple yang dibalik sekarang(tipe, banyak_tipe)
    data = [ (tipe,counter) for counter,tipe in data]
    print(data)

#fungsi ini menampilkan statistik dari yang terbanyak hingga tersedikit berdasarkan asal provinsi yang ada di file tersebut. Cara kerja mirip dengan fungsi stattipe
def statprov(data_budaya):
    list_kata = [a for i in data_budaya for a in i]
    data = []
    for datum in data_budaya:
        tup_tipe = list_kata.count(datum[2]), datum[2]
        if tup_tipe not in data:
            data.append(tup_tipe)
    data.sort()
    data.reverse()
    data = [ (prov,counter) for counter,prov in data]
    print(data)

#fungsi ini menambahkan datum warisan budaya kedalam list of list data_budaya
def tambah(objek, data_budaya):
    objek = objek.split(';')

    #jika file tersebut tidak sesuai aturan maka 
    if len(objek) != 4:
        print('Format salah.')

    #yang pertama dilakukan adalah mengkapitalisasi huruf awal dari setiap input
    else:
        data = [i.split() for i in objek]
        data1 = []
        data2 = []
        for i in range(len(data) - 1):
            for a in data[i]:
                data1.append(a.capitalize())
            data3 = data1[:]
            data2.append(' '.join(data3))
            data1.clear()
        #kecuali referensi url
        data2.extend(data[3])

        #sebuah dictionary dibuat dari data_budaya
        dict_nama = {nama:[tipe,prov,referensi] for nama,tipe,prov,referensi in data_budaya}

        #jika warisan budaya tersebut tidak ada dalam dictionary, maka akan dimasukkan ke dalam data_budaya
        if data2[0] not in dict_nama:
            data_budaya.append(data2)
            print(data2[0], 'ditambahkan.')

        #jika ternyata warisan budaya tersebut sudah ada di dalam dictionary, maka program akan mengusulkan perintah tambah
        else:
            print('Budaya tersebut sudah ada file ini(', data2[0], ', ', ', '.join(dict_nama[data2[0]]),'). Coba perintah "update".', sep = '')

#fungsi ini menambahkan datum warisan budaya kedalam list of list data_budaya. Cara kerjanya mirip dengan fungsi 'tambah'
def update(objek, data_budaya):
    objek = objek.split(';')
    if len(objek) != 4:
        print('Format salah.')
    else:
        data = [i.split() for i in objek]
        data1 = []
        data2 = []
        for i in range(len(data) - 1):
            for a in data[i]:
                data1.append(a.capitalize())
            data3 = data1[:]
            data2.append(' '.join(data3))
            data1.clear()
        data2.extend(data[3])
        dict_nama = {nama:[tipe,prov,referensi] for nama,tipe,prov,referensi in data_budaya}
        if data2[0] not in dict_nama:
            print('Budaya tidak diketahui. Coba perintah "tambah".')
        else:
            for i in range(len(data_budaya)):
                if data2[0] in data_budaya[i]:
                    data_budaya[i] = data2[:]
            print(data2[0], 'diupdate.')
            
#fungsi ini berfungsi untuk menghapus warisan budaya yang ada di list of list data_budaya
def hapus(objek, data_budaya):
    before = len(data_budaya)

    #Mengkapitalisasi setiap kata pada input(objek) yang diberikan
    list_objek = objek.split()
    list_objek = [i.capitalize() for i in list_objek]
    objek = ' '.join(list_objek)

    #jika warisan budaya tersebut memang ada di list of list data_budaya, maka warisan budaya tersebut akan dihapus
    for i in data_budaya:
        if objek in i[0]:
            data_budaya.remove(i)
    after = len(data_budaya)

    #sebagai indikator apakah warisan budaya tersebut memang ada di file atau tidak
    if before > after:
        print(objek.capitalize(), 'dihapus.')
    else:
        print(objek.capitalize(), 'tidak ada dalam file ini.')

#fungsi ini berfungsi untuk menyimpan list of list data_budaya ke file 
def save(berkas, data_budaya):

    #caranya adalah dengan meng-overwrite file lama dengan yang baru
    import csv
    with open(berkas, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for budaya in data_budaya:
            spamwriter.writerow(budaya)
    print('Berhasil disimpan.')

#fungsi ini berfungsi untuk menyimpan list of list data_budaya ke file baru
def saveas(objek, data_budaya):
    import csv
    with open(objek, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for budaya in data_budaya:
            spamwriter.writerow(budaya)
    print('Berhasil disimpan.')
        
#untuk memberitahu user macam-macam perintah yang ada dalam program
def macam_perintah():
    print('Macam-macam Perintah:')
    print(' 1. carinama $nama                           --> Mencari data berdasarkan $nama budaya tersebut. Ketik $nama = * untuk menampilkan semua budaya.')
    print(' 2. caritipe $nama                           --> Mencari data berdasarkan $nama tipe budaya tersebut.')
    print(' 3. cariprov $nama                           --> Mencari data berdasarkan $nama asal provinsi budaya tersebut.')
    print(' 4. stat                                     --> Menampilkan jumlah total warisan budaya.')
    print(' 5. stattipe                                 --> Menampilkan jumlah warisan budaya per tipe yang diurutkan dari terbanyak ke tersedikit.')
    print(' 6. statprov                                 --> Menampilkan jumlah warisan budaya per provinsi yang diurutkan dari terbanyak ke tersedikit.')
    print(' 7. tambah nama;tipe;provinsi;referenceurl   --> Menambahkan data budaya. Contoh Rendang;Makanan;Sumatra Barat;http://dbpedia.org/resource/Rendang')
    print(' 8. update nama;tipe;provinsi;referenceurl   --> Memperbarui data budaya. Tipe, provinsi, dan referenceurl yang lama akan diganti/ditimpa dengan yang baru.')
    print(' 9. hapus $nama                              --> Menghapus data $nama budaya tersebut.')
    print('10. save                                     --> Menyimpan file yang telah diperbarui.')
    print('11. saveas $nama                             --> Menyimpan file yang telah diperbarui dengan membuat file baru dengan judul $nama(disimpan dengan jenis .csv).')
    print('12. openfile $nama                           --> Membuka file baru.')
    print('13. keluar                                   --> Keluar dari program ini.')
    aksesoris2()
    
#inti dari program ini    
def main():

    #sebagai pembuka
    aksesoris1()
    print('BudayaKB Lite v1.0')
    print('~Kalau bukan kita yang melestarikan budaya, siapa lagi?~')
    aksesoris1()

    print('Hanya untuk jenis file csv')
    while True:
        berkas = input('> Open file(tambah ".csv" di belakang nama file): ')

        #untuk mengecek file apakah ada atau tidak di dalam directory 
        while cek_berkas(berkas):

            #jika benar ada, maka file tersebut akan ekstrak ke dalam variabel data_budaya
            data_budaya = ekstrak_berkas(berkas)
            macam_perintah()

            #program dengan berbagai macam fiturnya 
            while True:
                try:
                    
                    #masukkan berjumlah minimal 1 dan jika lebih maka akan di .split() dan dijadikan list
                    masukkan = input('> Masukkan perintah: ')
                    masukkan = masukkan.split()

                    #index 0 list akan dijadikan perintah dan index 1 list akan dijadikan input(objek)
                    perintah = masukkan[0]
                    objek = ' '.join(masukkan[1:])
                    
                    if perintah.lower() == 'pro-gamer_move' :
                        PRO_GAMER_MOVE(data_budaya)
                    elif perintah.lower() == 'carinama':
                        carinama(objek, data_budaya)
                    elif perintah.lower() == 'caritipe':
                        caritipe(objek, data_budaya)
                    elif perintah.lower() == 'cariprov':
                        cariprov(objek, data_budaya)
                    elif perintah.lower() == 'stat':
                        stat(data_budaya)
                    elif perintah.lower() == 'stattipe':
                        stattipe(data_budaya)
                    elif perintah.lower() == 'statprov':
                        statprov(data_budaya)
                    elif perintah.lower() == 'tambah':
                        tambah(objek, data_budaya)
                    elif perintah.lower() == 'update':
                        update(objek, data_budaya)
                    elif perintah.lower() == 'hapus':
                        hapus(objek, data_budaya)
                    elif perintah.lower() == 'save':
                        save(berkas, data_budaya)
                    elif perintah.lower() == 'saveas':
                        saveas(objek, data_budaya)

                    #perintah ini berfungsi untuk membuka file baru
                    elif perintah.lower() == 'openfile':
                        berkas = objek
                        if cek_berkas(berkas):
                            break
                        else:
                            pass

                    #perintah ini berfungsi untuk keluar dari program
                    elif perintah.lower() == 'keluar':
                        print('Sampai Jumpa! Cintailah budaya-budaya Indonesia~')
                        exit()
                    else:
                        print('Perintah tidak diketahui.')
                    aksesoris2()

                #jika masukkan hanya menerima satu kata dan kata tersebut tidak diketahui, maka akan terjadi exception ini
                except IndexError:
                    print('Perintah tidak diketahui.')
                    aksesoris2()
                    pass

main()
            
        

    


