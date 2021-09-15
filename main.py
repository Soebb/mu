from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import io
from PIL import Image
import mutagen
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
import requests
from music_tag import load_file
from config import Config

Bot = Client(
    "Bot",
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)


START_TXT = """
Hi {}, I'm Forward Tag Remover bot.\n\nForward me some messages, i will remove forward tag from them.\nAlso can do it in channels.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/samadii/ChannelForwardTagRemover'),
        ]]
    )


@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.channel & filters.video)
async def vid(bot, m):
    await m.edit(f"{m.video.file_name.replace('.mp4', '').replace('.webm', '').replace('.mkv', '')}\n\n🆔👉 @dlmacvin_music")

@Bot.on_message(filters.channel & filters.audio)
async def tag(bot, m):
    if "wikiseda" in m.caption:
        channel = -1001271917335
    else:
        channel = -1001516208383
    fname = m.audio.file_name
    if fname.__contains__("@") or fname.__contains__("["):
        first = fname.split(' ')[0]
        if "@" in first:
            filename = fname.split(f'{first}', -1)
        elif fname.__contains__("(@") and not "@" in first:
            filename = fname.split("(@")[-2]
        elif fname.__contains__("[@") and not "@" in first:
            filename = fname.split("[@")[-2]
        elif fname.__contains__("[") and not "@" in first:
            filename = fname.split("[")[-2]
        elif (not "@" in first) and (not fname.__contains__("(@") or fname.__contains__("[") or fname.__contains__("[@")):
            filename = fname.split("@")[-2]
    else:
        filename = fname
  
    
    try:
        m = await bot.get_messages(m.chat.id, m.message_id)
        file = await m.download(file_name="temp/file.mp3")
        await m.delete()
        music = load_file("temp/file.mp3")
        t = f"{music['title']}"
        a = f"{music['artist']}"
        al = f"{music['album']}"
        g = f"{music['genre']}"
        c = f"{music['comment']}"
        l = f"{music['lyrics']}"
        ar = music['artwork']
        image_data = ar.value.data
        img = Image.open(io.BytesIO(image_data))
        img.save("artwork.jpg")
    except Exception as e:
        print(e)
    
    
    if g.__contains__("@") or g.__contains__("["):
        first = g.split(' ')[0]
        if "@" in first:
            genre = g.split(f'{first}', -1)
        elif g.__contains__("(@") and not "@" in first:
            genre = g.split("(@")[-2]
        elif g.__contains__("[@") and not "@" in first:
            genre = g.split("[@")[-2]
        elif g.__contains__("[") and not "@" in first:
            genre = g.split("[")[-2]
        elif (not "@" in first) and (not g.__contains__("(@") or g.__contains__("[") or g.__contains__("[@")):
            genre = g.split("@")[-2]
    else:
        genre = g

    
    if l.__contains__("@") or l.__contains__("["):
        first = l.split(' ')[0]
        if "@" in first:
            lyrics = l.split(f'{first}', -1)
        elif l.__contains__("(@") and not "@" in first:
            lyrics = l.split("(@")[-2]
        elif l.__contains__("[@") and not "@" in first:
            lyrics = l.split("[@")[-2]
        elif l.__contains__("[") and not "@" in first:
            lyrics = l.split("[")[-2]
        elif (not "@" in first) and (not l.__contains__("(@") or l.__contains__("[") or l.__contains__("[@")):
            lyrics = l.split("@")[-2]
    else:
        lyrics = l

    if c.__contains__("@") or c.__contains__("["):
        first = c.split(' ')[0]
        if "@" in first:
            comment = c.split(f'{first}', -1)
        elif c.__contains__("(@") and not "@" in first:
            comment = c.split("(@")[-2]
        elif c.__contains__("[@") and not "@" in first:
            comment = c.split("[@")[-2]
        elif c.__contains__("[") and not "@" in first:
            comment = c.split("[")[-2]
        elif (not "@" in first) and (not c.__contains__("(@") or c.__contains__("[") or c.__contains__("[@")):
            comment = c.split("@")[-2]
    else:
        comment = c

    if t.__contains__("@") or t.__contains__("["):
        first = t.split(' ')[0]
        if "@" in first:
            title = t.split(f'{first}', -1)
        elif t.__contains__("(@") and not "@" in first:
            title = t.split("(@")[-2]
        elif t.__contains__("[@") and not "@" in first:
            title = t.split("[@")[-2]
        elif t.__contains__("[") and not "@" in first:
            title = t.split("[")[-2]
        elif (not "@" in first) and (not t.__contains__("(@") or t.__contains__("[") or t.__contains__("[@")):
            title = t.split("@")[-2]
    else:
        title = t

    if al.__contains__("@") or al.__contains__("["):
        first = al.split(' ')[0]
        if "@" in first:
            album = al.split(f'{first}', -1)
        elif al.__contains__("(@") and not "@" in first:
            album = al.split("(@")[-2]
        elif al.__contains__("[@") and not "@" in first:
            album = al.split("[@")[-2]
        elif al.__contains__("[") and not "@" in first:
            album = al.split("[")[-2]
        elif (not "@" in first) and (not al.__contains__("(@") or al.__contains__("[") or al.__contains__("[@")):
            album = al.split("@")[-2]
    else:
        album = al

    if a.__contains__("@") or a.__contains__("["):
        first = a.split(' ')[0]
        if "@" in first:
            artist = a.split(f'{first}', -1)
        elif a.__contains__("(@") and not "@" in first:
            artist = a.split("(@")[-2]
        elif a.__contains__("[@") and not "@" in first:
            artist = a.split("[@")[-2]
        elif a.__contains__("[") and not "@" in first:
            artist = a.split("[")[-2]
        elif (not "@" in first) and (not a.__contains__("(@") or a.__contains__("[") or a.__contains__("[@")):
            artist = a.split("@")[-2]
    else:
        artist = a

    try:
        await bot.send_photo(
            chat_id=m.chat.id,
            caption="🎤" + artist + " - " + title + "🎼" + "\n\n" + "#" + artist.split(f"{artist}", 0)[0].replace(" ", "_") + " #" + title.split(f"{title}", 0)[0].replace(" ", "_") + "\n\n" + "🆔👉 @dlmacvin_music",
            photo=open('artwork.jpg', 'rb')
        )
    except Exception as err:
        print(err)

    if ".mp3" in file:
        audio = MP3(file)
        length = audio.info.length * 0.33
        l2 = (audio.info.length * 0.33) + 30
    if ".m4a" in file:
        audio = MP4(file)
        length = audio.info.length * 0.33
        l2 = (audio.info.length * 0.33) + 30
    if audio.info.length > l2:
        os.system("ffmpeg -ss " + str(length) + " -t 30 -y -i \"" + file + "\" -ac 1 -map 0:a -codec:a libopus -b:a 128k -vbr off -ar 24000 temp/output.ogg")
    else:
        os.system("ffmpeg -ss 0 -t 30 -y -i \"" + file + "\" -ac 1 -map 0:a -codec:a libopus -b:a 128k -vbr off -ar 24000 temp/output.ogg")
    sendVoice(m.chat.id, "temp/output.ogg", f"🎤{artist} - {title}🎼\n\n🆔👉 @dlmacvin_music")
        
    music.remove_tag('comment')
    music.remove_tag('artist')
    music.remove_tag('lyrics')
    music.remove_tag('title')
    music.remove_tag('album')
    music.remove_tag('genre')
    music.remove_tag('artwork')
    music['artwork'] = open('artwork.jpg', 'rb').read()
    music['artist'] = "@dlmacvin_music"
    music['title'] = title + "[@dlmacvin_music]"
    music['album'] = album
    music['lyrics'] = lyrics
    music['genre'] = genre 
    music['comment'] = comment
    music.save()
    caption = "🎤" + artist + " - " + title + "🎼" + "\n\n" + "#" + artist.split(f"{artist}", 0)[0].replace(" ", "_") + " #" + title.split(f"{title}", 0)[0].replace(" ", "_") + "\n\n" + "🆔👉 @dlmacvin_music"
    try:
        await bot.send_audio(
            chat_id=m.chat.id,
            file_name=filename + ".mp3",
            caption=caption,
            thumb=open('artwork.jpg', 'rb'),
            audio="temp/file.mp3"
        )
    except Exception as e:
        print(e)
    

def sendVoice(chat_id,file_name,text):
    url = "https://api.telegram.org/bot%s/sendVoice"%(Config.BOT_TOKEN)
    files = {'voice': open(file_name, 'rb')}
    data = {'chat_id' : chat_id, 'caption' : text}
    r= requests.post(url, files=files, data=data)
   
Bot.run()
