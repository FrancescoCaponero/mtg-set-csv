import requests
import csv

set_code = "blb"
url = f"https://api.scryfall.com/cards/search?q=set:{set_code}"
all_cards = []
has_more = True

while has_more:
    response = requests.get(url)
    data = response.json()
    all_cards.extend(data['data'])
    has_more = data.get('has_more', False)
    url = data.get('next_page', None)

# Estrai i dati rilevanti, inclusi gli URL delle immagini
card_data = [
    (card['name'], card['type_line'], card['rarity'], card['image_uris']['normal'])
    for card in all_cards if 'image_uris' in card
]

# Salva i dati in un file CSV
with open(f'{set_code}_cards.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Type', 'Rarity', 'Image URL'])
    writer.writerows(card_data)

print(f"File CSV creato: {set_code}_cards.csv con {len(card_data)} carte.")
