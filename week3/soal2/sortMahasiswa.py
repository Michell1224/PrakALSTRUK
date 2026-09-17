import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="presensi",rev = False):
    maps= {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    
    kolom = maps[index]
    n = len(data)
    
    for i in range(n - 1):
        posisi = i
        
        for j in range(i + 1, n):
            if not rev:            #Ascending
                if data[j][kolom] < data[posisi][kolom]:
                    posisi = j
            else:                  #Descending
                if data[j][kolom] > data[posisi][kolom]:
                    posisi = j
            
        data[i], data[posisi] = data[posisi], data[i]
            
    # Jangan Dihapus
    show_data(data)

sort_by(data)


    
