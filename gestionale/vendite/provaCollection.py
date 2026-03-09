from gestionale.core.prodotti import ProdottoRecord

p1=ProdottoRecord("laptop",1200.0)
p2=ProdottoRecord("mouse",20.0)
p3=ProdottoRecord("Auricolari",250.0)


carrello=[p1,p2,p3,ProdottoRecord("Tablet",700)]
carrello.sort(Key=lamdax :x.prezzo_unitario  reverse=True)
print("Prodotti nel carrello")
for i, p in enumerate(carrello):
    print(f"{i}){p.name}-{p.prezzo_unitario}")

    tot = sum(p.prezzo_unitario for p in carrello)
    print (f"totale del carrello:{tot}")


#aggiungere
carrello.append(ProdottoRecord("Prodp",100.0))
carrello.extend([ProdottoRecord("aaa",100.00),ProdottoRecord("bbb"100.0)])

#rimuovere
carrello.pop()
carrello.pop(2)
#Sorting
carrello.sort()#non funziona se non defnisco un metodo lt
carrello.sort(reverse=True)
carrello_ordinato=sorted(carrello)

#copia
carrello.reverse()
carrello_copia=carrello.copy()
carrello_copia2=copy.deepcopy(carrello)#mi crea una copia non solo nella lista ma anche di tutti gli oggetti all'interno
#perll'appunto copia profonda


#TUPLE
sede_principale=(45,8)#sede di torino
sede_milano=(45,9)#sede di milano
#le faccio con una tupla e non con una lista perchè non le cambierò mai


print(f"sede principale lat: {sede_principale[0]}, long :{sede_principale[1]}")



AliquotaIVA=(#tupla che contiene altre tuple
    ("Strandard", 0.22),
    ("Ridotta",0.10),
    ("Alimentari",0.04)
    ("Esente",0.0)

)

for descr , valore in AliquotaIVA:
    print(f"{descr}:{valore*100}%")


def calcola_statistiche_carrello(carrello):
    prezzi=[p.prezzo_unitario for p in carrello]
    return (sum(prezzi)),sum(prezzi)/len(prezzi),max(prezzi),min(prezzi)



tot,media,max,min= calcola_statistiche_carrello(carrello)
tot, *altri_campi=calcola_statistiche_carrello(carrello)#non
print (tot)


s=set()
s1=set()
    #set
categorie={"gold","silver","bronze","gold"}
print (categorie)
print(len(categorie))
categorie2={"Platinum, Elite"}
categorie_all=categorie|categorie2#unione
print (categorie_all)




#togliere
s.remove(elem)#rimuovere elemento e si arrabbia se non c'è
s.discard(elem)#rimuove senza arrabbiarsi
s.pop()#rimuove e restituisce un elemento
s.clear()


#operazioni insiemistiche
s.union(s1)#unione di due set
s.intersection(s1)#intersezione
s.difference(s1)#elemnti di s che non sono contenuti in s1
s.symmetric_deifference(s1)#elementi di s1 non contenuti in s e il viceversa

s1.issubset(s)
s1.issuperset(s)
s1.isdisjont(s)






