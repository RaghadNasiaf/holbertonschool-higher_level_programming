#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Holberton School - Higher Level Programming
Python Server-Side Rendering

Task 1: Creating a Basic HTML Template in Flask

This module defines a basic Flask application that renders HTML pages
using Jinja templates and reusable header and footer components.
"""

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
