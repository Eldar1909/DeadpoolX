import discord
from discord.ext import commands
import os

# Tokenul botului - îl luăm din variabila de mediu
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    print("❌ Tokenul nu a fost găsit! Asigură-te că ai setat variabila de mediu 'DISCORD_TOKEN'.")
    exit(1)

# ID-urile canalelor
RAID_BASE_CHANNEL_ID = 1364002151474659492  # ID-ul canalului Raid-base
TRIBE_LOGS_CHANNEL_ID = 910278737331896340  # ID-ul canalului Tribe logs

# ID-ul rolului
ROLE_ID = 937964042247622657  # ID-ul rolului 'Tribe Member'

# Intenții pentru a permite botului să citească mesajele
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
        # Evităm ca botul să răspundă propriilor mesaje
        if message.author == bot.user:
            return

        # Verifică dacă mesajul este trimis de un webhook
        if message.webhook_id is not None:
            content = message.content.lower()

            # Căutăm anumite cuvinte cheie în mesaj
            if "tek sensor" in content:
                print("⚠️ Alertă: 'Tek Sensor' detectat!")
                # Trimite mesaj în canalul Raid-base (ID-ul canalului 1364002151474659492)
                raid_base_channel = bot.get_channel(RAID_BASE_CHANNEL_ID)
                if raid_base_channel:
                    # Trimite mesaj doar dacă nu s-a trimis deja unul similar
                    await raid_base_channel.send("Inamici la baza")  # Mesaj pentru 'Tek Sensor'
            
            elif "fob" in content:
                print("⚠️ Alertă: 'Fob' detectat!")
                # Trimite mesaj în canalul Raid-base (ID-ul canalului 1364002151474659492)
                raid_base_channel = bot.get_channel(RAID_BASE_CHANNEL_ID)
                if raid_base_channel:
                    # Trimite mesaj doar dacă nu s-a trimis deja unul similar
                    await raid_base_channel.send("Inamici la Fob")  # Mesaj pentru 'Fob'

            # Verifică dacă este un mesaj trimis într-un canal specific (Tribe logs)
            if message.channel.id == TRIBE_LOGS_CHANNEL_ID:
                # Trimite un ping la rolul 'Tribe Member' în canalul Raid-base
                raid_base_channel = bot.get_channel(RAID_BASE_CHANNEL_ID)
                if raid_base_channel:
                    await raid_base_channel.send(f"<@&{ROLE_ID}> Alertă: Mesaj detectat cu cuvintele cheie!")

    except Exception as e:
        print(f"❌ Eroare: {e}")

    # Permite botului să proceseze comenzi
    await bot.process_commands(message)

# Pornește botul
try:
    print("🚀 Pornind botul...")
    bot.run(TOKEN)
except Exception as e:
    print(f"❌ Botul nu s-a putut conecta: {e}")
