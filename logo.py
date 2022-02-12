@bot.on_message(filters.command(["logo"]))
async def logo(_, m : Message):
    if len(m.command) <2:
        return await m.reply_text("Please provide a name")
    else: 
        try:
            hee = await m.reply("making your logo...")
            name = m.text.split(None, 1)[1]
            req = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={name}")
            IMG = req.text
            await hee.delete()
            await m.reply_photo(IMG) 
        except Exception as e:
            await m.reply_text(f"Error: {e}")
