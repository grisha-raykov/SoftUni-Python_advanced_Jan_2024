import tkinter as tk
import json
import urllib.request
import requests
from io import BytesIO
from PIL import ImageTk, Image


def display_image(image_url: str) -> None:
    with urllib.request.urlopen(get_image_url()) as url:
        image_data = url.read()  # Donwload the image
    image_stream = BytesIO(image_data)
    image = ImageTk.PhotoImage(Image.open(image_stream))
    image_label.config(image=image)
    image_label.image = image  # Keeps reference to the image


def get_image_url() -> str:
    headers = {
        "Authorization": ""}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "256x256",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    return result['openai']['items'][0]['image_resource_url']


def render_image():
    print('Clicked')
    try:
        error_label.place_forget()
        image_url = get_image_url()
    except KeyError:
        error_label.place(x=20, y=50)
    else:
        display_image(image_url)


window = tk.Tk()

window.title("AI Image Generator")
window.geometry("500x350")

error_label = tk.Label(window, text='Prompt cannot be empty', fg='red')

input_field = tk.Entry(window, width=50)
input_field.place(x=165, y=20)
generate_button = tk.Button(window, text="Generate", width=14, height=1, command=render_image)
generate_button.place(x=165, y=50)

image_label = tk.Label(window, )
image_label.place(x=125, y=70)

window.mainloop()
