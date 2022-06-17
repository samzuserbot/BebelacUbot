![Prime](https://telegra.ph/file/7e0c2450664bfc304203b.jpg)

# Prime

Userbot ini di buat berdasarkan library [Pyrogram](https://github.com/pyrogram/pyrogram)

# Note

> Kami tidak bertanggung jawab dengan segala masalah terhadap akun anda, ketika anda sudah berniat mendeploy bot ini, berarti anda sudah siap dengan resikonya

# Deploy on Heroku
<details>
<summary><b> 🚀 Heroku Deployment</b></summary>
<br>

<h3 align="left">Klik Tombol di Bawah ini untuk Deploy di Heroku</h3>
<p align="left"><a href="https://prime-tech-deploy.vercel.app/"><img src="https://www.herokucdn.com/deploy/button.png" alt="Deploy to Heroku" target="_blank"/></a></p>

<a href="http://telegram.dog/XTZ_HerokuBot?start=QnVrYW5EZXYvUHJpbWUtVXNlcmJvdCBtYXN0ZXI"><img src="https://telegra.ph/file/70966bb4b212649afc8dc.jpg"/></a>
</details>

# Contoh kode
> Bagi yang mau kembangin Prime-Userbot bisa lihat contoh ini

```python
from Prime import CMD_HELP, app
from config import PREFIX

CMD_HELP.update(
    {
        "repo": f"""
『 **REPO** 』
  `{PREFIX}repo` -> Untuk menampilkan repo Prime-Userbot.
"""
    }
)

@app.on_message(filters.command("repo", PREFIX) & filters.me)
async def terminal(client, message):
    await app.send_message(message.chat.id, "[PRIME - USERBOT](https://github.com/BukanDev/Prime-Userbot)")
    
```

# Credits

- [Pyrogram](https://github.com/pyrogram/pyrogram) - base
- [Toni](https://github.com/Toni880) - Prime
- [Atka](https://github.com/jokokendi) - Ice-Userbot
- [ZectUserBot](https://github.com/SHRE-YANSH)
- [TeamYukki](https://github.com/TeamYukki/YukkiMusicBot) - YukkiMusicBot
- [TheHamkerCat](https://github.com/TheHamkerCat/WilliamButcherBot) - WilliamButcherBot
- [Xyren](https://github.com/Xyren-64bit)
- [mrismanaziz](https://github.com/mrismanaziz/PyroMan-Userbot) - PyroMan-Userbot


INGAT REPO ORIGINAL MASIH DI PRIVATE KALAU ANDA MAU DEPLOY REPO INI ANDA WAJIB PUNYA GIT_TOKEN DARI ADMIN KALIAN BISA MINTA DI [@PrimeSupportGroup](https://t.me/primesupportgroup)
