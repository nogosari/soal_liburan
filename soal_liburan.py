
NAMA     : HARITS JAUZA FATHIFALDI
NIM      : A11.2019.11745
KELOMPOK : A11.4118


import os,sys
def soal1() :
    print("SOAL LIBURAN - 1 \n")
    situs = input("Masukkan Nama Situs = ")
    split1=situs.split("//")

    if split1[0] == "http:" :
        split2 = split1[1].split(".")
    elif split1[0] == "https:" :
        split2 = split1[1].split(".")
    else :
        split2 = situs.split(".")
    
    if split2[0]== "www" :
        print ("Output = ", split2[1])
    else :
        print ("Output = ", split2[0])
    print("=======================================\n")

def soal2() :
    print("SOAL LIBURAN - 2 \n")
    counts = dict()
    line = input('Masukkan Kalimat : ')
    words = line.split()
    words.sort()
    print('Print Kata Sesuai Abjad\n', words)

    for word in words:
        counts[word] = counts.get(word,0) + 1
    print('\nCounts\n', counts)

    import operator
    sorted_d = sorted(counts.items(), key=operator.itemgetter(1))
    c = len(sorted_d)
    print ("\nTiga Kata Terbanyak :\n",sorted_d[c-1],sorted_d[c-2],sorted_d[c-3])

if __name__ == "__main__":
    soal1()
    soal2()
