# Sends inspirational quotes to the user using Zen Quotes API

# Format
"""
example quote -Quote Author Name
"""

import requests
from json import loads
from schema import Quote

def generate_quote(url="https://zenquotes.io/api/random") -> Quote:
    response = requests.get(url)
    json_data = loads(response.text)
    # quote = (
    #     json_data[0]["q"] + " -" + json_data[0]["a"]
    # )  # aligning the quote and it's author name in one string

    quote = Quote(quote=json_data[0]["q"], 
                  author=json_data[0]["a"]
                  )
    return quote
