import requests
import json
from core.localscommands import clear, pause, title
about = "https://discord.com/api/v9/users/@me"
billing = " https://discord.com/api/v9/users/@me/billing/subscriptions"
guilds = "https://discord.com/api/v9//users/@me/guilds"
connections = "https://discord.com/api/v9/users/@me/connections"

def main():
	token = input("Token \n> ")
	discordRequest = requests.get('https://discord.com/api/v9/users/@me', headers={"Authorization": token})
	if discordRequest.status_code == 401:
		clear()
		print("Token is invalid.")
		pause()
		exit()
	aboutUser = requests.get(about, headers={"Authorization": token})
	aboutBilling = requests.get(billing, headers={"Authorization": token})
	aboutGuilds = requests.get(guilds, headers={"Authorization": token})
	aboutConnections = requests.get(connections, headers={"Authorization": token})
	billingInfo = aboutBilling.text
	loads = json.loads(aboutUser.text)
	userDump = json.dumps(loads, indent = 2)
	loads2 = json.loads(billingInfo)
	billingDump = json.dumps(loads2, indent = 2)
	loads3 = json.loads(aboutGuilds.text)
	guildDump = json.dumps(loads3, indent = 2)
	loads4 = json.loads(aboutConnections.text)
	connectionsDump = json.dumps(loads4, indent = 2)
	print(f"---User Info---{userDump}\n---Billing Info---{billingDump}\n---Guild Info---{guildDump}\n---Connections Info---{connectionsDump}")
	response = input("\n\n\nSave to txt file? (y/n): ")
	if response == "y":
		with open(loads["username"] + loads["discriminator"] + ".txt", "w+") as f:
			f.write(f"---User Info---{userDump}\n---Billing Info---{billingDump}\n---Guild Info---{guildDump}\n---Connections Info---{connectionsDump}")
			f.close()
	elif response == "n":
		exit()
	else:
		print("please enter a valid value.")
try:
	main()
except Exception as e:
	print(e)
