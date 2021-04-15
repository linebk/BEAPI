import time, requests

class BEAPI():
    def __init__(self, apikey):
        self.host = "https://beapi.me"
        self.headers = {"Apikey": apikey}
        self.session = requests.Session()

    def pretyPrint(self, djson):
        print(json.dumps(djson, indent=4, sort_keys=True))
        
    def sendPost(self, path, headers=None, data=None, files=None, djson=None):
        if headers:headers = {**headers, **self.headers}
        else:headers = self.headers
        try:r = self.session.post(self.host+path,headers=headers,data=data,files=files,json=djson).json()
        except:raise Exception("Oops... Like api is down :(")
        if r["status"] != 200:raise Exception(str(r))
        return r
    
    def sendGet(self, path, headers=None, params=None):
        if headers:headers = {**headers, **self.headers}
        else:headers = self.headers
        try:r = self.session.get(self.host+path,headers=headers,params=params).json()
        except:raise Exception("Oops... Like api is down :(")
        if r["status"] != 200:raise Exception(str(r))
        return r

    ### WALLPAPER HD ###
    def alphaCodersSearch(self, search, page=1):
        params = {"search": search, "page": str(page)}
        return self.sendGet("/alphacoders",params=params)

    ### ANIME STREAM ###
    def animeOngoing(self):
        return self.sendGet("/animeongoing")

    ### ANIMEXIN ###
    def animexinOngoing(self):
        return self.sendGet("/animexin")

    ### AUTHKEY TO PRIMARY CONVERT ###
    def authKeyToPrimary(self, authkey):
        params = {"authkey": authkey}
        return self.sendGet("/authkey2primary",params=params)

    ### BRANLY SEARCH ###
    def brainlySearch(self, search):
        params = {"search": search}
        return self.sendGet("/brainly",params=params)

    ### COOKPAD SEARCH ###
    def cookpadSearch(self, search, lang="id"): #[en,id]
        params = {"search": search, "lang": lang}
        return self.sendGet("/cookpad",params=params)

    ### DANBOORU PAGE ###
    def danbooruPage(self, page=1):
        params = {"page": str(page)}
        return self.sendGet("/danbooru",params=params)

    ### GIF SEARCH ###
    def gifSearch(self, search):
        params = {"search": search}
        return self.sendGet("/gif",params=params)

    ### GOOGLE IMAGE ###
    def googleImage(self, search):
        params = {"search": search}
        return self.sendGet("/googleimg",params=params)

    ### GOOGLE SEARCH ###
    def googleSearch(self, search):
        params = {"search": search}
        return self.sendGet("/googlesearch",params=params)

    ### IMAGEREVERSE ###
    def imageReverseWithUrl(self, url):
        params = {"url": url}
        return self.sendGet("/imgreverse",params=params)
    def imageReverseWithPath(self, path):
        url = self.uploadStorage(path)["result"]
        params = {"url": url}
        return self.sendGet("/imgreverse",params=params)

    ### INSTAGRAM ###
    def instaPost(self, url):
        params = {"url": url}
        return self.sendGet("/igpost",params=params)
    def instaProfile(self, user):
        params = {"url": user}
        return self.sendGet("/igprofile",params=params)

    ### JOOX DOWNLOAD ###
    def jooxSearch(self, search):
        params = {"search": search}
        return self.sendGet("/joox",params=params)
    def jooxSearchId(self, id_song):
        params = {"id_song": id_song}
        return self.sendGet("/joox",params=params)

    ### KAMUS BESAR BAHASA INDONESIA ###
    def KBBISearch(self, search):
        params = {"search": search}
        return self.sendGet("/kbbi",params=params)

    ### LINEAPPNAME (LAST) ###
    def lineAppName(self):
        return self.sendGet("/line_appname")

    ### APPNAMELINE (RANDOM) ###
    def lineAppNameRandom(self, osname): #['android', 'androidlite', 'ios', 'iosipad', 'desktopwin', 'desktopmac', 'chromeos']
        params = {"osname": osname}
        return self.sendGet("/line_appname_random",params=params)

    ### LINE QR ROTATE ###
    def lineQr(self, sysname="BE-Team", appName="IOSIPAD\t10.5.2\tiPhone 8\t11.2.5", cert=None):
        headers = {"appname": appName, "cert" : cert, "sysname": sysname}
        return self.sendGet("/lineqr",headers=headers)

    ### LINE Primary To Secondary ###
    def linePrimaryConvert(self, authToken, sysname="BE-Team", appName="IOSIPAD\t10.5.2\tiPhone 8\t11.2.5"):
        headers = {"appname": appName, "sysname": sysname, "authtoken": authToken}
        return self.sendGet("/lineprimary2second",headers=headers)

    ## MUSICALLYDOWN ##
    def musicallyDown(self, url):
        params = {"url": url}
        return self.sendGet("/musicallydown",params=params)
    
    ### NINE GAG ###
    def nineGagFresh(self, category): #['funny', 'among-us', 'animals', 'anime-manga', 'animewaifu', 'animewallpaper', 'apexlegends', 'ask9gag', 'awesome', 'car', 'comic-webtoon', 'coronavirus', 'cosplay', 'countryballs', 'home-living', 'crappydesign', 'cyberpunk2077', 'drawing-diy-crafts', 'rate-my-outfit', 'food-drinks', 'football', 'fortnite', 'got', 'gaming', 'gif', 'girl', 'girlcelebrity', 'guy', 'history', 'horror', 'kpop', 'timely', 'leagueoflegends', 'lego', 'superhero', 'meme', 'movie-tv', 'music', 'basketball', 'nsfw', 'overwatch', 'pcmr', 'pokemon', 'politics', 'pubg', 'random', 'relationship', 'savage', 'satisfying', 'science-tech', 'sport', 'starwars', 'school', 'travel-photography', 'video', 'wallpaper', 'warhammer', 'wholesome', 'wtf', 'darkhumor', 'funny', 'nsfw', 'girl', 'wtf', 'anime-manga', 'random', 'animals', 'animewaifu', 'awesome', 'car', 'comic-webtoon', 'cosplay', 'cyberpunk2077', 'gaming', 'gif', 'girlcelebrity', 'leagueoflegends', 'meme', 'politics', 'relationship', 'savage', 'video', 'algeria', 'argentina', 'australia', 'austria', 'bosniaherzegovina', 'bahrain', 'belgium', 'bolivia', 'brazil', 'bulgaria', 'canada', 'chile', 'colombia', 'costarica', 'croatia', 'cyprus', 'czechia', 'denmark', 'dominicanrepublic', 'ecuador', 'egypt', 'estonia', 'finland', 'france', 'georgia', 'germany', 'ghana', 'greece', 'guatemala', 'hongkong', 'hungary', 'iceland', 'india', 'indonesia', 'iraq', 'ireland', 'israel', 'italy', 'japan', 'jordan', 'kenya', 'kuwait', 'latvia', 'lebanon', 'lithuania', 'luxembourg', 'malaysia', 'mexico', 'montenegro', 'morocco', 'nepal', 'netherlands', 'newzealand', 'nigeria', 'norway', 'oman', 'pakistan', 'peru', 'philippines', 'poland', 'portugal', 'puertorico', 'qatar', 'romania', 'russia', 'saudiarabia', 'senegal', 'serbia', 'singapore', 'slovakia', 'slovenia', 'southafrica', 'southkorea', 'spain', 'srilanka', 'sweden', 'switzerland', 'taiwan', 'tanzania', 'thailand', 'tunisia', 'turkey', 'uae', 'usa', 'ukraine', 'uk', 'uruguay', 'vietnam', 'yemen', 'zimbabwe']
        params = {"category": category}
        return self.sendGet("/9gag-fresh",params=params)
    def nineGagHot(self, category):
        params = {"category": category}
        return self.sendGet("/9gag-hot",params=params)

    ### ONE CAK RANDOM ###
    def oneCakRandom(self):
        return self.sendGet("/1cak")

    ## PHOTOFUNIA ##
    def photoFunia(self, args):
        return self.sendGet("/photofunia",params=args)

    ### PRIMBON ###
    def primbonNama(self, nama):
        params = {"nama": nama}
        return self.sendGet("/primbon",params=params)
    def primbonZodiac(self, zodiac):
        params = {"zodiac": zodiac}
        return self.sendGet("/primbon",params=params)
    def primbonKecocokan(self, nama1, nama2):
        params = {"nama1": nama1, "nama2": nama2}
        return self.sendGet("/primbon",params=params)

    ## REFACE ##
    def reface(self, args):
        return self.sendGet("/reface",params=args)
    
    ### SIMISIMI ###
    def simiTalk(self, text, lang="id"):
        params = {"text": text, "lang": lang}
        return self.sendGet("/simisimi",params=params)

    ### Smule ###
    def smulePost(self, url):
        params = {"url": url}
        return self.sendGet("/smule/post",params=params)
    def smuleProfile(self, user):
        params = {"user": user}
        return self.sendGet("/smule/user",params=params)
    def smulePerformance(self, user):
        params = {"user": user}
        return self.sendGet("/smule/performance",params=params)

    ### SHORT LINK GENERATOR ###
    def shortLink(self, url):
        return self.sendPost("/short-link",data={"url": url})

    ## SCREENSHOT WEB ##
    def SSWeb(self, url):
        return self.sendPost("/ss-web",data={"url": url})

    ### TRACK RESI ###
    def trackResi(self, resi, courier):  ##['pos', 'wahana', 'jnt', 'sap', 'sicepat', 'jet', 'dse', 'first', 'ninja', 'lion', 'idl', 'rex', 'ide', 'sentral']
        params = {"resi": resi, "courier": courier}
        return self.sendGet("/track-resi",params=params)

    ### TRANSLATE AND SPEECH ###
    def translator(self, text, lang):  ##{'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan', 'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-CN': 'Chinese', 'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole', 'ha': 'Hausa', 'haw': 'Hawaiian', 'iw': 'Hebrew', 'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer', 'rw': 'Kinyarwanda', 'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongolian', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'or': 'Odia (Oriya)', 'ps': 'Pashto', 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic', 'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil', 'tt': 'Tatar', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'tk': 'Turkmen', 'uk': 'Ukrainian', 'ur': 'Urdu', 'ug': 'Uyghur', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'}
        params = {"text": text, "lang": lang}
        return self.sendGet("/translate",params=params)

    ### TEXT TO SPEECH ###
    def tts(self, text, lang):  ##{'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan', 'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-CN': 'Chinese', 'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole', 'ha': 'Hausa', 'haw': 'Hawaiian', 'iw': 'Hebrew', 'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer', 'rw': 'Kinyarwanda', 'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongolian', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'or': 'Odia (Oriya)', 'ps': 'Pashto', 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic', 'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil', 'tt': 'Tatar', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'tk': 'Turkmen', 'uk': 'Ukrainian', 'ur': 'Urdu', 'ug': 'Uyghur', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'}
        params = {"text": text, "lang": lang}
        return self.sendGet("/tts",params=params)

    ### TIKTOK ###
    def tiktokPost(self, url):
        params = {"url": url}
        return self.sendGet("/tiktok",params=params)
    def tiktokProfile(self, user):
        params = {"user": user}
        return self.sendGet("/tiktok",params=params)

    ### TEXTPRO ###
    def textPro(self, args):
        return self.sendGet("/textpro",params=args)
    
    ### FILE TO URL ( STORAGE ) ###
    def uploadStorage(self, path):
        return self.sendPost("/storage",files={"file": open(path,"rb")})

    ### YOUTUBE MP3 ###
    def youtubeMp3Url(self, url):
        params = {"url": url}
        return self.sendGet("/ytmp3",params=params)
    def youtubeMp3Search(self, search):
        params = {"search": search}
        return self.sendGet("/ytmp3",params=params)

    ### YOUTUBE MP4 ###
    def youtubeMp4Url(self, url):
        params = {"url": url}
        return self.sendGet("/ytmp4",params=params)
    def youtubeMp4Search(self, search):
        params = {"search": search}
        return self.sendGet("/ytmp4",params=params)

