#!/usr/bin/python3
"""
Simple templating program for generating invitation files.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates invitation text files from a template and list of attendees.
    """

    # Validate template type
    if not isinstance(template, str):
        print("Invalid input type: template must be a string.")
        return

    # Validate attendees type
    if not isinstance(attendees, list):
        print("Invalid input type: attendees must be a list of dictionaries.")
        return

    # Ensure each attendee is a dictionary
    for item in attendees:
        if not isinstance(item, dict):
            print("Invalid input type: attendees must be a list of dictionaries.")
            return

    # Handle empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output = template

        for key in placeholders:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(output)
        except OSError:
            print(f"Error writing file {filename}")
