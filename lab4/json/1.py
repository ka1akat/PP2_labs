import json

with open("sample-data.json") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 75)
print("DN", " "*48,"Description"," "*5,"Speed"," "*2,"MTU" )
print("-" * 75)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "N/A")  
    speed = attributes.get("speed")
    mtu = attributes.get("mtu")

    print("{:<50} {:<20} {:<6} {:<6}".format(dn, description, speed, mtu))
