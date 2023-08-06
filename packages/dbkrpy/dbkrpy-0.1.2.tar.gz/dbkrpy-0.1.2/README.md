# DBKR-API-Python

## 사용하시기 전에 읽어주세요.

* 자동으로 루프를 돕니다 task.loop를 안만드셔도됩니다(30분)

* 길드수도 안에서 체크합니다. 따로 비교안하셔도됩니다.

* 따로 루프를 만드시고싶으시다면 클래스내에 post_guild_count 라는 함수가 있습니다 인자값은 길드수와 토큰을 받으니 이 함수를 사용하세요.

## 설치 방법

```sh
pip install dbkrpy
```

## 업데이트 방법

```sh
pip install --upgrade dbkrpy
```

## 사용 예제

```py
#Auto Loop
import dbkrpy
import discord
from discord.ext import commands

class UpdateGuild(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = 'KoreanBot Token paste here'
        dbkrpy.DBKRPython(self.bot,self.token)

def setup(bot):
    bot.add_cog(UpdateGuild(bot))

```

## on_message
```py
#Auto Loop
import asyncio
import dbkrpy
import discord

client = discord.Client()

token = "token"
DBKR = "Korean Bot token"

dbkrpy.DBKRPython(client,DBKR)
```

## Patch note

### 0.1.1

* 1만서버 이상일시 오류출력.

### 0.1.0

* 첫 배포 시작
