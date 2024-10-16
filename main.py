# Program Alat Bantu Pembuangan Sampah yang Benar!
# Program ini dituju untuk Masyarakat yang masih membuang sampah sembarangan
import time

register = input('Silahkan Masukkan Nama Anda: ')

opsi_sampah = (1, 2, 3, 4)

while True:
    print('')
    print('Halo ' + register + ',' + ' Selamat Datang!')
    print('^_ MENU _^')
    print('!SILAHKAN PILIH LIMBAH YANG INGIN ANDA KETAHUI!')
    print('1 = Organik')
    print('2 = Anorganik')
    print('3 = Bahan Beracun dan Berbahaya')
    print('4 = Exit Program')

    print('')
    input_sampah = int(input('Silahkan Pilih Opsi (1/2/3/4) '))

    if input_sampah in opsi_sampah:
        break
    else:
        print()
        print('Opsi Tidak Tersedia')
        time.sleep(2)

if input_sampah == 1:
    print('')
    print('^_SAMPAH ORGANIK_^')
    print('1. Pengertian Sampah Organik')
    print('2. Jenis Sampah Organik Basah dan Kering')
    print('3. Apa Saja Jenis Jenis Sampah Organik')
    print('4. Dampak dari Sampah Organik')
    print('5. Cara Mengelola Sampah Organik')
    print('6. Exit Program')


    opsiOrganik = (1, 2, 3, 4, 5, 6)
    print()
    inputOrganik = int(input('Silahkan Pilih Opsi (1/2/3/4/5/6) '))
    if inputOrganik in opsiOrganik:
        print()
    else: 
        print('Opsi Tidak Ditemukan.')
        time.sleep(2)
        exit()

    if inputOrganik == 1:
        print()
        print('Sampah organik adalah sampah yang berasal dari sisa-sisa makhluk hidup, baik hewan, tanaman, maupun manusia. Pada dasarnya, jenis sampah ini bisa terurai secara alamiah di alam juga bisa dimanfaatkan menjadi hal-hal lain, seperti kompos dan lainnya.')
        
    elif inputOrganik == 2:
        print('Sampah organik bisa dibagi lagi menjadi dua jenis, yaitu sampah organik kering dan basah.')
        print('')
        print('Jenis sampah organik kering memiliki kandungan air yang sedikit hingga tidak ada, contohnya adalah ranting pohon, dedaunan kering, tulang belulang, dsb.')
        print('Jenis sampah organik basah memiliki kandungan air yang cukup tinggi, membuatnya lebih cepat membusuk dan dapat terurai lebih cepat dibandingkan sampah kering. Contoh sampah organik basah adalah sisa sayuran, buah-buahan, dsb.')

    elif inputOrganik == 3:
        print('Perbedaan antara organik dan anorganik sebenarnya cukup sederhana.')
        print('Jika melihat dari karakteristiknya, sampah organik adalah jenis sampah yang terdiri dari bahan-bahan yang berasal dari hewan dan tumbuhan serta beberapa diantaranya mudah hancur apabila tertinggal di alam.')
        print('')
        print('Sampah anorganik terdiri dari bahan yang bukan berasal dari hewan dan tumbuhan serta tidak mudah hancur secara alami apabila tertinggal di alam.')
        print('Oleh karena itu, sampah anorganik perlu dikelola dengan bantuan mesin. Namun, perlu diketahui bahwa penumpukan sampah merupakan masalah yang menjadikan sampah dapat merusak lingkungan.')

    elif inputOrganik == 4:
        print('')
        print('Selain berbahaya bagi kesehatan, sampah organik juga memberikan dampak buruk bagi lingkungan. Dampak sampah organik bagi lingkungan adalah sebagai berikut.')
        print('')
        print('^_DAMPAK BAGI KESEHATAN_^')
        print('1. Tempat Bersarangnya Hewan Penyakit')
        print('2. Menyebabkan Penyakit pada Hewan Ternak')
        print('')
        print('^_DAMPAK BAGI LINGKUNGAN SEKITAR_^')
        print('1. Tercemarnya Sumber Air')
        print('2. Lingkungan Menjadi Kumuh')
        print('3. Polusi Udara (bau yang tidak enak)')

    elif inputOrganik == 5:
        print('1. Mengumpulkan Sampah')
        print('Kumpulkan Sampah Organik untuk Dijadikan Kompos')
        print('')
        print('2. Proses Pencahan')
        print('Setelah Mengumpulkan Sampah Organik, Lakukan Proses Pencahan agar Sampah Menjadi Lebih Lembut')
        print('')
        print('3. Proses Pendiaman')
        print('Masukkan Sampah-sampah kedalam wadah. Agar bisa menjadi pukuk kompos, tunggu sampah organik yang sudah dicacah agar terjadi pembusukkan')
        print('')
        print('4. Tutup Rapat')
        print('Sampah Organik harus didiamkan di tempat yang tertutup rapat dan kedap udara')
        print('')
        print('5. Tunggu Sampai 2 Minggu')
        print('Tunggu selama 2 minggu agar pembusukan pupuk sempurna')

    elif inputOrganik == 6:
        print('Menutup Program..')
        time.sleep(2)
        print('Selamat Tinggal, Terimakasih Telah Menggunakan Program Ini!')
        exit()

