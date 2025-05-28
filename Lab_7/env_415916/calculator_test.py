ffrom calculator import dodawanie,dzielenie,mnozenie,odejmowanie,suma_kolumn, srednia_kolumn
def test_dodawanie():
    assert dodawanie(2, 3) == 5
    assert dodawanie(-1, 1) == 0

def test_odejmowanie():
    assert odejmowanie(5, 3) == 2
    assert odejmowanie(1, -1) == 2

def test_mnozenie():
    assert mnozenie(2, 3) == 6
    assert mnozenie(-1, 1) == -1

def test_dzielenie():
    assert dzielenie(6, 3) == 2
    assert dzielenie(1, -1) == -1
    assert dzielenie(1, 0) == "Błąd: dzielenie przez zero!"

def test_suma_kolumn():
    df = pd.DataFrame({'wartosci': [1, 2, 3]})
    assert suma_kolumn(df, 'wartosci') == 6

def test_srednia_kolumn():
    df = pd.DataFrame({'wartosci': [2, 4, 6]})
    assert srednia_kolumn(df, 'wartosci') == 4.0
