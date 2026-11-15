import json
from highrise import BaseBot, User
from highrise.__main__ import main, BotDefinition
from asyncio import run as arun

class MonBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Le bot est bien connecté dans la salle !")

    async def on_user_join(self, user: User, position) -> None:
        await self.highrise.chat(f"Bienvenue dans la salle, @{user.username} !")

if __name__ == "__main__":
    with open("config.json", "r") as f:
        config = json.load(f)
    arun(main([BotDefinition(MonBot(), config["room_id"], config["bot_token"])]))