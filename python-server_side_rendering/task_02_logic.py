#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Holberton School - Higher Level Programming
Python Server-Side Rendering

Task 2: Creating a Dynamic Template with Loops and Conditions in Flask

This module creates a Flask application that renders multiple pages using Jinja.
It includes a dynamic /items route that reads a list of items from a JSON file
(items.json) and displays them in an HTML template with loops and conditions.
"""

import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about', strict_slashes=False)
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact', strict_slashes=False)
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items', strict_slashes=False)
def items():
    """
    Render the items page.

    Reads items from items.json in the project directory and passes the list to
    the items.html template. If the file is missing or invalid, it falls back
    to an empty list so the template shows 'No items found'.
    """
    items_list = []

    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, dict):
            loaded = data.get('items', [])
            if isinstance(loaded, list):
                items_list = loaded

    except (OSError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
