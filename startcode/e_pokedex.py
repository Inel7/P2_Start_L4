import tkinter
import requests

def haal_pokemon_informatie_op():
    pokemon_naam = entry.get().lower()

    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_naam}"
    response = requests.get(api_url)

    if response.status_code == 200 :
        data = response.json()

        # Extract de benodigde informatie
        naam = data['name']
        hoogte = data['height'] * 10  # Hoogte is in decimetres, omzetten naar centimeters
        gewicht = data['weight'] / 10  # Gewicht is in hectograms, omzetten naar kilograms
        base_experience = data['base_experience']
        # Maak een lege lijst waar we abilities aan gaan toevoegen.
        abilities = []
        for ability in data['abilities']:
            ability_naam = ability['ability']['name']
            abilities.append(ability_naam)

        # Genereer de tekst voor weergave
        info_tekst = f"Naam: {naam}\nHoogte: {hoogte} cm\nGewicht: {gewicht} kg\n" + f"Basiservaring: {base_experience}\nMogelijkheden: {abilities}"
        info.config(text=info_tekst)
    else:
        info.config(text="pokemon niet gevonden")

window = tkinter.Tk()
window.title("pokedex")
window.geometry("600x400")

label = tkinter.Label(window,text="voer een pokemon in")
label.pack()
entry = tkinter.Entry(window)
entry.pack()
info = tkinter.Label(window, text="")
info.pack()
button = tkinter.Button(window, text="haal info op")
button.pack()

window.mainloop()
import tkinter
import requests

def haal_pokemon_informatie_op():
    pokemon_naam = pokemon_naam_entry.get().lower() # Haal pokémonnaam op in kleine letters

    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_naam}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        # Extract de benodigde informatie
        naam = data['name']
        hoogte = data['height'] * 10  # Hoogte is in decimetres, omzetten naar centimeters
        gewicht = data['weight'] / 10  # Gewicht is in hectograms, omzetten naar kilograms
        base_experience = data['base_experience']
        # Maak een lege lijst waar we abilities aan gaan toevoegen.
        abilities = []
        for ability in data['abilities']:
            ability_naam = ability['ability']['name']
            abilities.append(ability_naam)

        # Genereer de tekst voor weergave
        info_tekst = f"Naam: {naam}\nHoogte: {hoogte} cm\nGewicht: {gewicht} kg\n" + f"Basiservaring: {base_experience}\nMogelijkheden: {abilities}"

        pokemon_info_label.config(text=info_tekst) # Plaats de infotekst
    else:
        # Als de Pokémon niet gevonden is, geef een melding weer
        pokemon_info_label.config(text="Pokémon niet gevonden")

# Creëer het hoofdvenster
window = tkinter.Tk()
window.title("Pokémon Informatie Applicatie")


pokemon_naam_label = tkinter.Label(window, text="Voer een Pokémon-naam in:")
pokemon_naam_label.pack()

pokemon_naam_entry = tkinter.Entry(window)
pokemon_naam_entry.pack()

pokemon_info_label = tkinter.Label(window, text="")
pokemon_info_label.pack()

haal_info_op_knop = tkinter.Button(window, text="Haal Pokémon Informatie op", command=haal_pokemon_informatie_op)
haal_info_op_knop.pack()


window.mainloop()  # Start de GUI-loop


