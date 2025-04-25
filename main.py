import discord
from discord.ext import commands
import os  # Vom folosi acest modul pentru a prelua variabilele de mediu

# Tokenul botului - preluat din variabila de mediu
TOKEN = os.getenv("DISCORD_TOKEN")  # Asigură-te că ai setat variabila de mediu DISCORD_TOKEN pe platforma ta de deployment

# Intenții - pentru a permite botului să citească mesajele
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Inițializare bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Eveniment care este apelat când botul este gata
@bot.event
async def on_ready():
    print(f"✅ Botul este online ca {bot.user}")

# Eveniment pentru procesarea mesajelor
@bot.event
async def on_message(message):
    try:
        if message.author == bot.user:
            return  # Evită să răspundă propriilor mesaje

        # Verifică dacă mesajul este trimis de un webhook
        if message.webhook_id is not None:
            content = message.content.lower()

            # Căutăm anumite cuvinte cheie în mesaj
            if "tek sensor" in content or "fob" in content:
                print("⚠️ Alertă: Mesaj cu 'Tek Sensor' sau 'Fob' detectat!")

                # Trimite un mesaj în canalul de alertă
                await message.channel.send("<@&937964042247622657> Alertă: Enemy detectat!")  # Ping la rolul 'Enemy'

    except Exception as e:
        print(f"❌ Eroare: {e}")

    # Permite botului să proceseze comenzi
    await bot.process_commands(message)

# Pornește botul
try:
    bot.run(TOKEN)
except Exception as e:
    print(f"❌ Botul nu s-a putut conecta: {e}")
