print(">>> BOT FILE LOADED <<<")

import os, discord, asyncio, json, time, re, aiohttp
from discord.ext import commands
from flask import Flask
from threading import Thread
import datetime

app = Flask('')

@app.route('/')
def home():
    return "OK"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)  # help_command=None αφαιρεί το !help
GUILD_ID = 1483104426037219371

# ── ROLE IDs ──────────────────────────────────────────────────
FOUNDER_ROLE_ID        = 1483104426465165421
OWNER_ID               = 1483104426465165420
CO_OWNER_ID            = 1483104426465165419

DEVELOPER_ID           = 1483104426431610981
MANAGER_ID             = 1483104426456780880
STAFF_ID               = 1483104426439737507
CIVILIAN_MANAGER_ID    = 1504617395401134161
CRIMINAL_MANAGER_ID    = 1483104426456780875
DUTY_ROLE_ID           = 1483104426037219372
AUTOROLE_ID            = 1483104426037219376
DONATE_MANAGER_ID      = 1483104426465165416

POLICE_ROLE_ID         = 1483104426422964293
EKAB_ROLE_ID           = 1483104426422964291
LIMENIKO_ROLE_ID       = 1504618618124767232
DIMARXIO_ROLE_ID       = 1483104426431610974
STRATOS_ROLE_ID        = 1504618773561348188
STAFF_APP_ROLE_ID      = 1504618019488534651
MANAGER_APP_ROLE_ID    = 1504618019488534651

POLICE_RESULTS_CHANNEL_ID   = 1504583708735438868
EKAB_RESULTS_CHANNEL_ID     = 1504583732437319711
LIMENIKO_RESULTS_CHANNEL_ID = 1504583961635196928
DIMARXIO_RESULTS_CHANNEL_ID = 1504583884006756415
STRATOS_RESULTS_CHANNEL_ID  = 1504583844660248690
STAFF_RESULTS_CHANNEL_ID    = 1504583608688443584
MANAGER_RESULTS_CHANNEL_ID  = 1504583635515212059

POLICE_CATEGORY_ID   = 1504585636705865818
EKAB_CATEGORY_ID     = 1504585636705865818
LIMENIKO_CATEGORY_ID = 1504585636705865818
DIMARXIO_CATEGORY_ID = 1504585636705865818
STRATOS_CATEGORY_ID  = 1504585636705865818
STAFF_CATEGORY_ID    = 1504585636705865818
MANAGER_CATEGORY_ID  = 1504585636705865818

DUTY_LOG_CHANNEL_ID   = 1504583283495665925
INVITE_LOG_CHANNEL_ID = 1504583413359972402

MAIN_TICKET_CATEGORY_ID   = 1504591642072453235
JOB_TICKET_CATEGORY_ID    = 1504591281442128043
DONATE_TICKET_CATEGORY_ID = 1504589006749438023
TEMP_VOICE_CATEGORY_ID    = 1504585516966744094
TEMP_VOICE_CHANNEL_ID     = 1483104428692340908

BOT_LOG_ID                    = 1504583330564280391
MESSAGE_EDIT_LOG_CHANNEL_ID   = 1504583504334422036
MESSAGE_DELETE_LOG_CHANNEL_ID = 1504583504334422036
MEMBER_JOIN_LOG_CHANNEL_ID    = 1504583011772006552
MEMBER_LEAVE_LOG_CHANNEL_ID   = 1504583011772006552
ROLE_UPDATE_LOG_CHANNEL_ID    = 1504583111986643045
VOICE_LOG_CHANNEL_ID          = 1504583133507620875
CHANNEL_CREATE_LOG_CHANNEL_ID = 1504583155066339428
CHANNEL_DELETE_LOG_CHANNEL_ID = 1504583155066339428
ROLE_CREATE_LOG_CHANNEL_ID    = 1504583111986643045
ROLE_DELETE_LOG_CHANNEL_ID    = 1504583111986643045
TICKET_LOG_ID                 = 1504583434285224027

STAFF_ALERT_CHANNEL_ID = 1483104428692340907  # ← Κανάλι για tag staff

DUTY_VOICE_1_ID = 1483104427828314308  # ← Duty voice channel 1
DUTY_VOICE_2_ID = 1483104427828314309  # ← Duty voice channel 2

MEMBERS_CHANNEL_ID = 1504585073423290528
BOTS_CHANNEL_ID    = 1504585203195056128
ONLINE_CHANNEL_ID  = 1504585172694335608
BOOSTS_CHANNEL_ID  = 1504585237592674487

APPLICATION_MANAGER_ROLES = [FOUNDER_ROLE_ID]

THUMBNIAL_URL  = "https://i.imgur.com/O2qQ0Qp.png"
BANNER_SUPPORT = "https://i.imgur.com/BJiWiz8.jpeg"
BANNER_JOB     = "https://i.imgur.com/BJiWiz8.jpeg"
BANNER_APP     = "https://i.imgur.com/BJiWiz8.jpeg"
BANNER_DONATE  = "https://i.imgur.com/BJiWiz8.jpeg"

# ══════════════════════════════════════════════════════════════
#  CUSTOM EMOJI
# ══════════════════════════════════════════════════════════════
EMOJI_SUPPORT   = "<:EMOJI_NAME:1505583043489042494>"
EMOJI_BAN       = "<:EMOJI_NAME:1505162274183319552>"
EMOJI_REPORT    = "<:EMOJI_NAME:1505585303124181155>"
EMOJI_BUG       = "<:EMOJI_NAME:1505161769897955398>"
EMOJI_OTHER     = "<:EMOJI_NAME:1505162431800807475>"
EMOJI_CLIP      = "<:EMOJI_NAME:1505162242604269568>"
EMOJI_ANTICHEAT = "<:EMOJI_NAME:1505162454068625438>"
EMOJI_OWNERSHIP = "<:EMOJI_NAME:1504849520033402890>"

EMOJI_CIVILIAN  = "<:EMOJI_NAME:1505585352100810772>"
EMOJI_CRIMINAL  = "<:EMOJI_NAME:1505585326360367228>"

EMOJI_POLICE    = "<:EMOJI_NAME:1505162327681404960>"
EMOJI_EKAB      = "<:EMOJI_NAME:1505162309209690114>"
EMOJI_LIMENIKO  = "<:EMOJI_NAME:1505162194537549924>"
EMOJI_DIMARXIO  = "<:EMOJI_NAME:1505585352100810772>"
EMOJI_STRATOS   = "<:EMOJI_NAME:1505162177932300369>"
EMOJI_STAFF     = "<:EMOJI_NAME:1505162242604269568>"
EMOJI_MANAGER   = "<:EMOJI_NAME:1505161769897955398>"

EMOJI_DONATE    = "<:EMOJI_NAME:1505161941402914846>"
EMOJI_DUTY_LB   = "<:EMOJI_NAME:1504849629743812658>"
EMOJI_DUTY_ST   = "<:EMOJI_NAME:1505585303124181155>"

# ── QUESTIONS ─────────────────────────────────────────────────
STAFF_QUESTIONS = [
    "Πόσο χρονών είσαι?","Πώς σε λένε στο roblox?","Πόσες ώρες θα μπορείς να είσαι on duty?",
    "Έχεις εμπειρία από staff? Αν ναι που?","Τι θα κάνεις αν φίλος σου κάνει abuse perms?",
    "Τι θα κάνεις αν ένα member προσβάλει κάποιο staff?","Τι θα κάνεις αν υπάρχουν πολλά άτομα στο support?",
    "Τι βήματα θα ακολουθήσεις αν αναφερθεί ένα περιστατικό in game?",
    "Τι θα κάνεις αν αναφερθεί RDM/VDM?","Γιατί να επιλέξουμε εσένα?"
]
MANAGER_QUESTIONS = [
    "Πόσο χρονών είσαι?","Πώς σε λένε στο roblox?","Πόσες ώρες θα μπορείς να είσαι on duty?",
    "Τι θέση manager θέλεις?","Έχεις εμπειρία management? Αν ναι που?",
    "Τι θα κάνεις αν τα μέλη τσακώνονται?","Πως θα κρατήσεις την ομαδικότητα?",
    "Τι θα κάνεις αν ένα member/staff δεν υπακούει τους κανόνες?",
    "Γνωρίζεις ότι σε ticket δεν απαντάς αν έχει ήδη απαντηθεί?",
    "Τι θα κάνεις αν υπάρχουν πολλά άτομα στο support?","Γιατί να επιλέξουμε εσένα?"
]
POLICE_QUESTIONS = [
    "Πόσο χρονών είσαι?","Πως σε λένε στο roblox?",
    "Ποια είναι η βασική αποστολή της Αστυνομίας μέσα στο RP και πώς την εφαρμόζεις στην πράξη?",
    "Πώς διαχειρίζεσαι ένα περιστατικό όπου ο πολίτης δεν συνεργάζεται αλλά δεν παρανομεί?",
    "Πότε επιτρέπεται η χρήση θανατηφόρας βίας και ποια είναι η διαδικασία κλιμάκωσης?",
    "Πώς αντιδράς όταν άλλος αστυνομικός παραβιάζει πρωτόκολλο μπροστά σου?",
    "Πώς χειρίζεσαι καταγγελία πολίτη για κατάχρηση εξουσίας?",
    "Έχεις υπό κράτηση άτομο που κάνει FailRP. Ποια είναι η σωστή διαδικασία?",
    "Ένας συνάδελφος κάνει RDM. Ποια είναι η άμεση ενέργειά σου?"
]
EKAB_QUESTIONS = [
    "Πόσο χρονών είσαι?","Πως σε λένε στο roblox?",
    "Ποια είναι η βασική αποστολή του ΕΚΑΒ μέσα στο RP και πώς την εφαρμόζεις στην πράξη?",
    "Ποια είναι η προτεραιότητα ενός διασώστη σε σκηνή πολλαπλών τραυματιών?",
    "Πώς αντιδράς όταν άλλος διασώστης παραβιάζει πρωτόκολλο μπροστά σου?",
    "Πώς χειρίζεσαι καταγγελία πολίτη για αμέλεια ή κακή συμπεριφορά?",
    "Έχεις υπό φροντίδα τραυματία που κάνει FailRP. Ποια είναι η σωστή διαδικασία?",
    "Πολίτης προσποιείται τραυματισμό για να αποφύγει σύλληψη. Πώς το χειρίζεσαι?",
    "Άλλος διασώστης κάνει powergaming σε revive. Ποια είναι η αντίδρασή σου?"
]
LIMENIKO_QUESTIONS = [
    "Πόσο χρονών είσαι?","Πως σε λένε στο roblox?",
    "Ποια είναι η κύρια αποστολή του Λιμενικού στο RP?",
    "Πώς διαχειρίζεσαι ύποπτο σκάφος που δεν υπακούει σε εντολές?",
    "Πότε επιτρέπεται η χρήση θαλάσσιας καταδίωξης?",
    "Μέλος του Λιμενικού κάνει κατάχρηση εξουσίας. Πώς το χειρίζεσαι?",
    "Έχεις υπό κράτηση άτομο που κάνει FailRP. Ποια είναι η σωστή διαδικασία?",
    "Πολίτης προσποιείται τραυματισμό για να αποφύγει σύλληψη. Πώς το χειρίζεσαι?"
]
DIMARXIO_QUESTIONS = [
    "Πόσο χρονών είσαι?","Πως σε λένε στο roblox?",
    "Ποια είναι η ευθύνη ενός δημοτικού υπαλλήλου απέναντι στους πολίτες?",
    "Πώς διαχειρίζεσαι παράπονο πολίτη για κακή εξυπηρέτηση?",
    "Πώς αντιδράς όταν άλλος υπάλληλος παραβιάζει πρωτόκολλο μπροστά σου?",
    "Πολίτης ζητάει άδεια που δεν δικαιούται. Πώς το χειρίζεσαι?",
    "Υπάλληλος παρακάμπτει διαδικασίες για φίλο του. Ποια είναι η αντίδρασή σου?",
    "Κατά τη διάρκεια δημόσιας εκδήλωσης, δημιουργείται ένταση. Πώς την ελέγχεις?"
]
STRATOS_QUESTIONS = [
    "Πόσο χρονών είσαι?","Πως σε λένε στο roblox?",
    "Ποια είναι η διαφορά μεταξύ στρατιωτικής και αστυνομικής αρμοδιότητας?",
    "Πότε επιτρέπεται ο Στρατός να επέμβει σε αστικό περιβάλλον?",
    "Πώς διαχειρίζεσαι εντολή ανωτέρου που θεωρείς λανθασμένη?",
    "Έχεις εντολή να φυλάξεις στρατιωτική βάση και πολίτης προσπαθεί να μπει. Πώς αντιδράς?",
    "Στρατιώτης παραβιάζει στρατιωτικό πρωτόκολλο. Πώς το αναφέρεις?"
]

