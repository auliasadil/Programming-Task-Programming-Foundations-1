'''Dibuat oleh Muhammad Aulia Adil
    Program ini berfungsi untuk menghitung distribusi kemunculan kata
pada sebuah himpunan teks. Kata-kata berupa preposisi dan kata penghubung
tidak dihitung karena tugas pemrograman 2 mengharuskan begitu.'''

#Impor matplotlib
import matplotlib.pyplot as plt

#Impor tanda baca dari string
from string import punctuation

#Fungsi ini berfungsi untuk menerima masukkan
def masukkan():
    print('=' * 56)
    print('Masukkan pesan: (untuk berhenti masukkan string kosong)')
    print('=' * 56)
    data_pesan = []
    while True:
        pesan = input('Pesan: ')
        if pesan == '':
            break
        #setiap masukkan akan dimasukkan ke dalam list
        data_pesan.append(pesan)
    return data_pesan

#Fungsi ini membersihkan tanda baca dari pesan-pesan yang dimasukkan
def bersihkan_tanda_baca(data_pesan): 
    data = []
    for pesan in data_pesan:
        #mentokenisasi setiap kalimat menjadi kata
        pesan_split = pesan.split()
        for kata in pesan_split:
            #cek tanda baca dimulai dari sini
            for i in tanda_baca():
                #mendeteksi setiap tanda baca dalam kata
                #jika ada, maka akan dihapus
                if i in kata:
                    #tanda hubung merupakan tanda spesial sehingga harus diberikan perlakuan khusus dan dicek paling akhir
                    if i == '-':
                        kata = cek_kata_sambung(kata)
                    else:
                        kata = kata.replace(i, '')
            #kata yang sudah difilter tanda bacanya, dijadikan kecil setiap hurufnya
            kata = kata.lower()
            #kata bersih dan kecil, dimasukkan ke dalam sebuah list
            data.append(kata)
    return data

'''Fungsi ini berfungsi untuk mendeteksi kata hubung dan membersikan tanda hubung dalam pesan tersebut.
Cara kerjanya adalah jika tanda hubung tersebut berada di pinggiran kata, maka akan dihapus.
Jika tanda hubung tersebut berada di tengah kata, maka tidak akan dihapus. 
Jika tanda hubung tersebut berada dalam emoticon atau tanda-tanda yang lain, maka tanda baca selain tanda hubung
akan dihapus terlebih dahulu sehingga yang paling akhir dihapus adalah tanda hubung.'''
def cek_kata_sambung(kata):
    list_huruf = []
    #memecah kata yang ada tanda hubungnya menjadi huruf-huruf dan huruf-huruf tersebut dimasukkan ke dalam list
    for huruf in kata:
        list_huruf.append(huruf)
    #menghapus tanda hubung yang ada dipinggiran kiri
    while True:
        if list_huruf == []:
            break
        elif list_huruf[0] == '-':
            list_huruf.remove('-')
        else:
            break
    list_huruf.reverse()
    #menghapus tanda hubung yang ada di pinggiran kanan
    while True:
        if list_huruf == []:
            break
        elif list_huruf[0] == '-':
            list_huruf.remove('-')
        else:
            break
    list_huruf.reverse()
    #menyatukan kembali huruf-huruf yang sudah bersih dari tanda hubung pinggiran menjadi kata
    kata = ''.join(list_huruf)
    return kata

#Fungsi ini menjadikan tanda hubung untuk dicek paling akhir
def tanda_baca():
    tanda_baca_baru = punctuation.replace('-', '')
    tanda_baca_baru += '-'
    return tanda_baca_baru

#Fungsi ini berfungsi membersihkan kata penghubung dan preposisi
def cek_stopword(data):
    #copy TP2-stopword text ke dalam folder python 
    stopword = [kata.strip() for kata in open('TP2-stopword.txt')]
    #jika kata-kata tersebut itu ada dalam list kata-kata(data), maka akan dihapus
    for word in stopword:
        while word in data:
            data.remove(word)
    return data

#Fungsi ini berfungsi untuk merapihkan data sehingga kita bisa membuat tabel distribusi kemunculan kata
def merapihkan_data(data):
    frekuensi = []
    data_baru = []
    for kata in data:
        if kata not in data_baru:
            #setiap kata hanya akan muncul sekali dalam tabel
            data_baru.append(kata)
            #setiap kata akan dihitung frekuensi kemunculannya
            frekuensi.append(data.count(kata))
    return data_baru, frekuensi

#Fungsi ini berfungsi untuk mengeluarkan input-input yang telah diproses menjadi tabel dan grafik
def output(data_baru, frekuensi):
    banyak_data = len(data_baru)
    print()
    print('Distribusi frekuensi kata:')
    print('-' * 30)
    print('{:<3s} {:<5s} {:>18s}'.format('No','Kata','Frekuensi'))
    print('-' * 30)
    #bagian ini untuk membuat tabel 
    for i in range(banyak_data):
        print('{:2d}  {:<14s} {:>2d}'.format(i + 1, data_baru[i], frekuensi[i]))
    print('-' * 30)
    #untuk menampilkan hasil dalam grafik
    data_baru.reverse()
    frekuensi.reverse()
    fig, ax = plt.subplots()
    ax.set(xlabel = 'Frekuensi', title = 'Frekuensi Kemunculan Kata')
    ax.barh(data_baru, frekuensi)
    plt.show()

#Inti dari program ini
def main():
    data_pesan = masukkan()
    data = bersihkan_tanda_baca(data_pesan)
    data = cek_stopword(data)
    data_baru, frekuensi = merapihkan_data(data)
    output(data_baru, frekuensi)
        
main()