if input_sampah == 2:
        print()
        print('')
        print('^_SAMPAH ANORGANIK_^')
        print('1. Apa Itu Sampah Anorganik')
        print('2. Jenis Sampah Anorganik ')
        print('3. Perbedaan Sampah Anorganik dengan Organik')
        print('4. Tahapan Mengelola Sampah Anorganik')
        print('5. Exit Program')

        opsiAnorganik = (1, 2, 3, 4, 5)
        inputAnorganik = int(input('Silahkan Pilih Opsi (1/2/3/4/5) '))
        
        if inputAnorganik in opsiAnorganik:
            print()
        else:
            print('Opsi Tidak Ditemukan')

        if inputAnorganik == 1:
            print('')
            print('Sampah anorganik adalah semacam sampah atau sisa bahan yang tidak mudah membusuk yang lazimnya bukan bermula dari hewan dan tumbuhan.')
            print('Sampah anorganik dapat berupa plastik, botol beling atau kaca, kaleng, kertas, dan pembungkus makanan lainnya.')
        
        elif inputAnorganik == 2:
            print('')
            print('1. Anorganik Padat')
            print('Limbah yang bentuknya keras, padat, dan bisa disentuh atau dipegang. Limbah anorganik padat ada pula yang tak bisa disentuh sebab terdapat kandungan zat kimia berbahaya di dalamnya. Adapun contoh dari limbah anorganik padat, yaitu alumunium, besi, basa, botol belong, plastik, dan beberapa barang sejenisnya.')
            print('')
            print('2. Anorganik Cair')
            print('Limbah Anorganik cair berupa cairan sangat berbahaya yang berasal dari suatu pabrik ataupun perusahaan produksi. Umumnya, pabrik atau perusahaan produksi tersebut mengalirkan limbah anorganik cair ini ke sungai-sungai sehingga makhluk hidup yang tinggal di situ dan lingkungan setempatnya akan rusak serta tercemar.')
            print('')
            print('3. Anorganik Gas')
            print('Limbah anorganik gas atau angin adalah limbah yang tidak dapat terjamah oleh indra. Umumnya, limbah anorganik gas ini berasal dari cerobong asap di pabrik-pabrik produksi. Asap atau uap tersebut sangat berbahaya karena bisa mengakibatkan bumi semakin panas, rentan akan hujan asam, dan berbagai polusi udara akan semakin bertambah.')

        elif inputAnorganik == 3:
            print('')
            print('Sampah organik mudah terurai di alam (busuk), seperti sisa makanan, daun, ranting. Sampah organik juga dapat diproses menjadi pupuk kompos. Kemudian tempat sampah organik ditandai berwarna hijau.')
            print('Sedangkan, sampah anorganik adalah sulit terurai, seperti plastik, kaleng, styrofoam. Hasil dari sampah ini bisa diolah menjadi kerajinan atau didaur ulang di pabrik. Untuk tempat sampah anorganik biasanya ditandai berwarna kuning.')

        elif inputAnorganik == 4:
            print('')
            print('Kita Dapat Mengelola Sampah Dengan Prinsip 3R (Reuse, Reduce, Recycle)')
            print('Berikut Langkahnya')
            print('')
            print('1. Reuse (Penggunaan Kembali)')
            print('Reuse adalah menggunakan kembali sampah secara langsung, dengan fungsi yang masih sama ataupun fungsi yang beda.')
            print('')
            print('2. Reduce (Pengurangan)')
            print('Reduce adalah pengurangan segala kegiatan yang dapat menimbulkan sampah')
            print('')
            print('3. Recycle (Daur Ulang)')
            print('Recycle adalah pemanfaatan kembali sampah dengan beberapa tahapan pengolahan.')

        elif inputAnorganik == 5:
            print('Menutup Program..')
            time.sleep(2)
            print('Selamat Tinggal, Terimakasih Telah Menggunakan Program Ini!')
        exit()

