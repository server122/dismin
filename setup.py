import json

try:
    with open('config.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {
        "servip": "127.0.0.1",
        "rconport": "25575",
        "rconpass": "123",
        "roleid": "*",
        "bottok": "*"
    }

print("DON'T SHARE CONFIG.JSON FILE!")
print()
ip = input("Enter server IP *Leave blank to set as default* (Default: 127.0.0.1): ")
data["servip"] = ip if ip else data["servip"]

port = input("Enter RCON port *Leave blank to set as default* (Default: 25575): ")
data["rconport"] = port if port else data["rconport"]

passw = input("Enter RCON password *Leave blank to set as default* (Default: 123): ")
data["rconpass"] = passw if passw else data["rconpass"]

while True:
    idr = input("Enter the ID of the role for which the bot will be available: ")
    if idr:
        data["roleid"] = idr
        break
    else:
        print("Please enter id")

while True:
    tok = input("Enter Discord bot token: ")
    if tok:
        data["bottok"] = tok
        break
    else:
        print("Please enter token")

with open('config.json', 'w') as f:
    json.dump(data, f)
