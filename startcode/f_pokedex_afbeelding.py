import tkinter
import requests
from PIL import Image, ImageTk
import io


def haal_pokemon_informatie_op():
    # De rest van de code is hetzelfde gebleven

    image_url = data['sprites']['front_default']
    laad_afbeelding(image_url)

# else .....

def laad_afbeelding(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        afbeelding_data = response.content
        afbeelding = Image.open(io.BytesIO(afbeelding_data))
        photo = ImageTk.PhotoImage(afbeelding)
        image_label.config(image=photo)
        image_label.image = photo



image_label = tkinter.Label(window)
image_label.pack()