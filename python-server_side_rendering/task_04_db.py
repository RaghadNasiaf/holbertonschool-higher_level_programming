#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Holberton School - Higher Level Programming
Python Server-Side Rendering

Task 4: Extending Dynamic Data Display to Include SQLite in Flask

This module extends the products display feature to support multiple data sources:
- JSON (products.json)
- CSV  (products.csv)
- SQL  (SQLite database: products.db)

Route:
- /products?source=json|csv|sql[&id=<int>]

Behavior:
- If source is invalid -> show "Wrong source"
- If id is provided but not found -> show "Product not found"
- If database errors occur -> show a clear error message in the template
"""

import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_json(filepath):
    """Read products from a JSON file and return a list of dictionaries."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
    except (OSError, json.JSONDecodeError):
        return []
    return []


def read_products_csv(filepath):
    """Read products from a CSV file and return a list of dictionaries."""
    products = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                product = {
                    "id": row.get("id"),
                    "name": row.get("name"),
                    "category": row.get("category"),
                    "price": row.get("price"),
                }

                # Normalize types when possible
                try:
                    product["id"] = int(product["id"])
                except (TypeError, ValueError):
                    pass

                try:
                    product["price"] = float(product["price"])
                except (TypeError, ValueError):
                    pass

                products.append(product)
    except OSError:
        return []
    return products


def read_products_sql(db_path):
    """
    Read products from SQLite database (products.db) and return list of dicts.
    """
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        for r in rows:
            products.append({
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3]
            })
    except sqlite3.Error:
        # Caller will handle error message
        raise
    return products


@app.route('/products', strict_slashes=False)
def products():
    """
    Render products from JSON/CSV/SQL based on 'source' query parameter.
    Optional: filter by id using 'id' query parameter.
    """
    source = request.args.get('source', '')
    raw_id = request.args.get('id', None)

    error = None
    products_list = []

    # Choose source
    if source == 'json':
        products_list = read_products_json('products.json')
    elif source == 'csv':
        products_list = read_products_csv('products.csv')
    elif source == 'sql':
        try:
            products_list = read_products_sql('products.db')
        except sqlite3.Error:
            return render_template(
                'product_display.html',
                products=[],
                error="Database error"
            )
    else:
        return render_template('product_display.html', products=[], error="Wrong source")

    # Filter by id if provided
    if raw_id is not None:
        try:
            wanted_id = int(raw_id)
        except (TypeError, ValueError):
            return render_template('product_display.html', products=[], error="Product not found")

        filtered = [
            p for p in products_list
            if isinstance(p.get("id"), int) and p.get("id") == wanted_id
        ]

        if len(filtered) == 0:
            return render_template('product_display.html', products=[], error="Product not found")

        return render_template('product_display.html', products=filtered, error=None)

    return render_template('product_display.html', products=products_list, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