# ── PERMISSION HELPERS ────────────────────────────────────────
OWNERSHIP_IDS = (FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID)

def is_founder(u):     return any(r.id == FOUNDER_ROLE_ID for r in u.roles)
def is_ownership(u):   return any(r.id in OWNERSHIP_IDS for r in u.roles)
def can_manage_applications(u): return any(r.id in APPLICATION_MANAGER_ROLES for r in u.roles)
def has_staff_permissions(m):
    return (m.guild_permissions.kick_members or m.guild_permissions.ban_members or
            any(r.id in (STAFF_ID, MANAGER_ID, OWNER_ID, CO_OWNER_ID, FOUNDER_ROLE_ID) for r in m.roles))
def is_staff_or_manager(m):
    return any(r.id in (STAFF_ID, MANAGER_ID, OWNER_ID, CO_OWNER_ID, FOUNDER_ROLE_ID) for r in m.roles)

# ── DATA FILES ────────────────────────────────────────────────
DUTY_FILE = "duty.json"
def load_duty_data():
    if not os.path.exists(DUTY_FILE): open(DUTY_FILE,"w").write("{}")
    return json.load(open(DUTY_FILE))
def save_duty_data(d): json.dump(d, open(DUTY_FILE,"w"), indent=4)
duty_data = load_duty_data()

INVITE_FILE = "invites.json"
def load_invite_data():
    if not os.path.exists(INVITE_FILE): open(INVITE_FILE,"w").write("{}")
    return json.load(open(INVITE_FILE))
def save_invite_data(d): json.dump(d, open(INVITE_FILE,"w"), indent=4)
invite_data  = load_invite_data()
invite_cache = {}

# cooldown για !invites (30 λεπτά για civilians)
invites_cooldown = {}   # {user_id: last_used_timestamp}
INVITES_COOLDOWN_SECS = 30 * 60  # 30 λεπτά

ALT_ACCOUNT_AGE_DAYS = 30
ALT_AUTO_KICK        = True
locked_applications  = set()

DUTY_VOICE_CHANNELS  = {DUTY_VOICE_1_ID, DUTY_VOICE_2_ID}
voice_duty_sessions  = {}   # {user_id_str: start_time}

# ── VOICE COUNTERS ────────────────────────────────────────────
async def update_voice_channels(guild):
    for ch_id, name in [
        (MEMBERS_CHANNEL_ID, f"👤 Members: {sum(1 for m in guild.members if not m.bot)}"),
        (BOTS_CHANNEL_ID,    f"🤖 Bots: {sum(1 for m in guild.members if m.bot)}"),
        (ONLINE_CHANNEL_ID,  f"🟢 Online: {sum(1 for m in guild.members if m.status != discord.Status.offline)}"),
        (BOOSTS_CHANNEL_ID,  f"🚀 Boosts: {guild.premium_subscription_count}"),
    ]:
        ch = guild.get_channel(ch_id)
        if ch:
            try: await ch.edit(name=name)
            except: pass

@bot.event
async def on_presence_update(before, after): await update_voice_channels(after.guild)
@bot.event
async def on_guild_update(before, after):
    if before.premium_subscription_count != after.premium_subscription_count:
        await update_voice_channels(after)

