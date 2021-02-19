import json

json_string = "{\"Hallo\": \"Welt\"}" # Da Strings bei JSON nur in "" stehen dürfen verwenden wir hier Backslashes
parsed_json = json.loads(json_string) # JSON parsen (ist nun ein Dictionary)
print(parsed_json["Hallo"]) # Ausgabe: Welt

# Backslashes vermeiden
json_string = '{"Hallo": "Welt"}' # Anders als Beispielsweise in Java können in Python Strings auch in '' stehen, dann benötigen wir die \ vor dem " nicht mehr.

# JSON-Array
json_string = '[1, 2, 3, "vier"]'
parsed_json = json.loads(json_string) # JSON-Arrays werden in Python als Liste gespeichert
print(parsed_json[1]) # Ausgabe: 2 (Typ: Integer)


# Sortieren
python_obj = {"wort_2": "Hallo", "wort_1": "Welt", "zeichen": "!"} # Sieht syntaktisch zwar aus wie JSON, ist aber noch ein Dictionary
json_string = json.dumps(python_obj, sort_keys=True)  # Dictionary wird in JSON konvertiert. Das optionale Parameter sort_keys bewirkt,
                                                    # dass die einzelnen Paare nach Schlüsseln sortiert werden.
print(json_string) # Ausgabe: {"wort_1": "Welt", "wort_2": "Hallo", "zeichen": "!"}

# Leerzeichen entfernen
json_string = json.dumps(python_obj, separators=(",",":")) # Trennzeichen werden als tuple mit dem Parameter separators übergeben. So können beispielsweise Leerzeichen entfernt werden.
print(json_string) # Ausgabe: {"wort_2":"Hallo","wort_1":"Welt","zeichen":"!"}

# Pretty-printing zur besseren Lesbarkeit
python_obj = {"name": "Jannik", "vermoegen": 100000000000000000000000000000, "programmiersprachen": ["Python", "Java", "PHP", "JavaScript/JSX", "HTML", "CSS/SCSS"]}
print(json.dumps(python_obj, indent=2)) # Einzug auf 2 (Default: None)
'''Ausgabe:
{
  "name": "Jannik",
  "vermoegen": 100000000000000000000000000000,
  "programmiersprachen": [
    "Python",
    "Java",
    "PHP",
    "JavaScript/JSX",
    "HTML",
    "CSS/SCSS"
  ]
}
'''

# Aus Datei lesen
with open("./beispiel.json", "r") as datei:
    python_obj = json.load(datei)
    print(python_obj['eine_nummer']) # Ausgabe: 123



