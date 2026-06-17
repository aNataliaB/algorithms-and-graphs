import tkinter as tk
from tkinter import messagebox
from core import Moneta, wydaj_zachlannie, wydaj_dynamicznie

def uruchom_obliczenia():
    try:
        if not all([entry_monety.get().strip(), entry_koszty.get().strip(), entry_kwota.get().strip()]):
            raise ValueError("Wszystkie pola muszą być wypełnione!")

        nomy_raw = [n.strip() for n in entry_monety.get().split(',') if n.strip()]
        kosz_raw = [k.strip() for k in entry_koszty.get().split(',') if k.strip()]
        kwota_raw = entry_kwota.get().strip()

        if not kwota_raw.isdigit():
             raise ValueError("Kwota do wydania musi być liczbą całkowitą!")
        
        cel = int(kwota_raw)
        
        if cel == 0:
            raise ValueError("Kwota do wydania nie może wynosić 0!")

        if cel > 10000:
            raise ValueError("Kwota jest zbyt duża (limit: 10000).")

        if len(nomy_raw) != len(kosz_raw):
            raise ValueError(f"Niezgodność: wpisano {len(nomy_raw)} nominałów, ale {len(kosz_raw)} kosztów!")

        portfel = []
        suma_portfela = 0
        
        for n, k in zip(nomy_raw, kosz_raw):
            if not n.isdigit() or not k.isdigit():
                raise ValueError(f"Wartości nie są poprawnymi liczbami dodatnimi!")
            
            nv = int(n)
            kv = int(k)

            if nv == 0:
                raise ValueError("Nominał monety nie może wynosić 0!")
            if kv == 0:
                raise ValueError("Koszt monety nie może wynosić 0! (Ustal min. 1)")

            portfel.append(Moneta(nv, kv))
            suma_portfela += nv

        if suma_portfela < cel:
            messagebox.showinfo("Informacja", f"Masz w portfelu łącznie {suma_portfela}gr, a chcesz wydać {cel}gr.\nTo niemożliwe - brakuje monet.")

        reszta_z, koszt_z = wydaj_zachlannie(portfel, cel)
        reszta_d, koszt_d = wydaj_dynamicznie(portfel, cel)

        def fmt(lista):
            if lista is None:
                return " \n Nie można wydać tej kwoty\ndostępnymi monetami."
            return ", ".join(map(str, lista))

        txt = (
            f"WYNIK ZACHŁANNY:\nMonety: {fmt(reszta_z)}\nKoszt: {koszt_z}\n\n"
            f"--------------------------------------------------\n\n"
            f"WYNIK DYNAMICZNY (Optymalny):\nMonety: {fmt(reszta_d)}\nKoszt: {koszt_d}"
        )
        label_wyniki.config(text=txt)

    except ValueError as e:
        messagebox.showwarning("Błąd danych", str(e))
    except Exception as e:
        messagebox.showerror("Błąd krytyczny", f"Wystąpił nieoczekiwany błąd: {e}")

root = tk.Tk()
root.title("System Wydawania Reszty - Minimalizacja Kosztu")
root.geometry("500x700")

tk.Label(root, text="Dostępne nominały (po przecinku):", font=("Arial", 10, "bold")).pack(pady=(15, 5))
entry_monety = tk.Entry(root, width=50)
entry_monety.pack()
entry_monety.insert(0, "11, 11, 10, 5, 2, 1, 1")

tk.Label(root, text="Koszty monet (po przecinku):", font=("Arial", 10, "bold")).pack(pady=5)
entry_koszty = tk.Entry(root, width=50)
entry_koszty.pack()
entry_koszty.insert(0, "1, 1, 1, 1, 1, 1, 1")

tk.Label(root, text="Kwota do wydania:", font=("Arial", 10, "bold")).pack(pady=5)
entry_kwota = tk.Entry(root, width=20)
entry_kwota.pack()
entry_kwota.insert(0, "26")

tk.Button(root, text="OBLICZ", command=uruchom_obliczenia, 
          bg="#2196F3", fg="white", font=("Arial", 11, "bold"), 
          height=2, width=20).pack(pady=20)

label_wyniki = tk.Label(root, text="Tutaj pojawi się wynik...", 
                        font=("Courier New", 10), justify="left", 
                        bg="#f0f0f0", relief="sunken", width=52, height=14)
label_wyniki.pack(pady=10)

root.mainloop()