# ══════════════════════════════════════════════════════════════
#  LOGS
# ══════════════════════════════════════════════════════════════
@bot.event
async def on_voice_state_update(member, before, after):
    guild = member.guild
    log   = bot.get_channel(VOICE_LOG_CHANNEL_ID)

    # ── Temp support channel ──
    if after.channel and after.channel.id == TEMP_VOICE_CHANNEL_ID:
        cat = guild.get_channel(TEMP_VOICE_CATEGORY_ID)
        tc  = await guild.create_voice_channel(name=f"{member.name}'s Support", category=cat)
        try: await member.move_to(tc)
        except: pass
        if log:
            e = discord.Embed(title="📞 Support Channel Created", color=discord.Color.blue(), timestamp=discord.utils.utcnow())
            e.set_thumbnail(url=member.display_avatar.url)
            e.add_field(name="👤 Χρήστης", value=f"{member.mention} (`{member.id}`)", inline=True)
            e.add_field(name="📁 Κανάλι",  value=f"**{tc.name}**", inline=True)
            e.set_footer(text=f"Quantum Roleplay • Voice Log | Channel ID: {tc.id}")
            await log.send(embed=e)
        # Tag staff στο alert channel
        alert_ch = guild.get_channel(STAFF_ALERT_CHANNEL_ID)
        if alert_ch:
            sr = guild.get_role(STAFF_ID); mr = guild.get_role(MANAGER_ID)
            tags = " ".join(r.mention for r in [sr, mr] if r)
            await alert_ch.send(f"{tags}\n🎙️ {member.mention} μπήκε στο Voice Support → **{tc.name}**!")

    if (before.channel and before.channel.category_id == TEMP_VOICE_CATEGORY_ID
            and before.channel.id != TEMP_VOICE_CHANNEL_ID
            and len(before.channel.members) == 0):
        try:
            nc = before.channel.name
            await before.channel.delete()
            if log:
                e = discord.Embed(title="🗑️ Support Channel Deleted", color=discord.Color.red(), timestamp=discord.utils.utcnow())
                e.add_field(name="📁 Κανάλι", value=f"**{nc}**", inline=True)
                e.add_field(name="📌 Λόγος",  value="Κανένας μέσα", inline=True)
                e.set_footer(text="Quantum Roleplay • Voice Log")
                await log.send(embed=e)
        except: pass

    # ── Duty voice tracking ──
    uid = str(member.id)
    entered = after.channel and after.channel.id in DUTY_VOICE_CHANNELS
    left    = before.channel and before.channel.id in DUTY_VOICE_CHANNELS

    if entered and not left:
        voice_duty_sessions[uid] = time.time()
        duty_log = bot.get_channel(DUTY_LOG_CHANNEL_ID)
        if duty_log:
            e = discord.Embed(title="🎙️ Voice Duty Start", color=discord.Color.green(), timestamp=discord.utils.utcnow())
            e.set_thumbnail(url=member.display_avatar.url)
            e.add_field(name="👤 Χρήστης", value=f"{member.mention} (`{member.id}`)", inline=True)
            e.add_field(name="🔊 Κανάλι",  value=f"**{after.channel.name}**", inline=True)
            e.set_footer(text=f"Quantum Roleplay • Voice Duty Log | User ID: {member.id}")
            await duty_log.send(embed=e)

    elif left and not entered:
        if uid in voice_duty_sessions:
            elapsed = time.time() - voice_duty_sessions.pop(uid)
            if uid not in duty_data or not isinstance(duty_data[uid], dict):
                duty_data[uid] = {"total_seconds": 0.0}
            duty_data[uid]["total_seconds"] = duty_data[uid].get("total_seconds", 0.0) + elapsed
            save_duty_data(duty_data)
            h, rem = divmod(int(elapsed), 3600); m2, s2 = divmod(rem, 60)
            total = duty_data[uid].get("total_seconds", 0.0)
            th, tr = divmod(int(total), 3600); tm2, _ = divmod(tr, 60)
            duty_log = bot.get_channel(DUTY_LOG_CHANNEL_ID)
            if duty_log:
                e = discord.Embed(title="🎙️ Voice Duty End", color=discord.Color.red(), timestamp=discord.utils.utcnow())
                e.set_thumbnail(url=member.display_avatar.url)
                e.add_field(name="👤 Χρήστης", value=f"{member.mention} (`{member.id}`)", inline=True)
                e.add_field(name="🔇 Κανάλι",  value=f"**{before.channel.name}**", inline=True)
                e.add_field(name="⏱ Session",  value=f"{h}ω {m2}λ {s2}δ", inline=True)
                e.add_field(name="📊 Σύνολο",  value=f"{th}ω {tm2}λ", inline=True)
                e.set_footer(text=f"Quantum Roleplay • Voice Duty Log | User ID: {member.id}")
                await duty_log.send(embed=e)

    # ── General voice logs ──
    if not log: return
    if not before.channel and after.channel:
        e = discord.Embed(title="🔊 Voice Join", color=discord.Color.green(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης", value=f"{member.mention} (`{member.id}`)", inline=True)
        e.add_field(name="🔊 Κανάλι",  value=f"**{after.channel.name}**", inline=True)
        e.set_footer(text=f"Quantum Roleplay • Voice Log | User ID: {member.id}")
        await log.send(embed=e)
    elif before.channel and not after.channel:
        e = discord.Embed(title="🔇 Voice Leave", color=discord.Color.red(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης", value=f"{member.mention} (`{member.id}`)", inline=True)
        e.add_field(name="🔇 Κανάλι",  value=f"**{before.channel.name}**", inline=True)
        e.set_footer(text=f"Quantum Roleplay • Voice Log | User ID: {member.id}")
        await log.send(embed=e)
    elif before.channel != after.channel:
        e = discord.Embed(title="🔀 Voice Move", color=discord.Color.yellow(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης", value=f"{member.mention} (`{member.id}`)", inline=False)
        e.add_field(name="📤 Από",     value=f"**{before.channel.name}**", inline=True)
        e.add_field(name="📥 Σε",      value=f"**{after.channel.name}**",  inline=True)
        e.set_footer(text=f"Quantum Roleplay • Voice Log | User ID: {member.id}")
        await log.send(embed=e)

@bot.event
async def on_guild_role_create(role):
    log = bot.get_channel(ROLE_CREATE_LOG_CHANNEL_ID)
    if not log: return
    moderator = "Άγνωστος"
    try:
        async for entry in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create):
            moderator = entry.user.mention; break
    except: pass
    e = discord.Embed(title="🆕 Ρόλος Δημιουργήθηκε", color=discord.Color.green(), timestamp=discord.utils.utcnow())
    e.add_field(name="📛 Όνομα",   value=f"**{role.name}**", inline=True)
    e.add_field(name="🎨 Χρώμα",  value=str(role.color),     inline=True)
    e.add_field(name="👤 Από",     value=moderator,           inline=True)
    e.add_field(name="🆔 Role ID", value=f"`{role.id}`",      inline=True)
    e.set_footer(text="Quantum Roleplay • Role Log")
    await log.send(embed=e)

@bot.event
async def on_guild_role_delete(role):
    log = bot.get_channel(ROLE_DELETE_LOG_CHANNEL_ID)
    if not log: return
    moderator = "Άγνωστος"
    try:
        async for entry in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete):
            moderator = entry.user.mention; break
    except: pass
    e = discord.Embed(title="🗑️ Ρόλος Διαγράφηκε", color=discord.Color.red(), timestamp=discord.utils.utcnow())
    e.add_field(name="📛 Όνομα",   value=f"**{role.name}**", inline=True)
    e.add_field(name="👤 Από",     value=moderator,           inline=True)
    e.add_field(name="🆔 Role ID", value=f"`{role.id}`",      inline=True)
    e.set_footer(text="Quantum Roleplay • Role Log")
    await log.send(embed=e)

@bot.event
async def on_member_update(before, after):
    guild = after.guild
    log   = bot.get_channel(ROLE_UPDATE_LOG_CHANNEL_ID)
    if not log: return
    if len(after.roles) > len(before.roles):
        new_role = next(r for r in after.roles if r not in before.roles)
        async for entry in guild.audit_logs(limit=5, action=discord.AuditLogAction.member_role_update):
            if entry.target.id == after.id:
                e = discord.Embed(title="➕ Role Added", color=discord.Color.green(), timestamp=discord.utils.utcnow())
                e.set_thumbnail(url=after.display_avatar.url)
                e.add_field(name="👤 Χρήστης",   value=f"{after.mention} (`{after.id}`)", inline=True)
                e.add_field(name="🎭 Ρόλος",     value=f"**{new_role.name}**",            inline=True)
                e.add_field(name="🛡️ Moderator", value=entry.user.mention,               inline=True)
                e.set_footer(text=f"Quantum Roleplay • Role Log | Role ID: {new_role.id}")
                await log.send(embed=e); break
    elif len(after.roles) < len(before.roles):
        removed = next(r for r in before.roles if r not in after.roles)
        async for entry in guild.audit_logs(limit=5, action=discord.AuditLogAction.member_role_update):
            if entry.target.id == after.id:
                e = discord.Embed(title="➖ Role Removed", color=discord.Color.red(), timestamp=discord.utils.utcnow())
                e.set_thumbnail(url=after.display_avatar.url)
                e.add_field(name="👤 Χρήστης",   value=f"{after.mention} (`{after.id}`)", inline=True)
                e.add_field(name="🎭 Ρόλος",     value=f"**{removed.name}**",             inline=True)
                e.add_field(name="🛡️ Moderator", value=entry.user.mention,               inline=True)
                e.set_footer(text=f"Quantum Roleplay • Role Log | Role ID: {removed.id}")
                await log.send(embed=e); break

@bot.event
async def on_guild_channel_create(channel):
    # Παράλειψε ticket/application channels
    skip_cats = {
        MAIN_TICKET_CATEGORY_ID, JOB_TICKET_CATEGORY_ID, DONATE_TICKET_CATEGORY_ID,
        TEMP_VOICE_CATEGORY_ID, POLICE_CATEGORY_ID, EKAB_CATEGORY_ID,
        LIMENIKO_CATEGORY_ID, DIMARXIO_CATEGORY_ID, STRATOS_CATEGORY_ID,
        STAFF_CATEGORY_ID, MANAGER_CATEGORY_ID
    }
    if hasattr(channel, "category_id") and channel.category_id in skip_cats: return
    log = bot.get_channel(CHANNEL_CREATE_LOG_CHANNEL_ID)
    if not log: return
    moderator = "Άγνωστος"
    try:
        async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create):
            moderator = entry.user.mention; break
    except: pass
    e = discord.Embed(title="📁 Κανάλι Δημιουργήθηκε", color=discord.Color.green(), timestamp=discord.utils.utcnow())
    e.add_field(name="📛 Όνομα",      value=f"**{channel.name}**",         inline=True)
    e.add_field(name="📂 Τύπος",     value=str(channel.type).capitalize(), inline=True)
    e.add_field(name="👤 Από",        value=moderator,                      inline=True)
    if hasattr(channel, "category") and channel.category:
        e.add_field(name="🗂️ Κατηγορία", value=channel.category.name,   inline=True)
    e.add_field(name="🆔 Channel ID", value=f"`{channel.id}`",            inline=True)
    e.set_footer(text="Quantum Roleplay • Channel Log")
    await log.send(embed=e)

@bot.event
async def on_guild_channel_delete(channel):
    log = bot.get_channel(CHANNEL_DELETE_LOG_CHANNEL_ID)
    if not log: return
    moderator = "Άγνωστος"
    try:
        async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete):
            moderator = entry.user.mention; break
    except: pass
    e = discord.Embed(title="🗑️ Κανάλι Διαγράφηκε", color=discord.Color.red(), timestamp=discord.utils.utcnow())
    e.add_field(name="📛 Όνομα",      value=f"**{channel.name}**",         inline=True)
    e.add_field(name="📂 Τύπος",     value=str(channel.type).capitalize(), inline=True)
    e.add_field(name="👤 Από",        value=moderator,                      inline=True)
    e.add_field(name="🆔 Channel ID", value=f"`{channel.id}`",            inline=True)
    e.set_footer(text="Quantum Roleplay • Channel Log")
    await log.send(embed=e)

@bot.event
async def on_message_edit(before, after):
    if before.author.bot or before.content == after.content: return
    log = bot.get_channel(MESSAGE_EDIT_LOG_CHANNEL_ID)
    if not log: return
    e = discord.Embed(title="✏️ Μήνυμα Επεξεργάστηκε", color=discord.Color.orange(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=before.author.display_avatar.url)
    e.add_field(name="👤 Χρήστης", value=f"{before.author.mention} (`{before.author.id}`)", inline=True)
    e.add_field(name="📢 Κανάλι",  value=before.channel.mention, inline=True)
    e.add_field(name="📝 Πριν",    value=before.content[:1020] or "*[κενό]*", inline=False)
    e.add_field(name="📝 Μετά",    value=after.content[:1020]  or "*[κενό]*", inline=False)
    e.add_field(name="🔗 Link",    value=f"[Πήγαινε στο μήνυμα]({after.jump_url})", inline=False)
    e.set_footer(text=f"Quantum Roleplay • Message Log | User ID: {before.author.id}")
    await log.send(embed=e)

@bot.event
async def on_message_delete(message):
    if message.author.bot: return
    log = bot.get_channel(MESSAGE_DELETE_LOG_CHANNEL_ID)
    if not log: return
    e = discord.Embed(title="🗑️ Μήνυμα Διαγράφηκε", color=discord.Color.red(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=message.author.display_avatar.url)
    e.add_field(name="👤 Χρήστης",     value=f"{message.author.mention} (`{message.author.id}`)", inline=True)
    e.add_field(name="📢 Κανάλι",      value=message.channel.mention, inline=True)
    e.add_field(name="📝 Περιεχόμενο", value=message.content[:1020] or "*[χωρίς κείμενο]*", inline=False)
    if message.attachments:
        e.add_field(name="📎 Αρχεία", value="\n".join(a.filename for a in message.attachments), inline=False)
    e.set_footer(text=f"Quantum Roleplay • Message Log | User ID: {message.author.id}")
    await log.send(embed=e)

# ══════════════════════════════════════════════════════════════
#  TICKET SYSTEM
# ══════════════════════════════════════════════════════════════
class TicketCloseView(discord.ui.View):
    def __init__(self, creator_id: int):
        super().__init__(timeout=None)
        self.creator_id = creator_id
        self.close_btn.custom_id = f"close_ticket_{creator_id}"

    @discord.ui.button(label="🔒 Close Ticket", style=discord.ButtonStyle.red, custom_id="close_ticket_placeholder")
    async def close_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:    cid = int(self.close_btn.custom_id.split("_")[-1])
        except: cid = self.creator_id

        if interaction.user.id == cid and not is_staff_or_manager(interaction.user):
            return await interaction.response.send_message(
                "❌ Δεν μπορείς να κλείσεις το δικό σου ticket. Επικοινώνησε με staff.", ephemeral=True)

        lc = interaction.guild.get_channel(TICKET_LOG_ID)
        if lc:
            e = discord.Embed(title="❌ Ticket Closed", color=discord.Color.red(), timestamp=discord.utils.utcnow())
            e.set_thumbnail(url=interaction.user.display_avatar.url)
            e.add_field(name="🔒 Έκλεισε από", value=interaction.user.mention, inline=True)
            e.add_field(name="📁 Κανάλι",       value=interaction.channel.name, inline=True)
            e.set_footer(text="Quantum Roleplay • Ticket Log")
            await lc.send(embed=e)
        await interaction.response.send_message("Κλείνει σε 4 δευτερόλεπτα...")
        await asyncio.sleep(4)
        try: await interaction.channel.delete()
        except: pass

def make_ticket_close_view(creator_id: int): return TicketCloseView(creator_id)

async def alert_staff_new_ticket(guild, author, channel, ticket_type: str):
    alert_ch = guild.get_channel(STAFF_ALERT_CHANNEL_ID)
    if not alert_ch: return
    sr = guild.get_role(STAFF_ID); mr = guild.get_role(MANAGER_ID)
    tags = " ".join(r.mention for r in [sr, mr] if r)
    await alert_ch.send(f"{tags}\n📩 Νέο **{ticket_type}** ticket από {author.mention} → {channel.mention}")

class SupportTicketSelect(discord.ui.Select):
    def __init__(self):
        opts = [
            discord.SelectOption(label="Ownership",       description="Επικοινωνία με Ownership",    emoji=EMOJI_OWNERSHIP,  value="ownership"),
            discord.SelectOption(label="Ban Appeal",      description="Αίτηση άρσης ban",            emoji=EMOJI_BAN,        value="ban_appeal"),
            discord.SelectOption(label="Report",          description="Αναφορά ατόμου ή συμβάντος",  emoji=EMOJI_REPORT,     value="report"),
            discord.SelectOption(label="Bug Report",      description="Αναφορά bug",                 emoji=EMOJI_BUG,        value="bug_report"),
            discord.SelectOption(label="Other",           description="Άλλο θέμα",                   emoji=EMOJI_OTHER,      value="other"),
            discord.SelectOption(label="Clip Permission", description="Αίτηση άδειας clip",          emoji=EMOJI_CLIP,       value="clip_perm"),
            discord.SelectOption(label="Anticheat",       description="Θέμα anticheat",              emoji=EMOJI_ANTICHEAT,  value="anticheat"),
        ]
        super().__init__(custom_id="support_ticket_select", placeholder="Επίλεξε κατηγορία...", min_values=1, max_values=1, options=opts)

    async def callback(self, interaction: discord.Interaction):
        guild = interaction.guild; author = interaction.user
        cat   = guild.get_channel(MAIN_TICKET_CATEGORY_ID)
        if not cat: return await interaction.response.send_message("Κατηγορία δεν βρέθηκε.", ephemeral=True)
        v = self.values[0]
        own  = [FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID]
        dona = [FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID, DONATE_MANAGER_ID]
        dev  = [FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID, DEVELOPER_ID]
        smow = [FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID, MANAGER_ID, STAFF_ID]
        cfg = {
            "ownership":  (own,  f"ownership-{author.name}",  "Ownership Ticket"),
            "ban_appeal": (dona, f"ban-appeal-{author.name}", "Ban Appeal"),
            "report":     (own,  f"report-{author.name}",     "Report"),
            "bug_report": (dev,  f"bug-{author.name}",        "Bug Report"),
            "other":      (smow, f"other-{author.name}",      "Other"),
            "clip_perm":  ([FOUNDER_ROLE_ID,OWNER_ID,CO_OWNER_ID,MANAGER_ID], f"clip-{author.name}", "Clip Permission"),
            "anticheat":  (dona, f"anticheat-{author.name}",  "Anticheat"),
        }
        rids, base_name, tt = cfg[v]
        name = base_name.replace(" ","-").lower()[:80]
        ow = {guild.default_role: discord.PermissionOverwrite(view_channel=False),
              author: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)}
        for rid in rids:
            r = guild.get_role(rid)
            if r: ow[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
        ch = await guild.create_text_channel(name=name, category=cat, overwrites=ow)
        e = discord.Embed(title=f"🎫 {tt}",
            description=f"Γεια σου {author.mention}!\n\n**Η ομάδα θα σε εξυπηρετήσει σύντομα.**\nΠαρακαλώ περίγραψε το αίτημά σου.\n\n*One active ticket at a time.*",
            color=discord.Color.from_rgb(20,20,40))
        e.set_image(url=BANNER_SUPPORT); e.set_footer(text="Quantum Roleplay • Support System")
        await ch.send(embed=e, view=make_ticket_close_view(author.id))
        lc = guild.get_channel(TICKET_LOG_ID)
        if lc:
            le = discord.Embed(title="📂 Νέο Ticket", color=discord.Color.blue(), timestamp=discord.utils.utcnow())
            le.set_thumbnail(url=author.display_avatar.url)
            le.add_field(name="👤 Από",    value=author.mention, inline=True)
            le.add_field(name="📋 Τύπος", value=tt,             inline=True)
            le.add_field(name="📁 Κανάλι",value=ch.mention,     inline=True)
            le.set_footer(text="Quantum Roleplay • Ticket Log")
            await lc.send(embed=le)
        await alert_staff_new_ticket(guild, author, ch, tt)
        await interaction.response.send_message(f"Δημιουργήθηκε: {ch.mention}", ephemeral=True)

class SupportTicketPanel(discord.ui.View):
    def __init__(self): super().__init__(timeout=None); self.add_item(SupportTicketSelect())

class JobTicketView(discord.ui.View):
    def __init__(self): super().__init__(timeout=None)

    @discord.ui.button(label="Civilian", style=discord.ButtonStyle.blurple, custom_id="job_civilian", emoji=EMOJI_CIVILIAN)
    async def civilian(self, interaction, button):
        await self._create(interaction, "Civilian Job", CIVILIAN_MANAGER_ID)

    @discord.ui.button(label="Criminal", style=discord.ButtonStyle.grey, custom_id="job_criminal", emoji=EMOJI_CRIMINAL)
    async def criminal(self, interaction, button):
        await self._create(interaction, "Criminal Job", CRIMINAL_MANAGER_ID)

    async def _create(self, interaction, tt, manager_rid):
        guild = interaction.guild; author = interaction.user
        cat   = guild.get_channel(JOB_TICKET_CATEGORY_ID)
        if not cat: return await interaction.response.send_message("Κατηγορία δεν βρέθηκε.", ephemeral=True)
        prefix = "civilian" if "Civilian" in tt else "criminal"
        name   = f"{prefix}-{author.name}".replace(" ","-").lower()[:80]
        ow = {guild.default_role: discord.PermissionOverwrite(view_channel=False),
              author: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)}
        for rid in [manager_rid, FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID]:
            r = guild.get_role(rid)
            if r: ow[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
        ch = await guild.create_text_channel(name=name, category=cat, overwrites=ow)
        e = discord.Embed(title=f"🎫 {tt}",
            description=f"Γεια σου {author.mention}!\n\n**Ο Job Manager θα σε εξυπηρετήσει σύντομα.**\n\n*One active ticket at a time.*",
            color=discord.Color.from_rgb(20,20,40))
        e.set_image(url=BANNER_JOB); e.set_footer(text="Quantum Roleplay • Job System")
        await ch.send(embed=e, view=make_ticket_close_view(author.id))
        lc = guild.get_channel(TICKET_LOG_ID)
        if lc:
            le = discord.Embed(title="📂 Νέο Job Ticket", color=discord.Color.blue(), timestamp=discord.utils.utcnow())
            le.set_thumbnail(url=author.display_avatar.url)
            le.add_field(name="👤 Από",    value=author.mention, inline=True)
            le.add_field(name="📋 Τύπος", value=tt,             inline=True)
            le.add_field(name="📁 Κανάλι",value=ch.mention,     inline=True)
            le.set_footer(text="Quantum Roleplay • Ticket Log")
            await lc.send(embed=le)
        await interaction.response.send_message(f"Δημιουργήθηκε: {ch.mention}", ephemeral=True)

class DonateTicketView(discord.ui.View):
    def __init__(self): super().__init__(timeout=None)

    @discord.ui.button(label="Make a Donate", style=discord.ButtonStyle.green, custom_id="donate_ticket_btn", emoji=EMOJI_DONATE)
    async def donate(self, interaction, button):
        guild = interaction.guild; author = interaction.user
        cat   = guild.get_channel(DONATE_TICKET_CATEGORY_ID)
        if not cat: return await interaction.response.send_message("Κατηγορία δεν βρέθηκε.", ephemeral=True)
        name  = f"donate-{author.name}".replace(" ","-").lower()[:80]
        ow = {guild.default_role: discord.PermissionOverwrite(view_channel=False),
              author: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)}
        for rid in [DONATE_MANAGER_ID, FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID]:
            r = guild.get_role(rid)
            if r: ow[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
        ch = await guild.create_text_channel(name=name, category=cat, overwrites=ow)
        e = discord.Embed(title="💎 Donate Ticket",
            description=(f"Γεια σου {author.mention}!\n\n"
                         "**Ευχαριστούμε για το ενδιαφέρον σου να κάνεις donate!**\n\n"
                         "Παρακαλώ περίγραψε τι donate θέλεις και θα σε εξυπηρετήσουμε σύντομα.\n\n"
                         "*One active ticket at a time.*"),
            color=discord.Color.gold())
        e.set_image(url=BANNER_DONATE); e.set_footer(text="Quantum Roleplay • Donate System")
        await ch.send(embed=e, view=make_ticket_close_view(author.id))
        lc = guild.get_channel(TICKET_LOG_ID)
        if lc:
            le = discord.Embed(title="💎 Νέο Donate Ticket", color=discord.Color.gold(), timestamp=discord.utils.utcnow())
            le.set_thumbnail(url=author.display_avatar.url)
            le.add_field(name="👤 Από",    value=author.mention, inline=True)
            le.add_field(name="📁 Κανάλι",value=ch.mention,     inline=True)
            le.set_footer(text="Quantum Roleplay • Ticket Log")
            await lc.send(embed=le)
        await interaction.response.send_message(f"Δημιουργήθηκε: {ch.mention}", ephemeral=True)

# ══════════════════════════════════════════════════════════════
#  APPLICATION SYSTEM
# ══════════════════════════════════════════════════════════════
active_application_sessions = {}

class ReasonModal(discord.ui.Modal):
    def __init__(self, action, target_user_id, app_type, orig_msg):
        super().__init__(title=f"{'Accept' if action=='accept' else 'Deny'} — Reason")
        self.action=action; self.target_user_id=target_user_id; self.app_type=app_type; self.orig_msg=orig_msg
        self.ri = discord.ui.TextInput(label="Reason", style=discord.TextStyle.paragraph, placeholder="Γράψε λόγο...", required=True, max_length=500)
        self.add_item(self.ri)

    async def on_submit(self, interaction):
        guild=interaction.guild; reason=self.ri.value; target=guild.get_member(self.target_user_id)
        at="✅ Accepted" if self.action=="accept" else "❌ Denied"
        color=discord.Color.green() if self.action=="accept" else discord.Color.red()
        if self.orig_msg.embeds:
            oe=self.orig_msg.embeds[0]
            oe.add_field(name=f"{at} by", value=f"{interaction.user.mention} — {reason}", inline=False)
            oe.color=color
            await self.orig_msg.edit(embed=oe, view=None)
        role_map = {"police":POLICE_ROLE_ID,"ekab":EKAB_ROLE_ID,"limeniko":LIMENIKO_ROLE_ID,
                    "dimarxio":DIMARXIO_ROLE_ID,"stratos":STRATOS_ROLE_ID,
                    "staff":STAFF_APP_ROLE_ID,"manager":MANAGER_APP_ROLE_ID}
        if self.action == "accept":
            rid = role_map.get(self.app_type)
            if target and rid:
                r = guild.get_role(rid)
                if r:
                    try: await target.add_roles(r)
                    except: pass
            if target:
                try:
                    dm=discord.Embed(title="✅ Η Αίτηση έγινε δεκτή!", description=f"**Reason:** {reason}", color=discord.Color.green())
                    await target.send(embed=dm)
                except: pass
        else:
            if target:
                try:
                    dm=discord.Embed(title="❌ Η Αίτηση απορρίφθηκε.", description=f"**Reason:** {reason}", color=discord.Color.red())
                    await target.send(embed=dm)
                except: pass
                await asyncio.sleep(2)
                try: await target.kick(reason=f"Application denied: {reason}")
                except: pass
        await interaction.response.send_message(f"{at} από {interaction.user.mention}. Reason: {reason}", ephemeral=True)

class ApplicationDecisionView(discord.ui.View):
    def __init__(self, uid, app_type): super().__init__(timeout=None); self.uid=uid; self.app_type=app_type
    @discord.ui.button(label="✅ Accept with Reason", style=discord.ButtonStyle.green, custom_id="app_accept_placeholder")
    async def accept_btn(self, interaction, button):
        if not can_manage_applications(interaction.user): return await interaction.response.send_message("❌ Δεν έχεις δικαίωμα.", ephemeral=True)
        await interaction.response.send_modal(ReasonModal("accept", self.uid, self.app_type, interaction.message))
    @discord.ui.button(label="❌ Deny with Reason", style=discord.ButtonStyle.red, custom_id="app_deny_placeholder")
    async def deny_btn(self, interaction, button):
        if not can_manage_applications(interaction.user): return await interaction.response.send_message("❌ Δεν έχεις δικαίωμα.", ephemeral=True)
        await interaction.response.send_modal(ReasonModal("deny", self.uid, self.app_type, interaction.message))

class StartApplicationView(discord.ui.View):
    def __init__(self, app_type):
        super().__init__(timeout=None); self.app_type=app_type
        labels = {"police":"▶️ Start ΕΛΑΣ","ekab":"▶️ Start ΕΚΑΒ","limeniko":"▶️ Start Λιμενικό",
                  "dimarxio":"▶️ Start Δημαρχείο","stratos":"▶️ Start Στρατός",
                  "staff":"▶️ Start Staff","manager":"▶️ Start Manager"}
        self.start_btn.label      = labels.get(app_type, "▶️ Start")
        self.start_btn.custom_id  = f"start_app_{app_type}"

    @discord.ui.button(label="▶️ Start", style=discord.ButtonStyle.blurple, custom_id="start_app_placeholder")
    async def start_btn(self, interaction, button):
        if self.app_type in locked_applications:
            return await interaction.response.send_message("🔒 Αυτές οι αιτήσεις είναι κλειστές.", ephemeral=True)
        cid = interaction.channel.id
        if cid in active_application_sessions:
            return await interaction.response.send_message("Αίτηση σε εξέλιξη.", ephemeral=True)
        qs_map = {"police":POLICE_QUESTIONS,"ekab":EKAB_QUESTIONS,"limeniko":LIMENIKO_QUESTIONS,
                  "dimarxio":DIMARXIO_QUESTIONS,"stratos":STRATOS_QUESTIONS,
                  "staff":STAFF_QUESTIONS,"manager":MANAGER_QUESTIONS}
        qs = qs_map.get(self.app_type, [])
        active_application_sessions[cid] = {"user_id":interaction.user.id,"type":self.app_type,"questions":qs,"answers":[],"q_index":0}
        await interaction.response.send_message(f"**Ερώτηση 1/{len(qs)}:**\n{qs[0]}")

class SendApplicationView(discord.ui.View):
    def __init__(self, app_type, uid, qs, ans):
        super().__init__(timeout=None); self.app_type=app_type; self.uid=uid; self.qs=qs; self.ans=ans
    @discord.ui.button(label="📨 Send", style=discord.ButtonStyle.green, custom_id="send_application")
    async def send_btn(self, interaction, button):
        if interaction.user.id != self.uid: return await interaction.response.send_message("❌ Δεν είσαι εσύ.", ephemeral=True)
        guild = interaction.guild
        rc_map = {"police":POLICE_RESULTS_CHANNEL_ID,"ekab":EKAB_RESULTS_CHANNEL_ID,
                  "limeniko":LIMENIKO_RESULTS_CHANNEL_ID,"dimarxio":DIMARXIO_RESULTS_CHANNEL_ID,
                  "stratos":STRATOS_RESULTS_CHANNEL_ID,"staff":STAFF_RESULTS_CHANNEL_ID,"manager":MANAGER_RESULTS_CHANNEL_ID}
        rc = guild.get_channel(rc_map.get(self.app_type, 0))
        member = guild.get_member(self.uid)
        labels = {"police":"🚓 ΕΛΑΣ","ekab":"🚑 ΕΚΑΒ","limeniko":"⚓ Λιμενικό",
                  "dimarxio":"🏛️ Δημαρχείο","stratos":"⚔️ Στρατός","staff":"👮 Staff","manager":"👔 Manager"}
        e = discord.Embed(title=f"📋 Αίτηση {labels.get(self.app_type,self.app_type)} — {member.display_name if member else self.uid}", color=discord.Color.blurple())
        e.set_author(name=str(member), icon_url=member.avatar.url if member and member.avatar else None)
        for q,a in zip(self.qs,self.ans): e.add_field(name=f"❓ {q}", value=f"💬 {a}", inline=False)
        e.set_footer(text=f"User ID: {self.uid}")
        if rc: await rc.send(embed=e, view=ApplicationDecisionView(self.uid, self.app_type))
        await interaction.response.edit_message(content="✅ Η αίτησή σου στάλθηκε!", view=None)
        if interaction.channel.id in active_application_sessions:
            del active_application_sessions[interaction.channel.id]

async def handle_application_message(message):
    cid = message.channel.id
    if cid not in active_application_sessions: return False
    s = active_application_sessions[cid]
    if message.author.id != s["user_id"]: return False
    s["answers"].append(message.content); s["q_index"] += 1
    qs = s["questions"]; qi = s["q_index"]
    if qi < len(qs): await message.channel.send(f"**Ερώτηση {qi+1}/{len(qs)}:**\n{qs[qi]}")
    else:
        v = SendApplicationView(s["type"],s["user_id"],qs,s["answers"])
        await message.channel.send("✅ Απάντησες σε όλες! Πάτα **Send** για να στείλεις.", view=v)
    return True

# ── APPLICATION SELECT — value αγγλικό, label ελληνικό (ΔΕΝ μπερδεύονται πλέον) ──
class ApplicationSelect(discord.ui.Select):
    def __init__(self):
        opts = [
            discord.SelectOption(label="ΕΛΑΣ",       description="Αίτηση για ΕΛΑΣ",      emoji=EMOJI_POLICE,   value="police"),
            discord.SelectOption(label="ΕΚΑΒ",       description="Αίτηση για ΕΚΑΒ",      emoji=EMOJI_EKAB,     value="ekab"),
            discord.SelectOption(label="Λιμενικό",   description="Αίτηση για Λιμενικό",  emoji=EMOJI_LIMENIKO, value="limeniko"),
            discord.SelectOption(label="Δημαρχείο",  description="Αίτηση για Δημαρχείο", emoji=EMOJI_DIMARXIO, value="dimarxio"),
            discord.SelectOption(label="Στρατός",    description="Αίτηση για Στρατός",   emoji=EMOJI_STRATOS,  value="stratos"),
            discord.SelectOption(label="Staff",      description="Αίτηση για Staff",      emoji=EMOJI_STAFF,    value="staff"),
            discord.SelectOption(label="Manager",    description="Αίτηση για Manager",    emoji=EMOJI_MANAGER,  value="manager"),
        ]
        super().__init__(custom_id="unified_application_select", placeholder="📂 Επίλεξε τύπο αίτησης...", min_values=1, max_values=1, options=opts)

    async def callback(self, interaction):
        app = self.values[0]  # ΠΑΝΤΑ αγγλικό: "police", "ekab" κλπ
        if app in locked_applications:
            return await interaction.response.send_message("🔒 Αυτές οι αιτήσεις είναι κλειστές.", ephemeral=True)
        guild=interaction.guild; author=interaction.user
        cat_map = {"police":POLICE_CATEGORY_ID,"ekab":EKAB_CATEGORY_ID,"limeniko":LIMENIKO_CATEGORY_ID,
                   "dimarxio":DIMARXIO_CATEGORY_ID,"stratos":STRATOS_CATEGORY_ID,
                   "staff":STAFF_CATEGORY_ID,"manager":MANAGER_CATEGORY_ID}
        title_map = {"police":"🚓 ΕΛΑΣ Application","ekab":"🚑 ΕΚΑΒ Application","limeniko":"⚓ Λιμενικό Application",
                     "dimarxio":"🏛️ Δημαρχείο Application","stratos":"⚔️ Στρατός Application",
                     "staff":"👮 Staff Application","manager":"👔 Manager Application"}
        cat   = guild.get_channel(cat_map.get(app, 0))
        cname = f"{app}-{author.name}".replace(" ","-").lower()[:80]
        ex    = discord.utils.get(guild.text_channels, name=cname)
        if ex: return await interaction.response.send_message(f"Έχεις ήδη: {ex.mention}", ephemeral=True)
        ow = {guild.default_role: discord.PermissionOverwrite(view_channel=False),
              author: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)}
        for rid in APPLICATION_MANAGER_ROLES:
            r = guild.get_role(rid)
            if r: ow[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
        ch = await guild.create_text_channel(name=cname, category=cat, overwrites=ow)
        e = discord.Embed(title=title_map.get(app,"Application"),
            description=f"{author.mention}, πάτα το κουμπί παρακάτω για να ξεκινήσεις την αίτησή σου.",
            color=discord.Color.blurple())
        e.set_image(url=BANNER_APP); e.set_footer(text="Quantum Roleplay • Applications")
        await ch.send(embed=e, view=StartApplicationView(app))
        await interaction.response.send_message(f"Δημιουργήθηκε: {ch.mention}", ephemeral=True)

class UnifiedApplicationPanel(discord.ui.View):
    def __init__(self): super().__init__(timeout=None); self.add_item(ApplicationSelect())

# ══════════════════════════════════════════════════════════════
#  DUTY — μόνο Status + Leaderboard (voice tracking)
# ══════════════════════════════════════════════════════════════
def get_total_seconds(uid: str, now: float) -> float:
    d = duty_data.get(uid, {})
    if not isinstance(d, dict): return 0.0
    total = d.get("total_seconds", 0.0)
    if uid in voice_duty_sessions: total += now - voice_duty_sessions[uid]
    return total

class DutyView(discord.ui.View):
    def __init__(self): super().__init__(timeout=None)

    @discord.ui.button(label="Status", style=discord.ButtonStyle.blurple, custom_id="duty_status", emoji=EMOJI_DUTY_ST, row=0)
    async def duty_status(self, interaction, button):
        guild=interaction.guild; now=time.time()
        active = []
        for ch_id in DUTY_VOICE_CHANNELS:
            ch = guild.get_channel(ch_id)
            if ch:
                for m in ch.members:
                    if not m.bot:
                        uid = str(m.id)
                        elapsed = now - voice_duty_sessions.get(uid, now)
                        h,rem=divmod(int(elapsed),3600); mn,sc=divmod(rem,60)
                        active.append((m, f"{h}ω {mn}λ {sc}δ", ch.name))
        e = discord.Embed(title="📋 Duty Status", color=discord.Color.blurple(), timestamp=discord.utils.utcnow())
        if active:
            e.description = "\n".join(f"🟢 {m.mention} — `{dur}` στο **{ch}**" for m,dur,ch in active)
            e.set_footer(text=f"{len(active)} άτομα on duty | Quantum Roleplay")
        else:
            e.description = "❌ Κανένας δεν είναι On Duty αυτή τη στιγμή."
            e.set_footer(text="Quantum Roleplay • Duty Status")
        await interaction.response.send_message(embed=e, ephemeral=True)

    @discord.ui.button(label="Leaderboard", style=discord.ButtonStyle.grey, custom_id="duty_leaderboard_btn", emoji=EMOJI_DUTY_LB, row=0)
    async def leaderboard_btn(self, interaction, button):
        guild=interaction.guild; now=time.time()
        totals=[(uid, get_total_seconds(uid,now)) for uid,d in duty_data.items() if isinstance(d,dict) and get_total_seconds(uid,now)>0]
        totals.sort(key=lambda x:x[1], reverse=True)
        medals=["🥇","🥈","🥉"]
        e = discord.Embed(title="🏆 Duty Leaderboard", color=discord.Color.gold(), timestamp=discord.utils.utcnow())
        desc=""
        for i,(uid,secs) in enumerate(totals[:10]):
            member=guild.get_member(int(uid)); name=member.display_name if member else f"User {uid}"
            h,rem=divmod(int(secs),3600); mn,_=divmod(rem,60)
            medal=medals[i] if i<3 else f"**#{i+1}**"
            is_on=" 🟢" if uid in voice_duty_sessions else ""
            desc+=f"{medal} {name}{is_on} — `{h}ω {mn}λ`\n"
        e.description = desc or "Κανένας δεν έχει κάνει duty ακόμα."
        e.set_footer(text="🟢 = Τώρα on duty • Δεν επαναφέρονται ποτέ | Quantum Roleplay")
        await interaction.response.send_message(embed=e, ephemeral=True)

# ══════════════════════════════════════════════════════════════
#  ON MESSAGE
# ══════════════════════════════════════════════════════════════
spam_tracker  = {}
URL_PATTERN   = re.compile(r"(https?://|www\.)\S+|discord\.gg/\S+", re.IGNORECASE)
TOKEN_PATTERN = re.compile(r"[MNO][a-zA-Z0-9_-]{23,25}\.[a-zA-Z0-9_-]{6}\.[a-zA-Z0-9_-]{27,38}")

@bot.event
async def on_message(message):
    if message.author.bot: await bot.process_commands(message); return
    guild=message.guild; author=message.author

    if guild and TOKEN_PATTERN.search(message.content):
        try: await message.delete()
        except: pass
        log = bot.get_channel(BOT_LOG_ID)
        if log:
            e = discord.Embed(title="🔑 TOKEN DETECTED!", description=f"{author.mention} έστειλε Bot Token!\n⚠️ **Άλλαξέ το ΑΜΕΣΩΣ!**", color=discord.Color.dark_red(), timestamp=discord.utils.utcnow())
            e.set_thumbnail(url=author.display_avatar.url)
            e.add_field(name="👤 Χρήστης", value=f"{author.mention} (`{author.id}`)", inline=True)
            e.add_field(name="📢 Κανάλι",  value=message.channel.mention, inline=True)
            e.set_footer(text="Quantum Roleplay • Security Log")
            await log.send(embed=e)
        return

    if guild and URL_PATTERN.search(message.content):
        exempt = [FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID]
        if not any(r.id in exempt for r in author.roles) and not author.guild_permissions.administrator:
            try: await message.delete()
            except: pass
            try: await author.timeout(datetime.timedelta(hours=1), reason="Link detected")
            except: pass
            log = bot.get_channel(BOT_LOG_ID)
            if log:
                e = discord.Embed(title="🔗 Link Detected", description=f"{author.mention} έστειλε link — **1 ώρα timeout**.", color=discord.Color.orange(), timestamp=discord.utils.utcnow())
                e.set_thumbnail(url=author.display_avatar.url)
                e.add_field(name="👤 Χρήστης", value=f"{author.mention} (`{author.id}`)", inline=True)
                e.add_field(name="📢 Κανάλι",  value=message.channel.mention, inline=True)
                e.set_footer(text="Quantum Roleplay • Security Log")
                await log.send(embed=e)
            return

    if guild:
        uid=str(author.id); now=time.time()
        if uid not in spam_tracker: spam_tracker[uid]=[]
        spam_tracker[uid].append(now); spam_tracker[uid]=[t for t in spam_tracker[uid] if now-t<5]
        if len(spam_tracker[uid])>=7:
            spam_tracker[uid]=[]
            if not author.guild_permissions.administrator:
                try: await author.timeout(datetime.timedelta(minutes=10), reason="Spam")
                except: pass
                log = bot.get_channel(BOT_LOG_ID)
                if log:
                    e = discord.Embed(title="🚫 Spam Detected", description=f"{author.mention} έκανε spam — **10 λεπτά timeout**.", color=discord.Color.red(), timestamp=discord.utils.utcnow())
                    e.set_thumbnail(url=author.display_avatar.url)
                    e.add_field(name="👤 Χρήστης", value=f"{author.mention} (`{author.id}`)", inline=True)
                    e.add_field(name="📢 Κανάλι",  value=message.channel.mention, inline=True)
                    e.set_footer(text="Quantum Roleplay • Security Log")
                    await log.send(embed=e)

    handled = await handle_application_message(message)
    if not handled: await bot.process_commands(message)

# ══════════════════════════════════════════════════════════════
#  MEMBER JOIN / LEAVE
# ══════════════════════════════════════════════════════════════
ban_kick_tracker = {}

@bot.event
async def on_member_ban(guild, user): await _track_mass_action(guild, user, "ban")

@bot.event
async def on_member_remove(member):
    await asyncio.sleep(1)
    async for entry in member.guild.audit_logs(limit=3, action=discord.AuditLogAction.kick):
        if entry.target.id==member.id and (datetime.datetime.utcnow()-entry.created_at.replace(tzinfo=None)).seconds<5:
            await _track_mass_action(member.guild, entry.user, "kick"); break
    uid=str(member.id)
    if uid in invite_data and "invited_by" in invite_data[uid]:
        iid=invite_data[uid]["invited_by"]
        if iid in invite_data:
            invite_data[iid]["left"]=invite_data[iid].get("left",0)+1
            invite_data[iid]["real"]=max(0,invite_data[iid].get("total",0)-invite_data[iid].get("left",0))
            save_invite_data(invite_data)
    await update_voice_channels(member.guild)
    log=bot.get_channel(MEMBER_LEAVE_LOG_CHANNEL_ID)
    if log:
        roles=[r.mention for r in member.roles if r.name!="@everyone"]
        e=discord.Embed(title="🔴 Μέλος Έφυγε", color=discord.Color.red(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης",   value=f"{member.mention} (`{member.id}`)", inline=True)
        e.add_field(name="📛 Username",   value=str(member), inline=True)
        e.add_field(name="👥 Μέλη τώρα", value=str(member.guild.member_count), inline=True)
        e.add_field(name="🎭 Ρόλοι",     value=" ".join(roles) if roles else "Κανένας", inline=False)
        e.set_footer(text=f"Quantum Roleplay • Member Log | User ID: {member.id}")
        await log.send(embed=e)

async def _track_mass_action(guild, moderator, action_type):
    uid=str(moderator.id) if hasattr(moderator,"id") else str(moderator); now=time.time()
    if uid not in ban_kick_tracker: ban_kick_tracker[uid]=[]
    ban_kick_tracker[uid].append(now); ban_kick_tracker[uid]=[t for t in ban_kick_tracker[uid] if now-t<10]
    if len(ban_kick_tracker[uid])>=3:
        ban_kick_tracker[uid]=[]; mm=guild.get_member(int(uid))
        exempt=[FOUNDER_ROLE_ID,OWNER_ID]; is_ex=mm and any(r.id in exempt for r in mm.roles)
        if mm and not is_ex:
            try: await mm.timeout(datetime.timedelta(weeks=1), reason=f"Mass {action_type}")
            except: pass
            log = bot.get_channel(BOT_LOG_ID)
            if log:
                e=discord.Embed(title=f"⚠️ Mass {action_type.upper()} Detected!", description=f"{mm.mention} έκανε mass {action_type}.\n**1 εβδομάδα timeout** δόθηκε.", color=discord.Color.dark_red(), timestamp=discord.utils.utcnow())
                await log.send(embed=e)

@bot.event
async def on_member_join(member):
    guild=member.guild
    age=(datetime.datetime.utcnow()-member.created_at.replace(tzinfo=None)).days
    if age<ALT_ACCOUNT_AGE_DAYS:
        log = bot.get_channel(BOT_LOG_ID)
        if log:
            e=discord.Embed(title="🚨 ALT ACCOUNT DETECTED!", color=discord.Color.dark_red(), timestamp=discord.utils.utcnow())
            e.set_thumbnail(url=member.display_avatar.url)
            e.add_field(name="👤 Χρήστης",       value=f"{member.mention} (`{member.id}`)", inline=False)
            e.add_field(name="📅 Ηλικία",        value=f"**{age} ημέρες**", inline=True)
            e.add_field(name="📆 Δημιουργήθηκε", value=f"<t:{int(member.created_at.timestamp())}:F>", inline=True)
            if ALT_AUTO_KICK:
                try:
                    await member.kick(reason=f"Alt account — ηλικία: {age} ημέρες")
                    e.add_field(name="⚡ Ενέργεια", value="✅ **Auto-kicked**", inline=False)
                except Exception as err:
                    e.add_field(name="⚡ Ενέργεια", value=f"❌ Απέτυχε: {err}", inline=False)
            else:
                e.add_field(name="⚡ Ενέργεια", value="⚠️ Μόνο ειδοποίηση", inline=False)
            e.set_footer(text="Quantum Roleplay • Security Log")
            await log.send(embed=e)
        if ALT_AUTO_KICK: return

    r=guild.get_role(AUTOROLE_ID)
    if r:
        try: await member.add_roles(r)
        except: pass

    try:
        ni=await guild.invites(); nim={i.code:i.uses for i in ni}; inviter=None
        for code,ou in invite_cache.get(guild.id,{}).items():
            if nim.get(code,0)>ou:
                for i in ni:
                    if i.code==code: inviter=i.inviter; break
                break
        invite_cache[guild.id]=nim
        if inviter:
            iid=str(inviter.id); mid=str(member.id)
            if mid not in invite_data: invite_data[mid]={}
            invite_data[mid]["invited_by"]=iid
            if iid not in invite_data: invite_data[iid]={"total":0,"real":0,"left":0}
            invite_data[iid]["total"]=invite_data[iid].get("total",0)+1
            invite_data[iid]["real"]=invite_data[iid].get("total",0)-invite_data[iid].get("left",0)
            save_invite_data(invite_data)
            il=bot.get_channel(INVITE_LOG_CHANNEL_ID)
            if il:
                e=discord.Embed(title="📨 Νέο Invite", description=f"{member.mention} μπήκε με invite του {inviter.mention}", color=discord.Color.green(), timestamp=discord.utils.utcnow())
                e.set_thumbnail(url=member.display_avatar.url)
                e.add_field(name="📊 Inviter Stats",
                    value=(f"**Όνομα:** {inviter.display_name}\n"
                           f"**Συνολικά:** {invite_data[iid].get('total',0)}\n"
                           f"**Real:** {invite_data[iid].get('real',0)}\n"
                           f"**Έφυγαν:** {invite_data[iid].get('left',0)}"), inline=False)
                e.set_footer(text=f"Quantum Roleplay • Invite Log | User ID: {member.id}")
                await il.send(embed=e)
    except Exception as ex: print(f"Invite error: {ex}")

    log=bot.get_channel(MEMBER_JOIN_LOG_CHANNEL_ID)
    if log:
        e=discord.Embed(title="🟢 Μέλος Μπήκε", color=discord.Color.green(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης",     value=f"{member.mention} (`{member.id}`)", inline=True)
        e.add_field(name="📛 Username",     value=str(member), inline=True)
        e.add_field(name="📅 Λογαριασμός", value=f"<t:{int(member.created_at.timestamp())}:R>", inline=True)
        e.add_field(name="👥 Μέλη τώρα",   value=str(guild.member_count), inline=True)
        e.set_footer(text=f"Quantum Roleplay • Member Log | User ID: {member.id}")
        await log.send(embed=e)
    await update_voice_channels(guild)

# ══════════════════════════════════════════════════════════════
#  COMMANDS
# ══════════════════════════════════════════════════════════════

@bot.command()
async def ban(ctx, member: discord.Member=None, *, reason="No reason"):
    if not has_staff_permissions(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    if not member: return await ctx.reply("Χρήση: `!ban @user [λόγος]`")
    await member.ban(reason=reason); await ctx.reply(f"🔨 **{member}** banned.")
    log=bot.get_channel(BOT_LOG_ID)
    if log: await log.send(f"🔨 **{ctx.author}** banned **{member}** — {reason}")

@bot.command()
async def kick(ctx, member: discord.Member=None, *, reason="No reason"):
    if not has_staff_permissions(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    if not member: return await ctx.reply("Χρήση: `!kick @user [λόγος]`")
    await member.kick(reason=reason); await ctx.reply(f"👢 **{member}** kicked.")
    log=bot.get_channel(BOT_LOG_ID)
    if log: await log.send(f"👢 **{ctx.author}** kicked **{member}** — {reason}")

@bot.command()
async def timeout(ctx, member: discord.Member=None, minutes: int=None, *, reason="No reason"):
    if not has_staff_permissions(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    if not member or not minutes: return await ctx.reply("Χρήση: `!timeout @user <minutes> [λόγος]`")
    await member.timeout(datetime.timedelta(minutes=minutes), reason=reason)
    await ctx.reply(f"⏳ **{member}** timeout {minutes} λεπτά.")
    log=bot.get_channel(BOT_LOG_ID)
    if log: await log.send(f"⏳ **{ctx.author}** timed out **{member}** {minutes}min — {reason}")

@bot.command()
async def clearmessage(ctx, amount: int=None):
    if not has_staff_permissions(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    if not amount: return await ctx.reply("Χρήση: `!clearmessage <amount>`")
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"🧹 Διαγράφηκαν **{amount}** μηνύματα.", delete_after=3)

@bot.command()
async def serverstatus(ctx):
    if not is_staff_or_manager(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    g=ctx.guild
    e=discord.Embed(title="📊 Server Status", color=discord.Color.blurple(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=g.icon.url if g.icon else None)
    e.add_field(name="👤 Members", value=sum(1 for m in g.members if not m.bot))
    e.add_field(name="🤖 Bots",    value=sum(1 for m in g.members if m.bot))
    e.add_field(name="🟢 Online",  value=sum(1 for m in g.members if m.status!=discord.Status.offline))
    e.add_field(name="🚀 Boosts",  value=g.premium_subscription_count)
    e.set_footer(text="Quantum Roleplay • Server Status")
    await ctx.reply(embed=e)

# ── !invites — cooldown 30 λεπτά για non-staff ────────────────
@bot.command()
async def invites(ctx, member: discord.Member=None):
    uid = str(ctx.author.id)
    now = time.time()

    # Αν έχει περάσει άλλο user αλλά δεν είναι staff, δεν επιτρέπεται
    if member and member.id != ctx.author.id and not is_staff_or_manager(ctx.author):
        return await ctx.reply("❌ Μπορείς να δεις μόνο τα δικά σου invites.")

    # Cooldown για non-staff
    if not is_staff_or_manager(ctx.author):
        last_used = invites_cooldown.get(uid, 0)
        remaining = INVITES_COOLDOWN_SECS - (now - last_used)
        if remaining > 0:
            mins = int(remaining // 60); secs = int(remaining % 60)
            return await ctx.reply(f"⏳ Cooldown! Μπορείς να το ξαναχρησιμοποιήσεις σε **{mins}λ {secs}δ**.", delete_after=10)
        invites_cooldown[uid] = now

    t = member if (member and is_staff_or_manager(ctx.author)) else ctx.author
    d = invite_data.get(str(t.id), {"total":0,"real":0,"left":0})
    e = discord.Embed(title=f"📨 Invites — {t.display_name}", color=discord.Color.blurple(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=t.display_avatar.url)
    e.add_field(name="📊 Συνολικά", value=str(d.get("total",0)), inline=True)
    e.add_field(name="✅ Real",     value=str(d.get("real",0)),  inline=True)
    e.add_field(name="🚪 Έφυγαν",  value=str(d.get("left",0)),  inline=True)
    e.set_footer(text="Quantum Roleplay • Invite Log")
    await ctx.reply(embed=e)

# ── !addinvites — μόνο Founder ────────────────────────────────
@bot.command()
async def addinvites(ctx, member: discord.Member=None, amount: int=None):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    if not member or amount is None:
        return await ctx.reply("Χρήση: `!addinvites @user <ποσότητα>`\nΜπορείς να βάλεις και αρνητικό για να αφαιρέσεις.")
    uid = str(member.id)
    if uid not in invite_data or not isinstance(invite_data[uid], dict):
        invite_data[uid] = {"total":0,"real":0,"left":0}
    invite_data[uid]["total"] = invite_data[uid].get("total",0) + amount
    invite_data[uid]["real"]  = max(0, invite_data[uid].get("total",0) - invite_data[uid].get("left",0))
    save_invite_data(invite_data)
    d = invite_data[uid]; sign = "+" if amount >= 0 else ""
    e = discord.Embed(title="📨 Invites Updated", color=discord.Color.green(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=member.display_avatar.url)
    e.add_field(name="👤 Χρήστης",  value=member.mention,       inline=True)
    e.add_field(name="📝 Αλλαγή",   value=f"`{sign}{amount}`",  inline=True)
    e.add_field(name="📊 Συνολικά", value=str(d.get("total",0)), inline=True)
    e.add_field(name="✅ Real",      value=str(d.get("real",0)),  inline=True)
    e.add_field(name="🚪 Έφυγαν",   value=str(d.get("left",0)),  inline=True)
    e.set_footer(text=f"Quantum Roleplay • Founder Action | {ctx.author}")
    await ctx.reply(embed=e)

@bot.command()
async def serverinvites(ctx):
    if not is_staff_or_manager(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    guild=ctx.guild; entries=[]
    for uid,d in invite_data.items():
        if not isinstance(d,dict): continue
        total=d.get("total",0)
        if total<=0: continue
        m=guild.get_member(int(uid)); name=m.display_name if m else f"User {uid}"
        entries.append((name,total,d.get("real",0),d.get("left",0)))
    entries.sort(key=lambda x:x[1], reverse=True)
    e=discord.Embed(title=f"📨 Server Invites — {guild.name}", color=discord.Color.blurple(), timestamp=discord.utils.utcnow())
    if guild.icon: e.set_thumbnail(url=guild.icon.url)
    e.set_image(url=BANNER_SUPPORT)
    if entries:
        medals=["🥇","🥈","🥉"]; desc=""
        for i,(name,total,real,left) in enumerate(entries[:20]):
            medal=medals[i] if i<3 else f"**#{i+1}**"
            desc+=f"{medal} **{name}** — `{total}` συνολικά | `{real}` real | `{left}` έφυγαν\n"
        e.description=desc
    else:
        e.description="Δεν υπάρχουν δεδομένα invites ακόμα."
    e.set_footer(text=f"Quantum Roleplay • {guild.member_count} μέλη συνολικά")
    await ctx.send(embed=e)

@bot.command()
async def scan(ctx, member: discord.Member=None):
    if not is_staff_or_manager(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    await ctx.reply("🔍 Σκανάρω...", delete_after=2); guild=ctx.guild
    if member:
        age=(datetime.datetime.utcnow()-member.created_at.replace(tzinfo=None)).days
        al=[]; alb={discord.AuditLogAction.ban:"🔨 Ban",discord.AuditLogAction.kick:"👢 Kick",
                    discord.AuditLogAction.member_role_update:"🎭 Role Update",
                    discord.AuditLogAction.channel_delete:"🗑️ Channel Delete",
                    discord.AuditLogAction.role_delete:"🗑️ Role Delete"}
        try:
            async for entry in guild.audit_logs(limit=50):
                if entry.user.id==member.id and entry.action in alb:
                    al.append(f"{alb[entry.action]} → `{getattr(entry.target,'name',str(entry.target))}` <t:{int(entry.created_at.timestamp())}:R>")
                    if len(al)>=8: break
        except: pass
        e=discord.Embed(title=f"🔍 Scan — {member.display_name}",
            color=discord.Color.dark_red() if (age<ALT_ACCOUNT_AGE_DAYS or member.guild_permissions.administrator) else discord.Color.blurple(),
            timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης",       value=f"{member} (`{member.id}`)", inline=True)
        e.add_field(name="📅 Ηλικία",        value=f"{age} ημέρες {'⚠️ ALT?' if age<ALT_ACCOUNT_AGE_DAYS else '✅'}", inline=True)
        e.add_field(name="📆 Δημιουργήθηκε", value=f"<t:{int(member.created_at.timestamp())}:F>", inline=True)
        e.add_field(name="🔑 Permissions",
            value=f"Administrator: {'✅' if member.guild_permissions.administrator else '❌'}\nBan: {'✅' if member.guild_permissions.ban_members else '❌'}\nKick: {'✅' if member.guild_permissions.kick_members else '❌'}",
            inline=True)
        e.add_field(name="🎭 Ρόλοι", value=", ".join(r.mention for r in member.roles[1:]) or "Κανένας", inline=False)
        e.add_field(name=f"📋 Ενέργειες ({len(al)})", value="\n".join(al) if al else "Καμία", inline=False)
        e.set_footer(text="Quantum Roleplay • Scan")
        await ctx.send(embed=e); return
    admins=[]; newa=[]; bl=[]; sus=[]
    for m in guild.members:
        age=(datetime.datetime.utcnow()-m.created_at.replace(tzinfo=None)).days
        if m.bot:
            iv=bool(m.public_flags and discord.PublicUserFlags.verified_bot in m.public_flags)
            bl.append(f"{'✅' if iv else '⚠️'} {m.mention} (`{m.id}`)")
        if not m.bot and m.guild_permissions.administrator: admins.append(f"{m.mention} (`{m.id}`)")
        if not m.bot and age<ALT_ACCOUNT_AGE_DAYS: newa.append(f"{m.mention} — {age} ημέρες")
        if not m.bot and m.guild_permissions.administrator and age<ALT_ACCOUNT_AGE_DAYS: sus.append(f"🚨 {m.mention} — Admin + {age} ημέρες")
    e=discord.Embed(title=f"🔍 Server Scan — {guild.name}", color=discord.Color.dark_orange(), timestamp=discord.utils.utcnow())
    e.add_field(name=f"👑 Administrators ({len(admins)})",  value="\n".join(admins[:10]) or "Κανένας", inline=False)
    e.add_field(name=f"🤖 Bots ({len(bl)})",               value="\n".join(bl[:10])     or "Κανένα",  inline=False)
    e.add_field(name=f"⚠️ Νέοι < {ALT_ACCOUNT_AGE_DAYS}d ({len(newa)})", value="\n".join(newa[:10]) or "Κανένας", inline=False)
    e.add_field(name=f"🚨 Ύποπτα ({len(sus)})",            value="\n".join(sus[:10])    or "✅ Τίποτα", inline=False)
    e.set_footer(text=f"Quantum Roleplay • Scan | {guild.member_count} μέλη")
    await ctx.send(embed=e)

@bot.command()
async def say(ctx, *, message: str):
    if not is_ownership(ctx.author): return await ctx.reply("❌ Μόνο Ownership.")
    await ctx.send(message)
    try: await ctx.message.delete()
    except: pass

@bot.command()
async def say2(ctx, *, message: str):
    if not is_ownership(ctx.author): return await ctx.reply("❌ Μόνο Ownership.")
    guild=ctx.guild
    e=discord.Embed(description=message, color=discord.Color.from_rgb(20,20,40), timestamp=discord.utils.utcnow())
    if guild.icon: e.set_thumbnail(url=guild.icon.url)
    e.set_footer(text=guild.name, icon_url=guild.icon.url if guild.icon else None)
    await ctx.send(embed=e)
    try: await ctx.message.delete()
    except: pass

@bot.command()
async def dmall(ctx, *, message: str):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    guild=ctx.guild
    now_str=discord.utils.utcnow().strftime("%d/%m/%Y %H:%M UTC")
    sent=0; failed=0
    for m in guild.members:
        if m.bot: continue
        try:
            e=discord.Embed(description=message, color=discord.Color.from_rgb(20,20,40), timestamp=discord.utils.utcnow())
            if guild.icon: e.set_thumbnail(url=guild.icon.url)
            e.set_footer(text=f"Στάλθηκε από: {ctx.author.display_name} • {now_str}", icon_url=ctx.author.display_avatar.url)
            await m.send(embed=e); sent+=1
        except: failed+=1
    await ctx.reply(f"📨 Στάλθηκε σε **{sent}** μέλη. ❌ Απέτυχε σε **{failed}**.")

@bot.command()
async def lockapplication(ctx, app_type: str=None):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    valid=["police","ekab","limeniko","dimarxio","stratos","staff","manager","all"]
    if not app_type or app_type.lower() not in valid:
        status="".join(f"{'🔒' if t in locked_applications else '🔓'} **{t.capitalize()}**\n" for t in valid[:-1])
        e=discord.Embed(title="🔒 Application Lock Status", description=status, color=discord.Color.blurple())
        e.set_footer(text="Χρήση: !lockapplication <police/ekab/limeniko/dimarxio/stratos/staff/manager/all>")
        return await ctx.reply(embed=e)
    app_type=app_type.lower()
    targets=valid[:-1] if app_type=="all" else [app_type]
    toggled=[]
    for t in targets:
        if t in locked_applications: locked_applications.remove(t); toggled.append(f"🔓 **{t.capitalize()}** — Ανοιχτό")
        else: locked_applications.add(t); toggled.append(f"🔒 **{t.capitalize()}** — Κλειστό")
    e=discord.Embed(title="🔒 Application Lock", description="\n".join(toggled), color=discord.Color.orange(), timestamp=discord.utils.utcnow())
    e.set_footer(text=f"Από: {ctx.author}")
    await ctx.reply(embed=e)

# ── !addemoji — Ownership: προσθέτει emoji στον server από URL ──
@bot.command()
async def addemoji(ctx, emoji_id: str=None, name: str=None):
    """Χρήση: !addemoji <emoji_id> <name>
    Το emoji_id είναι το νούμερο ID από το Discord emoji.
    """
    if not is_ownership(ctx.author): return await ctx.reply("❌ Μόνο Ownership.")
    if not emoji_id or not name:
        return await ctx.reply("Χρήση: `!addemoji <emoji_id> <name>`\n"
                               "Παράδειγμα: `!addemoji 1234567890 myemoji`\n"
                               "Το `emoji_id` το βρίσκεις κάνοντας `\\:emojname:` στο Discord.")
    # Φτιάξε URL για να κατεβάσουμε το emoji
    emoji_url = f"https://cdn.discordapp.com/emojis/{emoji_id}.png"
    try:
        async with ctx.typing():
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get(emoji_url) as resp:
                    if resp.status != 200:
                        # Δοκίμασε gif
                        emoji_url = f"https://cdn.discordapp.com/emojis/{emoji_id}.gif"
                        async with session.get(emoji_url) as resp2:
                            if resp2.status != 200:
                                return await ctx.reply("❌ Δεν βρέθηκε emoji με αυτό το ID. Σιγουρέψου ότι το ID είναι σωστό.")
                            image_data = await resp2.read()
                    else:
                        image_data = await resp.read()

        new_emoji = await ctx.guild.create_custom_emoji(name=name, image=image_data)
        e = discord.Embed(title="✅ Emoji Προστέθηκε!", color=discord.Color.green(), timestamp=discord.utils.utcnow())
        e.add_field(name="📛 Όνομα",    value=f"`{new_emoji.name}`",  inline=True)
        e.add_field(name="🆔 ID",       value=f"`{new_emoji.id}`",    inline=True)
        e.add_field(name="💬 Χρήση",    value=f"`<:{new_emoji.name}:{new_emoji.id}>`", inline=False)
        e.set_thumbnail(url=str(new_emoji.url))
        e.set_footer(text=f"Quantum Roleplay • Emoji | Από: {ctx.author}")
        await ctx.reply(embed=e)
    except discord.Forbidden:
        await ctx.reply("❌ Δεν έχω δικαίωμα.")
    except discord.HTTPException as ex:
        await ctx.reply(f"❌ Σφάλμα: `{ex}`\nΠιθανόν να έχεις φτάσει το όριο emoji του server.")
    except Exception as ex:
        await ctx.reply(f"❌ Άγνωστο σφάλμα: `{ex}`")

# ── Panels ────────────────────────────────────────────────────
@bot.command()
async def ticketpanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="Quantum Roleplay — Support Panel", description="**Επίλεξε κατηγορία για να ανοίξεις ticket.**\n*One active ticket at a time.*", color=discord.Color.from_rgb(20,20,40))
    e.set_image(url=BANNER_SUPPORT); e.set_footer(text="Quantum Roleplay • Support System")
    await ctx.send(embed=e, view=SupportTicketPanel()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

@bot.command()
async def jobpanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="Quantum Roleplay — Job Panel", description="**Επίλεξε κατηγορία job ticket.**\n*One active ticket at a time.*", color=discord.Color.from_rgb(20,20,40))
    e.set_image(url=BANNER_JOB); e.set_footer(text="Quantum Roleplay • Job System")
    await ctx.send(embed=e, view=JobTicketView()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

@bot.command()
async def donatepanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="💎 Quantum Roleplay — Donate",
        description="**Θέλεις να κάνεις donate;**\nΠάτα το κουμπί παρακάτω!\n\n*One active ticket at a time.*",
        color=discord.Color.gold())
    e.set_image(url=BANNER_DONATE); e.set_footer(text="Quantum Roleplay • Donate System")
    await ctx.send(embed=e, view=DonateTicketView()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

@bot.command()
async def applicationpanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    lock_info="".join(f"{'🔒' if t in locked_applications else '🔓'} {t.capitalize()}  " for t in ["police","ekab","limeniko","dimarxio","stratos","staff","manager"])
    e=discord.Embed(title="📋 Quantum Roleplay — Applications",
        description=f"**Επίλεξε τύπο αίτησης.**\n\n🚓 ΕΛΑΣ · 🚑 ΕΚΑΒ · ⚓ Λιμενικό\n🏛️ Δημαρχείο · ⚔️ Στρατός · 👮 Staff · 👔 Manager\n\n*Μία ενεργή αίτηση κάθε φορά.*\n\n{lock_info}",
        color=discord.Color.from_rgb(20,20,40))
    e.set_image(url=BANNER_APP); e.set_footer(text="Quantum Roleplay • Applications")
    await ctx.send(embed=e, view=UnifiedApplicationPanel()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

@bot.command()
async def dutypanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="🟢 Staff Duty Panel",
        description="Το duty μετράει **αυτόματα** όταν μπαίνεις στα duty voice channels.\n\n"
                    "📋 **Status** — Ποιοι είναι on duty τώρα\n"
                    "🏆 **Leaderboard** — Συνολικές ώρες",
        color=discord.Color.green())
    await ctx.send(embed=e, view=DutyView()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

@bot.command()
async def panel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="📌 Quantum Roleplay — Founder Panel", color=discord.Color.dark_gray(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
    e.add_field(name="🛠 Moderation",   value="`!ban` `!kick` `!timeout` `!clearmessage`", inline=False)
    e.add_field(name="📊 Info",         value="`!serverstatus` `!invites` `!serverinvites` `!scan [@user]`", inline=False)
    e.add_field(name="🧰 Utility",      value="`!say` `!say2` `!dmall`", inline=False)
    e.add_field(name="🔍 Security",     value="`!setaltdays <days>`", inline=False)
    e.add_field(name="📋 Applications", value="`!applicationpanel` `!lockapplication <type>`", inline=False)
    e.add_field(name="🎫 Panels",       value="`!ticketpanel` `!jobpanel` `!donatepanel` `!dutypanel`", inline=False)
    e.add_field(name="📨 Invites",      value="`!addinvites @user <ποσότητα>`", inline=False)
    e.add_field(name="😀 Emoji",        value="`!addemoji <emoji_id> <name>`", inline=False)
    e.set_footer(text=f"Quantum Roleplay • Founder Panel | {ctx.author}")
    await ctx.reply(embed=e)

@bot.command()
async def panel2(ctx):
    if not is_ownership(ctx.author): return await ctx.reply("❌ Μόνο Ownership.")
    e=discord.Embed(title="📌 Quantum Roleplay — Owners Panel", color=discord.Color.gold(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
    e.add_field(name="🛠 Moderation", value="`!ban` `!kick` `!timeout` `!clearmessage`", inline=False)
    e.add_field(name="📊 Info",       value="`!serverstatus` `!invites [@user]` `!serverinvites` `!scan [@user]`", inline=False)
    e.add_field(name="🧰 Utility",    value="`!say` `!say2`", inline=False)
    e.add_field(name="😀 Emoji",      value="`!addemoji <emoji_id> <name>`", inline=False)
    e.set_footer(text=f"Quantum Roleplay • Owners Panel | {ctx.author}")
    await ctx.reply(embed=e)

@bot.command()
async def panel3(ctx):
    if not is_staff_or_manager(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    e=discord.Embed(title="📌 Quantum Roleplay — Staff Panel", color=discord.Color.blurple(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
    e.add_field(name="🛠 Moderation", value="`!ban` `!kick` `!timeout` `!clearmessage`", inline=False)
    e.add_field(name="📊 Info",       value="`!serverstatus` `!invites` `!serverinvites` `!scan [@user]`", inline=False)
    e.set_footer(text=f"Quantum Roleplay • Staff Panel | {ctx.author}")
    await ctx.reply(embed=e)

# ══════════════════════════════════════════════════════════════
#  ON READY
# ══════════════════════════════════════════════════════════════
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for v in [SupportTicketPanel(), JobTicketView(), DonateTicketView(),
              DutyView(), UnifiedApplicationPanel()]:
        bot.add_view(v)
    guild=bot.get_guild(GUILD_ID)
    if guild:
        await update_voice_channels(guild)
        try:
            invs=await guild.invites()
            invite_cache[guild.id]={i.code:i.uses for i in invs}
            print(f"Loaded {len(invs)} invites.")
        except Exception as e: print(f"Invites error: {e}")
        # Resume duty tracking για όσους είναι ήδη στα voice channels
        for ch_id in DUTY_VOICE_CHANNELS:
            ch = guild.get_channel(ch_id)
            if ch:
                for m in ch.members:
                    if not m.bot:
                        uid = str(m.id)
                        if uid not in voice_duty_sessions:
                            voice_duty_sessions[uid] = time.time()
                            print(f"Resumed duty for {m.name}")
    await bot.change_presence(activity=discord.Game(name="Quantum Roleplay"))
    print("Bot fully online!")

if __name__=="__main__":
    keep_alive()
    bot.run(TOKEN)
