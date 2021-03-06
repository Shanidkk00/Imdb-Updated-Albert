# (c) [Muhammed] @PR0FESS0R-99
# (s) @Mo_Tech_YT , @Mo_Tech_Group, @MT_Botz
# Copyright permission under MIT License
# All rights reserved by PR0FESS0R-99
# License -> https://github.com/PR0FESS0R-99/DonLee-Robot-V2/blob/Professor-99/LICENSE

import random
from countryinfo import CountryInfo
from pyrogram import filters, Client as DonLee_Robot_V2
from DonLee_Robot_V2.Config_Vars.H_Vars import BUTTONS
from DonLee_Robot_V2 import Config, Import 

@DonLee_Robot_V2.on_message(filters.command(["country"]))
async def country_info(bot, update: Import.Msg):
    country = update.text.split(" ", 1)[1]
    country = CountryInfo(country)
    info = f"""π’ππππππ π¨ππΏππππΊππππ

π­πΊππΎ : {country.name()}

π­πΊππππΎ π­πΊππΎ : {country.native_name()}

π’πΊππππΊπ : {country.capital()}

Population : <code>{country.population()}</code>

π±πΎππππ : {country.region()}

π²ππ» π±πΎππππ : {country.subregion()}

π³ππ π«πΎππΎπ π£πππΊπππ : {country.tld()}

π’πΊπππππ π’ππ½πΎπ : {country.calling_codes()}

π’ππππΎππΌππΎπ : {country.currencies()}

π±πΎπππ½πΎππΌπΎ : {country.demonym()}

π³πππΎππππΎ : <code>{country.timezones()}</code>

π¬πΊπ½πΎ π»π @Sanoob_Achu_18"""
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    buttons=[[
      Import.Button("πΆπππππΎπ½ππΊ", url=f"{country.wiki()}"),
      Import.Button("π¦πππππΎ", url=f"https://www.google.com/search?q={country_name}")
    ]]
    try:
        await update.reply_photo(
            photo=random.choice(Config.PHOTO),
            caption=info,
            reply_markup=Import.Markup(buttons),
            quote=True
        )
    except Exception as error:
        await update.reply_text(
            text=error,
            disable_web_page_preview=True,
            quote=True
        )
