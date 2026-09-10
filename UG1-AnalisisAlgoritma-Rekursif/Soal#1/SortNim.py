def InsertRecursive(sorted_array, current_value, current_length):
    # TODO 1: Implementasikan base case, logika komparasi pengurutan sesuai NIM, 
    # dan pemanggilan rekursi fungsi insert.
    if current_length < 0 or sorted_array[current_length] <= current_value:
        sorted_array.insert(current_length + 1, current_value)
        return

    InsertRecursive(sorted_array, current_value, current_length - 1)

def RecursiveFilterSort(data_array, current_length):
    # TODO 2: Implementasikan base case, pemecahan rekursif, dan filter kondisional 
    # untuk memanggil fungsi InsertRecursive sesuai paritas NIM.
    if current_length == 0:
        return []
    
    sorted_array = RecursiveFilterSort(data_array, current_length - 1)

    current_value = data_array[current_length - 1]

    if int(NIM_MAHASISWA[-1]) % 2 == 0:
        if current_value % 2 == 0:
            InsertRecursive(sorted_array, current_value, len(sorted_array) - 1)
    else:
        if current_value % 2 != 0:
            InsertRecursive(sorted_array, current_value, len(sorted_array) - 1)
    return sorted_array

# Ganti Dengan NIM Anda
# Contoh, NIM_MAHASISWA = "71230994" -> nanti outputnya [4, 2, 0] 
NIM_MAHASISWA = "71251198"

if NIM_MAHASISWA != "":
    raw_data = [int(digit) for digit in NIM_MAHASISWA]
    data_length = len(raw_data)
    
    final_result = RecursiveFilterSort(raw_data, data_length)

    # TODO 3: cetak hasil akhir sesuai format yang diminta.
    print("==== FILTER & SORT NIM ====")
    print("NIM Mahasiswa:", NIM_MAHASISWA)

    if int(NIM_MAHASISWA[-1]) % 2 == 0:
        print("TIpe           : GENAP (Ascending)")
    else:
        print("TIpe           : GANJIL (Descending)")

    print("DAta Digit Awal : ", raw_data)
    print("Hasil Akhir     : ", final_result)