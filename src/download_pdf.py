import requests
import os


# TODO: Fix problem with SSLCert
url = 'https://bitcoin.org/bitcoin.pdf'
r = requests.get(url)

filepath = '../data/bitcoin.pdf'
os.makedirs(os.path.dirname(filepath),exist_ok=True)

with open (filepath, 'wb') as f:
    f.write(r.content)