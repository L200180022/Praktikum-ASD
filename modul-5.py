class Mahasiswa(object):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us

class MhsTIF (Mahasiswa):  
    def katakanPy(self):
        print('Python is cool.')
        
listen = [MhsTIF ('dimas',68,'Sukoharjo', 130000),
MhsTIF('ahdi',87,'malang', 890000),
MhsTIF('Dano',90,'batu', 123000),
MhsTIF('suti',38,'surabaya', 230000),
MhsTIF('anggi',46,'bali', 22000),
MhsTIF('andi',57,'pontiank', 980000),
MhsTIF('odit',58,'lembang', 267000),
MhsTIF('Tito',50,'bandung', 212000),
MhsTIF('dodo',86,'gresik', 975000),
MhsTIF('dodi',71,'jakarta', 21000),
MhsTIF('adi',110,'Rembang', 125000)]

#1
def urutkannim(l):
    n = len(l)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if l[k].nim > l[k+1].nim :
                swap(l,k,k+1)

def ceknim (l):
    for i in l :
        print (i.nim)

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp
#2
def urutkan(A,B):
    C = A+B
    n = len(C)
    for i in range(1,n):
        nilai=C[i]
        pos=i
        while pos > 0 and nilai < C[pos-1]:
            C[pos]=c[pos-1]
            pos=pos-1
        C[pos] = nilai
    return C
A = [11,13,14,23,24]
B = [25,27,31,35]

#3
from time import time as detak
from random import shuffle as kocok
def swap(A,p,q):
    tmp = A[p]
    A[p]= A[q]
    A[q]= tmp

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos -1]
            pos = pos -1
        A[pos] = nilai
        
def cariPosisiYangTerkecil(A,darisini, sampaisini):
    posisiYangTerkecil = darisini
    for i in range (darisini+1, sampaisini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

k = []
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak(); bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw = detak(); selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw = detak(); insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw));
