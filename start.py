import hashlib
import os
import time
import webbrowser

import requests


url = 'https://northstar.dog/puppies'

def annoy(cycles):
    webbrowser.open(url)

    for _ in range(cycles):
        os.system('play -nq -t alsa synth {} sine {}'.format(1, 5000))
        os.system('play -nq -t alsa synth {} sine {}'.format(1, 50))


print("alerting test:")
annoy(2)

last_hash = None

while True:
    result = requests.get(url)
    raw_html = result.text

    new_hash = hashlib.sha256(raw_html.encode()).hexdigest()

    if last_hash is None:
        last_hash = new_hash

    if new_hash != last_hash:
        print("SITE CHANGE!!!!!")
        annoy(1000)
        last_hash = new_hash

        print(fmt_txt_only(raw_html))
    else:
        print("No change at {}. Curent hash is {}".format(time.ctime(), new_hash))

    time.sleep(5)
