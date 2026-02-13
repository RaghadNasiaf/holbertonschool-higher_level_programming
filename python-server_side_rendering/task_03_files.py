#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Holberton School - Higher Level Programming
Python Server-Side Rendering

Task 3: Displaying Data from JSON or CSV Files in Flask

This module creates a Flask application route that reads product data from
either JSON or CSV files based on a query parameter (?source=json|csv).
It can optionally filter products by id (?id=<number>).
It handles invalid sources and missing products with clear messages.
"""

import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_json(filepath):
    """
    Read products from a JSON file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        list: List of product dictionaries (each has id, name, category, price).
              Returns an empty list if file can't be read or format is invalid.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
    except (OSError, json.JSONDecodeError):
        return []
    return []


def read_products_csv(filepath):
    """
    Read products from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        list: List of product dictionaries (id as int when possible, price as float when possible).
              Returns an empty list if file can't be read.
    """
    products = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Normalize fields
                product = {
                    "id": row.get("id"),
                    "name": row.get("name"),
                    "category": row.get("category"),
                    "price": row.get("price"),
                }

                # Convert id to int if possible
                try:
                    product["id"] = int(product["id"])
                except (TypeError, ValueError):
                    pass

                # Convert price to float if possible
                try:
                    product["price"] = float(product["price"])
                except (TypeError, ValueError):
                    pass

                products.append(product)
    except OSError:
        return []
    return products


@app.route('/products', strict_slashes=False)
def products():
    """
    Render products from JSON or CSV based on 'source' query parameter.

    Query params:
        source: required, either 'json' or 'csv'
        id: optional, filters products by id

    Behavior:
        - If source is invalid -> show "Wrong source"
        - If id is provided but not found -> show "Product not found"
        - If id not provided -> show all products
    """
    source = request.args.get('source', '')
    raw_id = request.args.get('id', None)

    error = None
    products_list = []

    if source == 'json':
        products_list = read_products_json('products.json')
    elif source == 'csv':
        products_list = read_products_csv('products.csv')
    else:
        error = "Wrong source"
        return render_template('product_display.html', products=[], error=error)

    # If id is provided, try filtering
    if raw_id is not None:
        try:
            wanted_id = int(raw_id)
        except (TypeError, ValueError):
            # If id is not a valid integer, treat as not found
            return render_template('product_display.html', products=[], error="Product not found")

        filtered = [p for p in products_list if isinstance(p.get("id"), int) and p.get("id") == wanted_id]

        if len(filtered) == 0:
            return render_template('product_display.html', products=[], error="Product not found")

        return render_template('product_display.html', products=filtered, error=None)

    return render_template('product_display.html', products=products_list, error=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
