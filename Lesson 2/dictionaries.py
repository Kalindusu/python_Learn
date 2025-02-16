#dictionary

band={
    "vocal": "vocalist",
    "guitar": "guitarist",
    "drums": "drummer"
}

band2=dict(vocal="vocalist", guitar="guitarist", drums="drummer")

print(band)
print(band2)

print(type(band))
print(len(band))
print(type(band2))

#Access items
print(band["vocal"])
print(band.get("name"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#List of key-value pairs
print(band.items())
