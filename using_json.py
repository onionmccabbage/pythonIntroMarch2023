import json

# JSON is a very popular dat format - it is just plain text
j = '''[
     {"item":"Pots", "Price":3.99}, 
     {"item":"Dots", "Price":1.99},
     {"item":"Wots", "Price":9.99}
    ]'''

# convert plain-text JSON into a Python structure
s = json.loads(j)

# convert a Python structure back into JSON (plain text)
j2 = json.dumps(s)
print(j, type(j))
print(s, type(s))
print(j2, type(j2))