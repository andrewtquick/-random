import discord
import random
from discord.ext import commands
from discord.ext.commands import command as Command
from discord.ext.commands import Context, Cog

class RandomGame(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.map = ['The SKELD', 'MIRA HQ', 'POLUS']
        self.ejects = ['Yes', 'No']
        self.emerg_cd = ['0s', '5s', '10s', '15s', '20s', '25s', '30s', '35s', '40s', '45s', '50s', '55s', '60s']
        self.discuss_time = ['0s', '15s', '30s', '45s', '60s', '75s', '90s', '105s', '120s']
        self.vote_time = ['0s', '15s', '30s', '45s', '60s', '75s', '90s', '105s', '120s', '135s', '150s', '165s', '180s', '195s', '210s', '225s', '240s', '255s', '270s', '285s', '300s']
        self.player_speed = ['0.5x', '0.75x', '1.0x', '1.25x', '1.5x', '1.75x', '2.0x', '2.25x', '2.5x', '2.75x', '3.0x']
        self.crew_vision = ['0.25x', '0.5x', '0.75x', '1.0x', '1.25x', '1.5x', '1.75x', '2.0x', '2.25x', '2.5x', '2.75x', '3.0x', '3.25x', '3.50x', '3.75x', '4.0x', '4.25x', '4.50x', '4.75x', '5.0x']
        self.impost_vision = ['0.25x', '0.5x', '0.75x', '1.0x', '1.25x', '1.5x', '1.75x', '2.0x', '2.25x', '2.5x', '2.75x', '3.0x', '3.25x', '3.50x', '3.75x', '4.0x', '4.25x', '4.50x', '4.75x', '5.0x']
        self.kill_cd = ['10s', '12.5s', '15s', '17.5s', '20s', '22.5s', '25s', '27.5s', '30s', '32.5s', '35s', '37.5s', '40s', '42.5s', '45s', '47.5s', '50s', '52.5s', '55s', '57.5s', '60s']
        self.kill_dist = ['Short', 'Normal', 'Long']
        self.visual_tasks = ['On', 'Off']
        self.random_msg = [
            'Ahhhh, feeling spicy today? Give this a shot!',
            "You just want to ruin people's day, don't cha? Have at it",
            'Does this work for you?!',
            'UGH, FINE. HERE',
            'YES, this is the BEST I can do.',
            'Good luck. You may not have any friends left after this one.',
            'MUAHAHAHAHAH, IT LIVES!! Err, I mean try this one.',
            'Best of luck, nerd.'
            ]

    @Command(name='random', help='Randomizes the game settings for Among Us')
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def random(self, ctx: Context):
        embed = discord.Embed(title="Among Us", colour=discord.Colour(0xf8e71c), description="Randomized game settings")
        embed.set_thumbnail(url="https://s2.gaming-cdn.com/images/products/7522/271x377/among-us-cover.jpg")
        embed.add_field(name="Map", value=self.map[random.randint(0,2)])
        embed.add_field(name="Imposters", value=random.randint(1,3))
        embed.add_field(name="Confirm Ejects", value=random.choice(self.ejects))
        embed.add_field(name="Emergency Meetings", value=random.randint(0,10))
        embed.add_field(name="Emergency Cooldown", value=self.emerg_cd[random.randint(0, 12)])
        embed.add_field(name="Discussion Time", value=self.discuss_time[random.randint(0, 8)])
        embed.add_field(name="Voting Time", value=self.vote_time[random.randint(0, 20)])
        embed.add_field(name="Player Speed", value=self.player_speed[random.randint(0, 10)])
        embed.add_field(name="Crewmate Vision", value=self.crew_vision[random.randint(0, 19)])
        embed.add_field(name="Imposter Vision", value=self.impost_vision[random.randint(0, 19)])
        embed.add_field(name="Kill Cooldown", value=self.kill_cd[random.randint(0, 20)])
        embed.add_field(name="Kill Distance", value=random.choice(self.kill_dist))
        embed.add_field(name="Visual Tasks", value=random.choice(self.visual_tasks))
        embed.add_field(name="Common Tasks", value=random.randint(0, 2))
        embed.add_field(name="Long Tasks", value=random.randint(0, 3))
        embed.add_field(name="Short Tasks", value=random.randint(0, 5))
        embed.set_footer(text='Among Us Game Randomizer brought to you by Xylr')
        
        await ctx.send(content=f"{ctx.author.mention} - {random.choice(self.random_msg)}", embed=embed)

def setup(bot):
    bot.add_cog(RandomGame(bot))