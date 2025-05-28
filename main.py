
# BOT TEMPLATE MADE BY CRISOPEO, PLEASE PUT CREDITS IF YOU ARE CREATING A BOT WITH THIS TEMPLATE.
# SUBSCRIBE TO CRISOPEO ON YOUTUBE: @Crisopeo
# JOIN HIS DISCORD SERVER



import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import json
import os

# ---------------------------
# CONFIGURAZIONE E INTERNACIONALIZZAZIONE
# ---------------------------
LANG_FILE = 'lang_prefs.json'
if os.path.exists(LANG_FILE):
    with open(LANG_FILE, 'r') as f:
        LANG_PREFS = json.load(f)
else:
    LANG_PREFS = {}

# Dizionario traduzioni
TRANSLATIONS = {
    'en': {
        'ping': '🏓 Pong! {latency}ms',
        'language_info': '🌐 Your language is set to {lang}',
        'help_user': '**⌨️ USER COMMANDS**',
        'help_admin': '**🛠️ ADMIN COMMANDS**',
        'shutdown_confirm': 'Shutting down... Goodbye!',
        'no_perms': '❌ You do not have permission to use this.',
        'afk_on': '🌙 You are now AFK.',
        'afk_off': '👋 Welcome back! AFK removed.',
        'qea_not_found': '❌ Question not found. Use a number between 1 and 4.',
    },
    'it': {
        'ping': '🏓 Pong! {latency}ms',
        'language_info': '🌐 La lingua è impostata su {lang}',
        'help_user': '**⌨️ COMANDI UTENTE**',
        'help_admin': '**🛠️ COMANDI ADMIN**',
        'shutdown_confirm': 'Spegnimento in corso... Arrivederci!',
        'no_perms': '❌ Non hai i permessi per usare questo.',
        'afk_on': '🌙 Sei ora in modalità AFK.',
        'afk_off': '👋 Sei tornato! AFK rimosso.',
        'qea_not_found': '❌ Domanda non trovata. Usa un numero da 1 a 4.',
    },
    'es': {
        'ping': '🏓 ¡Pong! {latency}ms',
        'language_info': '🌐 Tu idioma está configurado en {lang}',
        'help_user': '**⌨️ COMANDOS DE USUARIO**',
        'help_admin': '**🛠️ COMANDOS ADMIN**',
        'shutdown_confirm': 'Apagando... ¡Adiós!',
        'no_perms': '❌ No tienes permiso para usar esto.',
        'afk_on': '🌙 Ahora estás AFK.',
        'afk_off': '👋 ¡Has vuelto! AFK eliminado.',
        'qea_not_found': '❌ Pregunta no encontrada. Usa un número entre 1 y 4.',
    },
    'ja': {
        'ping': '🏓 ポン！{latency}ms',
        'language_info': '🌐 言語が{lang}に設定されました',
        'help_user': '**⌨️ ユーザーコマンド**',
        'help_admin': '**🛠️ 管理者コマンド**',
        'shutdown_confirm': 'シャットダウン中...さようなら！',
        'no_perms': '❌ 権限がありません。',
        'afk_on': '🌙 AFKモードになりました。',
        'afk_off': '👋 お帰りなさい！AFKが解除されました。',
        'qea_not_found': '❌ 質問が見つかりません。1から4までの番号を使用してください。',
    }
}
# Mappatura lingue disponibili
LANGUAGES = {'English': 'en', 'Italiano': 'it', 'Español': 'es', '日本語': 'ja'}

def get_lang(user_id):
    return LANG_PREFS.get(str(user_id), 'it')  # default Italiano

def save_prefs():
    with open(LANG_FILE, 'w') as f:
        json.dump(LANG_PREFS, f)

# ---------------------------
# BOT INIT
# ---------------------------
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True
intents.guild_reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ---------------------------
# EVENTI
# ---------------------------
@bot.event
async def on_ready():
    print(f"[INFO] Bot is online as {bot.user}")
    # Sync slash commands
    await bot.tree.sync()

