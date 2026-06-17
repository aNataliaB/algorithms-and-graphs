def dijkstra(graf, start, koniec):
    INF = float('inf')
    odleglosci = {w: INF for w in graf}
    odleglosci[start] = 0
    odwiedzone = set()
    poprzedni = {}

    while len(odwiedzone) < len(graf):
        aktualny = None
        najmniejsza = INF

        for wierzcholek in odleglosci:
            if wierzcholek not in odwiedzone and odleglosci[wierzcholek] < najmniejsza:
                aktualny = wierzcholek
                najmniejsza = odleglosci[wierzcholek]

        if aktualny is None or najmniejsza == INF:
            break

        odwiedzone.add(aktualny)
        if aktualny == koniec:
            break

        for sasiad, koszt in graf[aktualny].items():
            if sasiad in graf:
                nowa_odleglosc = odleglosci[aktualny] + koszt
                if nowa_odleglosc < odleglosci[sasiad]:
                    odleglosci[sasiad] = nowa_odleglosc
                    poprzedni[sasiad] = aktualny

    return odleglosci, poprzedni

graf = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 5, 'B': 1, 'D': 1},
    'D': {'B': 4, 'C': 1},
    'E': {}
}
while True:
    print(f"Dostępne wierzchołki: {list(graf.keys())}")
    start = input("Podaj wierzchołek startowy: ").strip().upper()
    koniec = input("Podaj wierzchołek końcowy: ").strip().upper()

    if start not in graf and koniec not in graf:
        print("Podane wierzchołki są niepoprawne!")
    elif start not in graf :
        print("Podany wierzchołek początkowy jest niepoprawny!")
    elif koniec not in graf:
        print("Podany wierzchołek końcowy jest niepoprawny!")
    else:
        odleglosci, poprzedni = dijkstra(graf, start, koniec)
        if odleglosci[koniec] == float('inf'):
            print(f"Nie istnieje droga między wierzchołkiem {start}, a {koniec}.")
        else:
            sciezka = []
            aktualny = koniec

            while aktualny != start:
                sciezka.append(aktualny)
                if aktualny not in poprzedni:
                    break
                aktualny = poprzedni[aktualny]

            sciezka.append(start)
            sciezka.reverse()

            print("Najkrótsza droga:")
            print(" -> ".join(sciezka))
            print("Całkowity koszt:", odleglosci[koniec])

    decyzja = input("\nCzy chcesz sprawdzić inną drogę? (t/n): ").strip().lower()
    if decyzja != 't':
        print("Dziękuję za skorzystanie z programu. Do widzenia!")
        break