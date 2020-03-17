#nomor 1
class matriks():
    def __init__(self, baris, kolom):
        self.baris = baris
        self.kolom = kolom

    #nomor 1a
    def memastikan(self):
        a = [[self.baris for j in range (self.baris)]for i in range (self.kolom)]
        for i in a:
            print (i)
        if self.baris == self.kolom:
            print ("Konsisten")
        else:
            print ("Tidak konsisten")
            
    #nomor 1b
    def mengambilukuran(self):
        a = [[self.baris for j in range (self.baris)]for i in range (self.kolom)]
        for i in a:
            print (i)
        b = 0
        for x in i:
            b+=1
        print ("Ukurannya adalah",[b, len(a)])

    #nomor 1c
    def menjumlahkanmatriks(self):
        a = [[self.baris for j in range (self.baris)]for i in range (self.kolom)]
        for i in a:
            print (i)
        print ("\n", "+\n")

        b = [[self.baris for j in range (self.baris)]for i in range (self.kolom)]
        for i in b:
            print(i)
        print ("\n","Hasil penjumlahan")

        c = self.baris+self.kolom
        d = [[c for i in range(self.baris)]for j in range(self.kolom)]
        for i in d:
            print (i)
            
    #nomor 1d
    def mengalikanmatriks(self):
        a = [[self.baris for j in range (self.baris)]for i in range (self.kolom)]
        for i in a:
            print (i)
        print ("\n", "*\n")

        b = [[self.baris for j in range (self.baris)]for i in range (self.kolom)]
        for i in b:
            print(i)
        print ("\n","Hasil penjumlahan")

        c = self.baris**self.kolom
        d = [[c for i in range(self.baris)]for j in range(self.kolom)]
        for i in d:
            print (i)

    #nomor 1e
    def determinan(self):
        #hanya untuk matriks 2x2
        a = [[self.baris for j in range (self.baris)]for i in range (self.kolom)]
        ad = 0
        bc = 0
        for i in a:
            if i == 0:
                ad = self.baris[i][i]*self.baris[i+1][i+1]
            elif i == 1:
                bc = self.baris[i-1][i]*self.baris[i][i-1]
        return ad-bc
