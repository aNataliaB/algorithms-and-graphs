class Moneta:
    def __init__(self, nominal, koszt):
        self.nominal = nominal
        self.koszt = koszt

    def __repr__(self):
        return f"{self.nominal}gr"

def wydaj_zachlannie(dostepne_monety, kwota):
    posortowane = sorted(dostepne_monety, key=lambda x: x.nominal, reverse=True)
    
    wybrane = []
    pozostala_kwota = kwota
    
    for m in posortowane:
        if m.nominal <= pozostala_kwota:
            wybrane.append(m)
            pozostala_kwota -= m.nominal
            
    if pozostala_kwota == 0:
        return wybrane, sum(m.koszt for m in wybrane)
    return None, 0

def wydaj_dynamicznie(dostepne_monety, kwota_cel):
    n = len(dostepne_monety)
    dp = [[float('inf')] * (kwota_cel + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        m = dostepne_monety[i-1]
        for j in range(kwota_cel + 1):
            dp[i][j] = dp[i-1][j]
            if j >= m.nominal:
                nowy_koszt = dp[i-1][j - m.nominal] + m.koszt
                if nowy_koszt < dp[i][j]:
                    dp[i][j] = nowy_koszt

    if dp[n][kwota_cel] == float('inf'):
        return None, 0

    wynik = []
    j = kwota_cel
    for i in range(n, 0, -1):
        m = dostepne_monety[i-1]
        if j >= m.nominal and dp[i][j] == dp[i-1][j - m.nominal] + m.koszt:
            wynik.append(m)
            j -= m.nominal
            
    return wynik, sum(m.koszt for m in wynik)