if input_sampah == 3:
    print('')
    print('^_LIMBAH B3 (BAHAN BERACUN DAN BEBAHAYA)_^')
    print('1. Apa Itu Limbah B3')
    print('2. Jenis-Jenis Limbah B3')
    print('3. Karakteristik Limbah B3')
    print('4. Exit Program')

    opsiB3 = (1, 2, 3 ,4)
    inputB3 = int(input('Silahkan Pilih Opsi (1/2/3/4) '))

    if inputB3 in opsiB3:
        print()
    else:
        print('Opsi Tidak Ditemukan')
    
    if inputB3 == 1:
        print('Limbah B3 adalah limbah yang mengandung zat yang sifat konsentrasinya beracun, yang dapat membahayakan kesehatan manusia, dan mencemarkan lingkungan sekitar')
    
    elif inputB3 == 2:
        print('1. Baterai Bekas')
        print('2. Lampu TL dan Bohlam')
        print('3. Oli Bekas')
        print('4. Aki Bekas')
        print('5. Toner Bekas')
        print('6. E-Waste')
    
    elif inputB3 == 3:
        print('1. Mudah Meledak (Explosive - E)')
        print('Limbah B3 (Explosive E) adalah Limbah yang pada suhu dan tekanan standar yaitu 25oC   atau 760 mmHg dapat meledak, atau melalui reaksi kimia dan/atau fisika dapat menghasilkan gas dengan suhu dan tekanan tinggi yang dengan cepat dapat merusak lingkungan sekitarnya.')
        print('')
        print('2. Mudah Menyala (Ignitable - I)')
        print('Limbah B3 (Ignitable -I) dalam bentuk cairan dengan kandungan alkohol kurang dari 24% volume pada titik nyalanya. Limbah B3 juga biasanya tidak lebih dari 140oF atau 60oC yang kemudian akan menyala jika terjadi kontak langsung dengan percikan api atau berbagai sumber menyala lain dalam tekanan udara 760 mmHg.')
        print('')
        print('3. Reaktif (Reactive - R)')
        print('Limbah B3 reaktif merupakan Limbah yang tidak stabil bahkan dalam keadaan normal sekalipun, limbah ini dapat membuat perubahan tanpa meledak. Limbah ini secara visual menunjukkan perubahan warna, gelembung gas, asap, dan jika tercampur dengan air mampu menimbulkan ledakan, juga menghasilkan uap, gas, atau asap.')
        print('')
        print('4. Infeksius (Infectious - X)')
        print('Limbah B3 juga bersifat infeksius khususnya pada limbah medis padat yang terkontaminasi organisme patogen dalam jumlah dan virulensi yang cukup mampu menularkan berbagai penyakit pada manusia.')
        print('')
        print('5. Korosif (Corrosive - C)')
        print('Limbah B3 Corrosive atau Limbah B3 dengan kandungan pH sama atau kurang dari 2. Sifat korosif dari Limbah padat sendiri dilakukan dengan mencampurkan Limbah dengan air sesuai dengan metode-metode yang berlaku dan jika limbah dengan pH terkecil atau sama dengan 2')
        print('')
        print('6. Beracun (Toxic - T)')
        print('Limbah B3 Toxic merupakan Limbah yang telah diuji ketentuan karakteristiknya melalui Uji Toksikologi LD50, TCLP, dan uji subkronis. Penentuan karakteristik beracunnya diidentifikasi jika limbah ini memiliki konsentrasi zat pencemar yang lebih besar dari TCLP-A.')
    
    elif inputB3 == 4:
        print('Menutup Program..')
        time.sleep(2)
        print('Selamat Tinggal, Terimakasih Telah Menggunakan Program Ini!')
        exit

if input_sampah == 4:
    print('Terimakasih Telah Menggunakan Program Ini!')
    print('Program Akan Ditutup Dalam (2) detik.')
    time.sleep(2)
    exit()