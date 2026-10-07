"""
 Software Req Doc: BrewSite Project
 Release Date: October 2026
 Code Author: Abraham Ortega
 Description: A small Flask web application for the ICT 362 BrewSite
              project. Flask handles the routes (the URLs) and Jinja
              templates build the HTML pages. The site has two pages:
                  /home     - welcome page with three embedded pictures
                  /brewery  - a listing of Las Cruces breweries
                              (also reachable at /breweries)
"""

from flask import Flask, render_template, redirect, url_for

from breweries import BREWERIES, DATA_SOURCE

# Create the Flask application. __name__ tells Flask where to look for the
# templates/ and static/ folders, which sit next to this file.
app = Flask(__name__)


@app.route("/")
def index():
    """Send anyone who visits the bare site address over to /home.

    Returns:
        Response: A redirect to the home page.
    """
    return redirect(url_for("home"))


@app.route("/home")
def home():
    """Render the home page.

    Returns:
        str: The HTML for home.html, built on top of base.html.
    """
    return render_template("home.html", title="Home")


@app.route("/brewery")
@app.route("/breweries")   # same page at both addresses
def brewery():
    """Render the brewery listing page.

    The list of brewery dictionaries is passed into the template, where a
    Jinja for loop builds one card per brewery.

    Returns:
        str: The HTML for brewery.html with the brewery data filled in.
    """
    return render_template(
        "brewery.html",
        title="Breweries",
        breweries=BREWERIES,
        source=DATA_SOURCE,
    )


# Only start the development server when this file is run directly,
# the same __name__ guard used in IronVaultArchive.py for SkillBuilder 5.
if __name__ == "__main__":
    app.run(debug=True)
