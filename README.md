# BrewSite

A Flask and Jinja web application for ICT 362 Software Technology II.
It lists craft breweries in Las Cruces, New Mexico.

## Pages

| Route      | What it shows                                      |
|------------|----------------------------------------------------|
| `/home`    | Welcome page with project info and three embedded pictures |
| `/brewery` or `/breweries` | Brewery listings with address, phone, and website |

## Running it locally

```
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000/home

## Branches

| Branch        | Purpose                                  |
|---------------|------------------------------------------|
| `development` | Where new work is written and committed  |
| `staging`     | Code that is being tested before release |
| `production`  | Finished code that is ready to go live   |

Brewery data from [Open Brewery DB](https://www.openbrewerydb.org/).
