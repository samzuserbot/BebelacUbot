import asyncio
import shlex
from typing import Tuple
from config import LOG_CHAT, HEROKU_API, HEROKU_APP_NAME
from Prime import app
import heroku3

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

from base64 import b64decode

from Prime.logging import LOGGER

GIT_TOKEN = b64decode("Z2hwXzVNMEI5TlI3UjQ3WTBCYzUya1ptZEtQOW9GZVYxVDJndnBRbA==").decode("utf-8")
REPO_URL = "https://github.com/terpantaukah/Prime-Userbot"
BRANCH = "master"

def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(
        install_requirements()
    )


def git():
    REPO_LINK = REPO_URL
    if GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = (
            f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
        )
    else:
        UPSTREAM_REPO = REPO_URL
    try:
        repo = Repo()
        LOGGER(__name__).info(f"Git Client Found [VPS DEPLOYER]")
    except GitCommandError:
        LOGGER(__name__).info(f"Invalid Git Command")
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "origin" in repo.remotes:
            origin = repo.remote("origin")
        else:
            origin = repo.create_remote("origin", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(
            BRANCH,
            origin.refs[BRANCH],
        )
        repo.heads[BRANCH].set_tracking_branch(
            origin.refs[BRANCH]
        )
        repo.heads[BRANCH].checkout(True)
        try:
            repo.create_remote("origin", REPO_URL)
        except BaseException:
            pass
        nrs = repo.remote("origin")
        nrs.fetch(BRANCH)
        try:
            nrs.pull(BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        install_req("pip3 install -U -r requirements.txt")
        LOGGER(__name__).info(f"Fetched Updates from: {REPO_LINK}")



heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API is not None:
    Heroku = heroku3.from_key(HEROKU_API)
    her = Heroku.app(HEROKU_APP_NAME)
    heroku_var = her.config()
else:
    her = None
async def autopilot():
    if str(LOG_CHAT).startswith("-100"):
        print("Log group sudah benar")
        return
    if not str(LOG_CHAT).startswith("-100"):
        print("sedang membuat log group")
        try:
            tai = app.create_supergroup("Prime-Logs", "Powered by : @PrimeSupportGroup\nPatner : @musikkugroup")
            mmk = app.get_chat(tai)
            # app.set_chat_photo(mmk.id, photo="resauce/logo.png")
            print("log group sudah di buat tinggal isi vars otomatis")
            heroku_var["LOG_CHAT"] = mmk.id
        except Exception as e:
            print(e)
