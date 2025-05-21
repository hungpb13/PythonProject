# Dictionary = a collection of {key:value} pairs
# Ordered and changeable. NO duplicate keys

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

print(capitals.get("China"))
print(capitals.get("Japan"))

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "New York"})

print(capitals)

keys = capitals.keys()
print(keys)
for key in keys:
    print(f"{key}: {capitals.get(key)}")

values = capitals.values()
print(values)

items = capitals.items()
print(items)
for key, value in items:
    print(f"{key} - {value}")

capitals.pop("China")
capitals.popitem()

print(capitals)
