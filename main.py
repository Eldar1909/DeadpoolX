import discord
from discord.ext import commands

# Tokenul botului - nu uita să înlocuiești cu tokenul tău real
TOKEN = "TOKENUL_TAU_AICI"  # Îți recomand să pui tokenul într-un fișier de configurare sau să-l folosești ca variabilă de mediu

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
            if "tek sensor" in content:
                print("⚠️ Alertă: Mesaj cu 'Tek Sensor' detectat!")
                # Trimite mesaj în canalul respectiv
                await message.channel.send("Inamici la baza")  # Mesaj pentru 'Tek Sensor'
            
            elif "fob" in content:
                print("⚠️ Alertă: Mesaj cu 'Fob' detectat!")
                # Trimite mesaj în canalul respectiv
                await message.channel.send("Inamici la Fob")  # Mesaj pentru 'Fob'

    except Exception as e:
        print(f"❌ Eroare: {e}")

    # Permite botului să proceseze comenzi
    await bot.process_commands(message)

# Pornește botul
try:
    bot.run(TOKEN)
except Exception as e:
    print(f"❌ Botul nu s-a putut conecta: {e}")
