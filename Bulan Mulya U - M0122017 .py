import datetime
waktu=datetime.date.today()
year=waktu.year
month=waktu.month
day=waktu.day
while True:
        if day<10:
                day='0{0}'.format(day)
                if month<10:
                        month='0{0}'.format(month)
                        break
                else:
                        month=month
                        break
                break
        else:
                if month<10:
                        month='0{0}'.format(month)
                        break
                else:
                        month=mont
                        break
                day=day
                break
hariini='{0}-{1}-{2}'.format(day,month,year)

#inputan
nik=int(input('NIK : '))
digit=len(str(abs(nik)))
while (digit!=16):
        print ('NIK salah, masukkan ulang')
        nik=int(input('NIK : '))
        digit=len(str(abs(nik)))
nama=str(input('Nama Lengkap : '))
nama=nama.upper()
tempatlahir=str(input('Tempat Lahir : '))
tempatlahir=tempatlahir.upper()
tanggallahir=input('Tanggal Lahir (DDMMYYYY) : ')
tanggallahir=datetime.datetime.strptime(tanggallahir, '%d%m%Y')
hari=tanggallahir.day
bulan=tanggallahir.month
tahun=tanggallahir.year
while True:
        if hari<10:
                hari='0{0}'.format(hari)
                if bulan<10:
                        bulan='0{0}'.format(bulan)
                        break
                else:
                        bulan=bulan
                        break
                break
        else:
                if bulan<10:
                        bulan='0{0}'.format(bulan)
                        break
                else:
                        bulan=bulan
                        break
                hari=hari
                break
tanggallahir='{0}-{1}-{2}'.format(hari,bulan,tahun)
while True:
	jeniskelamin=str(input('Jenis Kelamin (pilih L/P) : '))
	if jeniskelamin in ['L', 'l']:
		jeniskelamin='LAKI-LAKI'
		break
	elif jeniskelamin in ['P','p']:
		jeniskelamin='PEREMPUAN'
		break
	print('Jenis Kelamin salah, masukkan ulang')
while True:
        golongandarah=str(input('Golongan Darah : '))
        if golongandarah in ['A', 'a']:
                golongandarah='A'
                break
        elif golongandarah in ['B','b']:
                golongandarah='B'
                break
        elif golongandarah in ['O','o']:
                golongandarah='O'
                break
        elif golongandarah in ['AB','Ab','aB','ab']:
                golongandarah='AB'
                break
        print('Golongan Darah tidak ditemukan, masukkan ulang')
provinsi=str(input('Provinsi : '))
provinsi=provinsi.upper()
while True:
	kota=str(input('Kabupaten/Kota (pilih 1/2) : '))
	if kota=='1':
		kota='KABUPATEN'
		namakota=str(input('Nama Kabupaten : '))
		namakota=namakota.upper()
		namkot=namakota
		break
	elif kota=='2':
		kota='KOTA'
		namakota=str(input('Nama Kota : '))
		namakota=namakota.upper()
		namkot=namakota
		break
	print('pilih Kabupaten atau Kota dengan benar, masukkan ulang')
kecamatan=str(input('Kecamatan : '))
kecamatan=kecamatan.upper()
kelurahan=str(input('Kelurahan/Desa : '))
kelurahan=kelurahan.upper()
rt=int(input('RT : '))
rw=int(input('RW : '))
alamat=str(input('Alamat : '))
alamat=alamat.upper()
agama=str(input('Agama : '))
agama=agama.upper()
status=str(input('Status Perkawinan : '))
status=status.upper()
pekerjaan=str(input('Pekerjaan : '))
pekerjaan=pekerjaan.upper()
while True:
        kewarganegaraan=str(input('Kewarganegaraan : '))
        if kewarganegaraan in ['Indonesia','indonesia','INDONESIA','wni','WNI']:
                kewarganegaraan='WNI'
                masaberlaku='SEUMUR HIDUP'
                break
        else :
                kewarganegaraan=kewarganegaraan.upper()
                year+=5
                masaberlaku='{0}-{1}-{2}'.format(day,month,year)
                break
