Przepraszam za tak mocne opóźnienie w oddaniu projektu, niestety problemy zdrowotne i mój ostatni pobyt w szpitalu pokrzyżował mi plany,

# Habitflow

Prosta aplikacja do zarządzania nawykami, zbudowana w Django.

## Funkcjonalności

- Dodawanie, edycja i usuwanie nawyków
- Oznaczanie nawyków jako wykonane w danym dniu
- Podgląd historii wykonania nawyków
- Proste statystyki (liczba dni z rzędu, procent wykonania)

## Instalacja

```bash
git clone git@github.com:IzabelaWasilczuk/Habbit.git
cd Habitflow
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
