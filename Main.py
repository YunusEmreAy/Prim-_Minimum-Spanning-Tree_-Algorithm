# Yunus Emre Ay / E-posta:TR.yunus.emre.ay@gmail.com

import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

with open("Main.txt", "r", encoding="utf-8") as file:

    matris = list()
    boyut = int(file.readline().replace("\n",""))

    for i in range(boyut):  # dosyadaki bilgiler adim adim matrise aliniyor
        liste = file.readline().replace("\n", "").split(",")
        matris.append(liste)

alfabe = "ABCDEFGHIJKLMNOPRSTUVYZ"


def gorsel_yazdir(son_liste): # Graphs yapisini gorsel olarak yazdirmaktadir.

    edges = list()
    for i in range(boyut):
        for j in range(boyut):
            if matris[i][j] != "0":
                edges.append((alfabe[i], alfabe[j]))

    G = nx.DiGraph()
    G.add_edges_from(edges)
    nx.draw_circular(G, with_labels=True)
    plt.savefig("Baslangic_Graphs_yapisi.png")    # python dosyasinin buludugu dizine graphs yapisini "Baslangic_Graphs_yapisi.png" ismiyle yazdirmaktadir.
    plt.show()


    edges = list()
    for i in son_liste:
        edges.append((i[0], i[1]))
    G = nx.DiGraph()
    G.add_edges_from(edges)
    nx.draw_circular(G, with_labels=True)
    plt.savefig("Prim_Graphs_yapisi.png")    # python dosyasinin buludugu dizine graphs yapisini "Prim_Graphs_yapisi.png" ismiyle yazdirmaktadir.
    plt.show()


def prim_algoritmasi():
    kenarlar = list()
    son_liste = list()
    girilenler = list()

    secim = alfabe[0:boyut]
    while(True):
        print("Lutfen Baslangic Node'unu seciniz.(Buyuk harf kullaniniz)\nNode'lar: ",end="")
        for i in range(boyut-1):
            print("{} / ".format(alfabe[i]),end="")
        print(alfabe[i+1])
        start = input("Baslangic Node --> ")
        girilenler.append(start)

        if start in secim:
            break


    for i in range(boyut):
        for j in range(boyut):
            if matris[i][j] != "0":
                liste = list()
                liste.append(alfabe[i])
                liste.append(alfabe[j])
                liste.append(int(matris[i][j]))
                kenarlar.append(liste)

    print("Tum Kenarlar: ", kenarlar)
    kenarlar_agirlik = 0
    for i in kenarlar:
        kenarlar_agirlik += i[2]

    kenarlar_copy = kenarlar.copy()
    for i in kenarlar_copy:
        if start == i[1]:
            kenarlar.remove(i)

    while(len(kenarlar) != 0):
        en_kucuk = sys.maxsize
        for i in range(len(kenarlar)):
            if (kenarlar[i][0] in girilenler) and (en_kucuk > kenarlar[i][2]):
                en_kucuk = kenarlar[i][2]
                indis = i
        girilenler.append(kenarlar[indis][1])
        son_liste.append(kenarlar[indis])

        kenarlar_copy = kenarlar.copy()
        for i in kenarlar_copy:
            if i[1] in girilenler:
                kenarlar.remove(i)


    print("Prim Kenarlar: ",son_liste)

    prim_agirlik = 0
    for i in son_liste:
        prim_agirlik += i[2]

    print("Tum Kenarlar Agirlik: ", kenarlar_agirlik)
    print("Prim Kenarlar Agirlik: ", prim_agirlik)

    gorsel_yazdir(son_liste)
    print("\n***Python Dosyasinin Buludugu Dizine Graphs Yapilari Gorsel olarak Yazdirilmstir.***\n")



print("--------------------------------------------------------------------------------------------------------------")
print("\n***Bilgilendirme: 'txt' Dosyasinda Bulunan '0' Simgesi 'Kenar Yok' Olarak Dergerlendirilecektir***\n")

prim_algoritmasi()
