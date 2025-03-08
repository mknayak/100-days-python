from InternetSpeedTwitterBot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

print(f"Internet speed is {bot.down} Mbps download / {bot.up} Mbps upload")