# ---------------------------
# SLASH COMMAND: Set language
# ---------------------------
@bot.tree.command(name='set_language', description='Select your preferred language')
@app_commands.choices(language=[app_commands.Choice(name=nm, value=code) for nm, code in LANGUAGES.items()])
async def set_language(interaction: discord.Interaction, language: app_commands.Choice[str]):
    LANG_PREFS[str(interaction.user.id)] = language.value
    save_prefs()
    msg = TRANSLATIONS[language.value]['language_info'].format(lang=language.name)
    await interaction.response.send_message(msg, ephemeral=True)

# ---------------------------
# COMANDI UTENTE
# ---------------------------
@bot.command()
async def ping(ctx):
    lang = get_lang(ctx.author.id)
    latency = round(bot.latency * 1000)
    await ctx.send(TRANSLATIONS[lang]['ping'].format(latency=latency))

@bot.command()
async def language(ctx, lang_code: str = None):
    """
    Se chiamato senza argomenti, mostra la lingua corrente.
    Se passato un codice (en, it, es, ja), imposta la lingua preferita.
    """
    if lang_code:
        code = lang_code.lower()
        if code in TRANSLATIONS:
            LANG_PREFS[str(ctx.author.id)] = code
            save_prefs()
            # Nome leggibile
            name = next(name for name, val in LANGUAGES.items() if val == code)
            await ctx.send(TRANSLATIONS[code]['language_info'].format(lang=name))
        else:
            # Lingua non valida
            current = get_lang(ctx.author.id)
            available = ', '.join(LANGUAGES.keys())
            await ctx.send(f"❌ Codice lingua non valido. Scegli tra: {available}")
    else:
        # Mostra lingua corrente
        lang = get_lang(ctx.author.id)
        name = next(name for name, val in LANGUAGES.items() if val == lang)
        await ctx.send(TRANSLATIONS[lang]['language_info'].format(lang=name))
@bot.command()
async def helpme(ctx):
    lang = get_lang(ctx.author.id)
    help_text = (
        f"{TRANSLATIONS[lang]['help_user']}\n"
        "`!ping` - Mostra latenza\n"
        "`!language` - Mostra lingua corrente\n"
        "`!helpme` - Questo messaggio\n"
        "`!afk` - Attiva/disattiva AFK\n"
        "`!qea <numero>` - Risponde alle domande 1-4\n"
        "`!qeahelp` - Elenco domande per !qea\n"
        "`!helpmeadmin` - Comandi admin (solo Admin)\n"
    )
    await ctx.send(help_text)

@bot.command()
async def shutdown(ctx):
    if not ctx.author.guild_permissions.administrator:
        lang = get_lang(ctx.author.id)
        await ctx.send(TRANSLATIONS[lang]['no_perms'])
        return
    await ctx.send(TRANSLATIONS[get_lang(ctx.author.id)]['shutdown_confirm'])
    await asyncio.sleep(1)
    await bot.close()

# ---------------------------
# AFK
# ---------------------------
afk_users = {}
@bot.command()
async def afk(ctx):
    lang = get_lang(ctx.author.id)
    member = ctx.author
    uid = member.id
    if uid in afk_users:
        await member.edit(nick=afk_users[uid])
        await ctx.send(TRANSLATIONS[lang]['afk_off'])
        del afk_users[uid]
    else:
        afk_users[uid] = member.display_name
        await member.edit(nick=f"AFK - {member.display_name}")
        await ctx.send(TRANSLATIONS[lang]['afk_on'])

# ---------------------------
# QEA (Q&A)
# ---------------------------
QEA_LIST = {
    1: {"question": "Cos'è il cambiamento climatico?", "answer": "..."},
    2: {"question": "Come funzionano le intelligenze artificiali?", "answer": "..."},
    3: {"question": "Cos'è il computer vision?", "answer": "..."},
    4: {"question": "Cos'è GitHub?", "answer": "..."}
}
@bot.command()
async def qeahelp(ctx):
    qeahelptext = (
        "**1.** Cos'è il cambiamento climatico?\n"
        "**2.** Come funzionano le intelligenze artificiali?\n"
        "**3.** Cos'è il computer vision?\n"
        "**4.** Cos'è GitHub?\n"
        "Usa `!qea <numero>` per le risposte!"
    )
    await ctx.send(qeahelptext)

