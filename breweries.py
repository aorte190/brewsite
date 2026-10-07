"""
 Brewery data for the /brewery page.

 Each brewery is a dictionary, and the dictionaries are stored in a list so
 the template can loop through them. Listings come from Open Brewery DB, a
 free public directory of breweries, filtered to Las Cruces, New Mexico.
 Only breweries with a street address are included.
"""

# Where the data came from, shown at the bottom of the /brewery page
DATA_SOURCE = {
    "name": "Open Brewery DB",
    "url": "https://www.openbrewerydb.org/",
    "retrieved": "October 2026",
}

BREWERIES = [
    {
        "name": "High Desert Brewing Co",
        "type": "Brewpub",
        "address": "1201 W Hadley Ave",
        "city": "Las Cruces",
        "state": "NM",
        "zip": "88005",
        "phone": "(575) 525-6752",
        "website": "http://www.highdesertbrewingco.com",
    },
    {
        "name": "Picacho Peak Brewing Company",
        "type": "Brewpub",
        "address": "3900 W Picacho Ave",
        "city": "Las Cruces",
        "state": "NM",
        "zip": "88007",
        "phone": "(575) 680-6394",
        "website": "http://www.picachopeakbrewery.com",
    },
    {
        "name": "Spotted Dog Brewery",
        "type": "Brewpub",
        "address": "2920 Avenida De Mesilla",
        "city": "Las Cruces",
        "state": "NM",
        "zip": "88005",
        "phone": "(575) 650-2729",
        "website": "http://www.spotteddogbrewery.com",
    },
    {
        "name": "De La Vega's Pecan Grill and Brewery",
        "type": "Contract",
        "address": "500 S Telshor Blvd",
        "city": "Las Cruces",
        "state": "NM",
        "zip": "88011",
        "phone": "(575) 521-1099",
        "website": "http://www.pecangrill.com",
    },
]