print()

#outputan
print('{0}KTP {0}'.format(' '*33))
print('{0}'.format('-'*70))
print('|{0}|'.format(' '*68))
provinsi='PROVINSI {}'.format(provinsi)
while True:
        if (int(len(provinsi))%2==1):
                provinsi='{0} '.format(provinsi)
                a=int((68-int(len(provinsi)))/2)
                break
        else:                                
                a=int((68-int(len(provinsi)))/2)
                break
print('|{0}{1}{0}|'.format(' '*a,provinsi))
namakota='{0} {1}'.format(kota,namakota)
while True:
        if (int(len(namakota))%2==1):
                namakota='{0} '.format(namakota)
                b=int((68-int(len(namakota)))/2)
                break
        else:
                b=int((68-int(len(namakota)))/2)
                break
print('|{0}{1}{0}|'.format(' '*b,namakota))
print('|{0}|'.format(' '*68))
nik="|  NIK          : {0}".format(nik)
print("{0}{1}|".format(nik,' '*int(69-int(len(nik)))))
print('|{0}------------  |'.format(' '*54))
nama='|  Nama             :{0}'.format(nama)
print("{0}{1}|          |  |".format(nama,' '*int(55-int(len(nama)))))
ttl='|  Tempat/Tgl Lahir :{0}, {1}'.format(tempatlahir,tanggallahir)
print("{0}{1}|          |  |".format(ttl,' '*int(55-int(len(ttl)))))
jeniskelamin='|  Jenis kelamin    :{0}'.format(jeniskelamin)
golongandarah='      Gol. Darah :{0}'.format(golongandarah)
jekgol=int(len(jeniskelamin))+int(len(golongandarah))
print('{0}{1}{2}|          |  |'.format(jeniskelamin,golongandarah,' '*int(55-int(jekgol))))
alamat='|  Alamat           :{0}'.format(alamat)
print("{0}{1}|          |  |".format(alamat,' '*int(55-int(len(alamat)))))
rtrw='|      RT/RW        :{0}/{1}'.format(rt,rw)
print('{0}{1}|   FOTO   |  |'.format(rtrw,' '*int(55-int(len(rtrw)))))
kelurahan="|      Kel/Desa     :{0}".format(kelurahan)
print('{0}{1}|          |  |'.format(kelurahan,' '*int(55-int(len(kelurahan)))))
kecamatan="|      Kecamatan    :{0}".format(kecamatan)
print('{0}{1}|          |  |'.format(kecamatan,' '*int(55-int(len(kecamatan))))) 
agama="|  Agama            :{0}".format(agama)
print("{0}{1}|          |  |".format(agama,' '*int(55-int(len(agama)))))
status="|  Status Perkawinan:{0}".format(status)
print("{0}{1}------------  |".format(status,' '*int(55-int(len(status)))))
pekerjaan="|  Pekerjaan        :{0}".format(pekerjaan)
while True:
        if (int(len(namkot))%2==1):
                namkot='{0} '.format(namkot)
                c=int((16-int(len(namkot)))/2)
                break
        else:
                c=int((16-int(len(namkot)))/2)
                break
print("{0}{1}{2}{3}{2}|".format(pekerjaan,' '*int(53-int(len(pekerjaan))),' '*c,namkot))
kewarganegaraan="|  Kewarganegaraan  :{0}".format(kewarganegaraan)
print("{0}{1} {2}   |".format(kewarganegaraan,' '*int(55-int(len(kewarganegaraan))),hariini))
masaberlaku="|  Berlaku Hingga   :{0}".format(masaberlaku)
print("{0}{1}|".format(masaberlaku,' '*int(69-int(len(masaberlaku)))))
print('|{0}TTD       |'.format(' '*58))
print('|{0}|'.format(' '*68))
print('-'*70)
