#1
class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

al = Mahasiswa("ana", 289, "surabaya", 270000)
a2 = Mahasiswa("danar", 109, "jambi", 260000)
a3 = Mahasiswa("muham", 124, "madura", 220000)
a4 = Mahasiswa("aji", 389, "malang", 287000)
a5 = Mahasiswa("nan", 645, "batu", 290000)
a6 = Mahasiswa("ahad", 143, "sragen", 290000)
a7 = Mahasiswa("alo", 139, "batang", 250000)
a8 = Mahasiswa("adit", 165, "demak", 276000)
a9 = Mahasiswa("kito", 200, "pati", 276000)
a10 = Mahasiswa("dana", 192, "purwodadi", 270000)
a11 = Mahasiswa("nanda", 187, "klaten", 245000)


Daftar = [al, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]

def cariKotaasal(list, target):
    a = []
    for i in list :
        if i.kotaTinggal == target:
            a.append(list.index(i))
    return a

a = cariKotaasal(Daftar, "klaten")
print(a)

#2
class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

al = Mahasiswa("ana", 289, "surabaya", 270000)
a2 = Mahasiswa("danar", 109, "jambi", 260000)
a3 = Mahasiswa("muham", 124, "madura", 220000)
a4 = Mahasiswa("aji", 389, "malang", 287000)
a5 = Mahasiswa("nan", 645, "batu", 290000)
a6 = Mahasiswa("ahad", 143, "sragen", 290000)
a7 = Mahasiswa("alo", 139, "batang", 250000)
a8 = Mahasiswa("adit", 165, "demak", 276000)
a9 = Mahasiswa("kito", 200, "pati", 276000)
a10 = Mahasiswa("dana", 192, "purwodadi", 270000)
a11 = Mahasiswa("nanda", 187, "klaten", 245000)

Daftar = [al, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]

def cariUangSakuTerkecil(list):
    temp = list[0].uangSaku
    for i in list[1:]:
        if i.uangSaku < temp:
            temp = i.uangSaku
    return temp

A = cariUangSakuTerkecil(Daftar)
print(A)

#3
class Mahasiswa(object):
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

al = Mahasiswa("ana", 289, "surabaya", 270000)
a2 = Mahasiswa("danar", 109, "jambi", 260000)
a3 = Mahasiswa("muham", 124, "madura", 220000)
a4 = Mahasiswa("aji", 389, "malang", 287000)
a5 = Mahasiswa("nan", 645, "batu", 290000)
a6 = Mahasiswa("ahad", 143, "sragen", 290000)
a7 = Mahasiswa("alo", 139, "batang", 250000)
a8 = Mahasiswa("adit", 165, "demak", 276000)
a9 = Mahasiswa("kito", 200, "pati", 276000)
a10 = Mahasiswa("dana", 192, "purwodadi", 270000)
a11 = Mahasiswa("nanda", 187, "klaten", 245000)

Daftar = [al, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]

def cariTerkecil (self):
    terkecil = self[0].uangSaku
    c = []
    for i in self:
        if i.uangSaku < terkecil :
            c.append ((i.nama, i.NIM, i.kotaTinggal, i.uangSaku))
    return c
print(cariTerkecil(Daftar))

#4
class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

al = Mahasiswa("ana", 289, "surabaya", 270000)
a2 = Mahasiswa("danar", 109, "jambi", 260000)
a3 = Mahasiswa("muham", 124, "madura", 220000)
a4 = Mahasiswa("aji", 389, "malang", 287000)
a5 = Mahasiswa("nan", 645, "batu", 290000)
a6 = Mahasiswa("ahad", 143, "sragen", 290000)
a7 = Mahasiswa("alo", 139, "batang", 250000)
a8 = Mahasiswa("adit", 165, "demak", 276000)
a9 = Mahasiswa("kito", 200, "pati", 276000)
a10 = Mahasiswa("dana", 192, "purwodadi", 270000)
a11 = Mahasiswa("nanda", 187, "klaten", 245000)

Daftar = [al, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]

def cariUangSakuKurangdari250rb(list):
    temp = []
    for i in list:
        if i.uangSaku < 250000:
            temp.append(i)
    return temp

f = cariUangSakuKurangdari250rb(Daftar)
for i in f:
    print(i.nama)

#5
class node (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
    def cari (self, cari):
        curNode = self
        while curNode is not None :
            if curNode.next != None :
                if curNode.data != cari :
                    curNode = curNode.next
                else :
                    print ("Data", cari, "ada dalam Linked List")
                    break
            elif curNode.next == None :
                print ("Data", cari, "tidak ada dalam linked list")
                break
a = node (80)
menu = a
a.next = node (22)
a = a.next
a.next = node (10)
a = a.next
a.next = node (19)

menu.cari(10)
menu.cari(22)

#6
def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    data = []
    while low <= high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            data.append(kumpulan.index(target))
            return True
        elif target < kumpulan[mid]:
            high = mid -1
        else :
            low = mid +1
    return False

list = [38, 12, 56, 137, 299]
target1 = 56
target2 = 120

print ("nilai target :", target1)
print (binSe(list, target1))

print ("\nnilai target :", target2)
print (binSe(list, target2))

#7
def binSeMass(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

list = [2, 4, 5, 6, 7, 5, 6, 6, 6, 10, 11, 12, 13, 13, 14]
print(binSeMass(list, 6))

#8
"""
untuk mencari berapa jumlah tebakan yang digunakan oleh Binary Search
yaitu dengan menggunakan Logaritma basis 2 (log2(n))
misalkan :
        // apabila terdapat elemen array berjumlah 100 maka memiliki maksimal 7 kali tebakan
           itu dikarenakan log2(100) = 6.643856189774725 sehingga diperoleh angka 7
           dapat juga diperoleh dari log2(128) = 7 karena yang mendekati dari 100 adalah 128
       //  apabila terdapat elemen array berjumlah 1000 maka memiliki maksimal 10 kali tebakan
           itu dikarenakan log2(1000) = 9.965784284662087 sehingga diperoleh angka 10
           dapat juga diperoleh dari log2(1024) = 10 karena yang mendekati dari 1000 adalah 128
""" 
