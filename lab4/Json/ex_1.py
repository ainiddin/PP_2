import json

with open(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab4\json\sample_data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("DN",50*" ", "Description",5*" ", "Speed",3*" ", "MTU",8*" ")
print("-" * 51," ","-" * 15," ","-" * 8," ","-" * 7)
three=0
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    DN = attributes["dn"]
    Description = attributes.get("descr", "")
    Speed = attributes.get("speed", "inherit")
    MTU = attributes["mtu"]

    print(DN.ljust(50), Description.ljust(20), Speed.ljust(8), MTU.ljust(8))
 