@bot.command()
async def qea(ctx, number: int):
    lang = get_lang(ctx.author.id)
    if number in QEA_LIST:
        q = QEA_LIST[number]
        await ctx.send(f"**{number}. {q['question']}**\n{q['answer']}")
    else:
        await ctx.send(TRANSLATIONS[lang]['qea_not_found'])

# ---------------------------
# AUTORISED CHECKER PER ADMIN
# ---------------------------
def is_admin():
    async def predicate(ctx):
        if ctx.author.guild_permissions.administrator:
            return True
        await ctx.send(TRANSLATIONS[get_lang(ctx.author.id)]['no_perms'])
        return False
    return commands.check(predicate)

# ---------------------------
# COMANDI ADMIN
# ---------------------------
@bot.command()
@is_admin()
async def helpmeadmin(ctx):
    help_text = (
        f"{TRANSLATIONS[get_lang(ctx.author.id)]['help_admin']}\n"
        "`!createchannel <nome> <tipo>` - Crea text/voice channel\n"
        "`!createrole <nome> <#colore>` - Crea ruolo HEX\n"
        "`!modchannel <#canale> <nuovo_nome>` - Rinomina canale\n"
        "`!modrole <@ruolo> <#colore>` - Cambia colore ruolo\n"
        "`!rolestemplate <template>` - Ruoli da template\n"
        "`!shutdown` - Spegni bot\n"
    )
    await ctx.send(help_text)

@bot.command()
@is_admin()
async def createchannel(ctx, name: str, channel_type: str):
    guild = ctx.guild
    if channel_type.lower() == "text":
        await guild.create_text_channel(name)
        await ctx.send(f"✅ Canale testuale `{name}` creato.")
    elif channel_type.lower() == "voice":
        await guild.create_voice_channel(name)
        await ctx.send(f"✅ Canale vocale `{name}` creato.")
    else:
        await ctx.send("❌ Tipo non valido. Usa text o voice.")

@bot.command()
@is_admin()
async def createrole(ctx, name: str, color: str):
    try:
        clr = discord.Color(int(color.strip('#'),16))
        await ctx.guild.create_role(name=name, color=clr)
        await ctx.send(f"✅ Ruolo `{name}` creato con colore `{color}`.")
    except:
        await ctx.send("❌ Errore: formato colore HEX richiesto (#ff0000)")

@bot.command()
@is_admin()
async def modchannel(ctx, channel: discord.TextChannel, *, new_name: str):
    old = channel.name
    await channel.edit(name=new_name)
    await ctx.send(f"🔧 `{old}` rinominato in `{new_name}`.")

@bot.command()
@is_admin()
async def modrole(ctx, role: discord.Role, color: str):
    try:
        clr = discord.Color(int(color.strip('#'),16))
        await role.edit(color=clr)
        await ctx.send(f"🎨 `{role.name}` colore aggiornato a `{color}`.")
    except:
        await ctx.send("❌ Colore HEX non valido.")

TEMPLATES = {
    'default': ["Owner","Admin","Moderator","Trial","Vip","User"],
    'media': ["Owner","Admin","Sr.Mod","Mod","Staff","Abbonato","Iscritto","Utente"],
    'levels':["Level 100","Level 50","Level 25","Level 10","Level 5","Level 0"]
}

@bot.command()
@is_admin()
async def rolestemplate(ctx, template: str):
    t=template.lower()
    if t not in TEMPLATES:
        await ctx.send("❌ Template non trovato. Usa default, media o levels.")
        return
    created=[]
    for rn in TEMPLATES[t]:
        if not discord.utils.get(ctx.guild.roles,name=rn):
            await ctx.guild.create_role(name=rn)
            created.append(rn)
    if created:
        await ctx.send(f"✅ Ruoli creati: {', '.join(created)}")
    else:
        await ctx.send("ℹ️ Tutti i ruoli già esistenti.")

# ---------------------------
# BOT RUN
# ---------------------------

bot.run("BOT TOKEN")