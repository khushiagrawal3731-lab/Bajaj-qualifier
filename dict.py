marks = { "harry" : 78, "yu" : 79, 8:"khufd"}  # It is unordered mutable indexed and does not contain duplicate key
print(marks["yu"])
# marks["harry"]
print(marks, type(marks))

#Methods

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry":99, "renuka": 76})
print(marks)
print(marks.get("renuka"))