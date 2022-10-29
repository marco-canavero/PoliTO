# Lo scopo del codice Python è analizzare il file prodotti.txt per ricavarne alcune informazioni, ovvero (1) il podio delle nazioni
# con i punteggi più alti, (2) il miglior prodotto per ciascuna categoria (e.g. Piatto/ Coltello/ ...) e (3) il prodotto con il
# punteggio massimo.

# Ciascuna riga del file prodotti.txt è del tipo: Codice Categoria Prezzo Nazione Punteggio1 P2 P3 P4 P5

print(open('prodotti.txt', 'r').read())  # visualizza a schermo il file prodotti, per comodità
print()


def main():

    # apertura file prodotti.txt
    prodotti = ''
    try:
        prodotti = open("prodotti.txt", 'r', encoding='utf-8')
    except FileNotFoundError as error:  # se il file non viene trovato
        print(error)

    dizionario = dict()  # crea un dizionario che ha come chiave il nome della nazione
    lista_prodotti = list()
    for line in prodotti:  # itera sulle righe del file
        if line != '' or line != '\n':
            parole = line.rstrip().split(' ')  # separa le parole che compongono ogni riga
            nazione = parole[3]
            codice = parole[0]
            categoria = parole[1]
            punteggi = parole[4::]
            for i in punteggi:  # converti il punteggi da stringa a float
                i = float(i)
            minimo = min(punteggi)
            massimo = max(punteggi)
            punteggi.remove(minimo)  # rimuovi il punteggio minimo e massimo
            punteggi.remove(massimo)
            somma = 0  # è la somma dei tre punteggi intermedi
            for j in punteggi:
                somma += float(j)
            if nazione not in dizionario:  # verifica se il dizionario ha già la nazione come chiave (sono uniche)
                dizionario[nazione] = [[codice, categoria, punteggi, somma]]
            elif nazione in dizionario:
                dizionario[nazione].append([codice, categoria, punteggi, somma])

    prodotti.close()  # chiudi il file

    dizionario_categorie = dict()
    lista_nazioni = list()  # individua la nazione vincitrice
    for key, val in dizionario.items():
        punt_nazione = 0
        for num in val:
            punt_nazione += num[3]
            lista_prodotti.append(num)

            categoria = num[1]  # è il nome della categoria
            if categoria not in dizionario_categorie:  # riempi il dizionario con la categoria come chiave
                dizionario_categorie[categoria] = [[num[0], num[3]]]
            elif categoria in dizionario_categorie:
                dizionario_categorie[categoria].append([num[0], num[3]])

        lista_nazioni.append([key, round(punt_nazione, 2)])

    # questo sort ordina la lista 2D in base al secondo elemento di ciascuna sottolista usando la funzione lambda
    lista_nazioni.sort(key=lambda x: x[1], reverse=True)

    # cerco il prodotto con il punteggio massimo
    lista_prodotti.sort(key=lambda x: x[3], reverse=True)
    print(f'Il miglior prodotto è {lista_prodotti[0][0]}, categoria: {lista_prodotti[0][1]} con punteggio pari a: {lista_prodotti[0][3]}\n')

    i = 1
    k = 0
    # stampa a video il podio delle nazioni vincitrici
    while i < 4:
        naz = lista_nazioni[k][0]  # è la nazione
        pun = lista_nazioni[k][1]  # è il punteggio della nazione
        print(f'{i}° classificato: {naz} - punteggio: {pun} punti.')
        i += 1
        k += 1

    print('\nCLASSIFICA CATEGORIE: ')
    for key, val in dizionario_categorie.items():  # stampa il miglior prodotto per categoria
        val.sort(key=lambda x: x[1], reverse=True)
        print(f'Il miglior prodotto nella categoria {key.upper()} è {val[0][0]} con punteggio {val[0][1]}')


main()
