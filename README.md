
  <h3 align="center">BEAPI DOCUMENT</h3>

  <p align="center">
    awsome api feature from me
    <br />
    <br />
    <a href="https://beapi.me/register">REGISTER</a>
    ·
    <a href="https://wa.me/6289625658302?text=Report+Bug">REPORT ERROR</a>
    ·
    <a href="https://wa.me/6289625658302?text=Request+Feature">REQUEST FEATURE</a>
  </p>
  
  
  <!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Site Map</summary>
  <ol>
    <li><a href="#Installation"> Installation</a></li>
    <li>
      <a href="#API-List"> API List</a>
      <ul>
        <li><a href="#ALPHACODERS">AlphaCoders</a></li>
        <li><a href="#ANIMESTREAM">AnimeStream</a></li>
        <li><a href="#ANIMEXIN">AnimeXin</a></li>
        <li><a href="#AUTHKEY2PRIMARY">Authkey2Primary</a></li>
        <li><a href="#BRAINLY">BrainlySearch</a></li>
        <li><a href="#COOKPAD">CookpadSearch</a></li>
        <li><a href="#DANBOORU">DanbooruPage</a></li>
        <li><a href="#GIFSEARCH">GIFSearch</a></li>
        <li><a href="#GOOGLEIMG">GoogleImage</a></li>
        <li><a href="#GOOGLESEARCH">GoogleSearch</a></li>
        <li><a href="#INSTAGRAMPOST">InstagramPost</a></li>
        <li><a href="#INSTAGRAMPROFILE">InstagramProfile</a></li>
        <li><a href="#JOOXSEARCH">JooxSearch</a></li>
        <li><a href="#KBBISEARCH">KBBISearch</a></li>
        <li><a href="#LINEAPPNAMELAST">LineAppNameLastest</a></li>
        <li><a href="#LINEAPPNAMERANDOM">LineAppNameRandom</a></li>
        <li><a href="#LINEQRROTATE">LineQrRotate</a></li>
        <li><a href="#LINEPRIMARYCONVERT">Primary2Secondary</a></li>
        <li><a href="#MUSICALLYDOWN">MusicallyDown (TikTok Download)</a></li>
        <li><a href="#9GAG">NineGag</a></li>
      </ul>
    </li>
  </ol>
</details>

<br />
<br />

## [ Installation ]
coming soon...

<br />
<br />

<!-- API LIST -->
## [ API List ]
### ALPHACODERS
**URL :** 
<https://beapi.me/alphacoders>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `search` ( your search query )
- `page` ( page of result )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.alphaCodersSearch("naruto", 1)
  api.pretyPrint(res) #for prety print result
```

<br />

### ANIMESTREAM
**URL :** 
<https://beapi.me/animeongoing>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.animeOngoing()
  api.pretyPrint(res) #for prety print result
```

<br />

### ANIMEXIN
**URL :** 
<https://beapi.me/animexin>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.animexinOngoing()
  api.pretyPrint(res) #for prety print result
```

<br />

### AUTHKEY2PRIMARY
**URL :** 
<https://beapi.me/authkey2primary>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `authkey` ( your authkey line )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.authKeyToPrimary('your line authkey')
  api.pretyPrint(res) #for prety print result
```

<br />

### BRAINLY
**URL :** 
<https://beapi.me/brainly>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `search` ( your search query )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.brainlySearch('kenapa bumi bulat')
  api.pretyPrint(res) #for prety print result
```

<br />

### COOKPAD
**URL :** 
<https://beapi.me/cookpad>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `search` ( your search query )
- `lang` ( language [en,id] )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.cookpadSearch('nastar', 'id')
  api.pretyPrint(res) #for prety print result
```

<br />

### DANBOORU
**URL :** 
<https://beapi.me/danbooru>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `page` ( page of result )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.danbooruPage(1)
  api.pretyPrint(res) #for prety print result
```

<br />

### GIFSEARCH
**URL :** 
<https://beapi.me/gif>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `search` ( your search query )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.gifSearch("naruto")
  api.pretyPrint(res) #for prety print result
```

<br />

### GOOGLEIMG
**URL :** 
<https://beapi.me/googleimg>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `search` ( your search query )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.googleImage("naruto")
  api.pretyPrint(res) #for prety print result
```

<br />

### GOOGLESEARCH
**URL :** 
<https://beapi.me/googlesearch>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `search` ( your search query )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.googleSearch("naruto")
  api.pretyPrint(res) #for prety print result
```

<br />

### IMGREVERSE
**URL :** 
<https://beapi.me/imgreverse>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `url` ( static image url )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  #WITH URL
  res = api.imageReverseWithUrl("static_img_url")
  #WITH PATH
  res = api.imageReverseWithPath("path_to_file")
  api.pretyPrint(res) #for prety print result
```

<br />

### INSTAGRAMPOST
**URL :** 
<https://beapi.me/igpost>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `url` ( your igpost url )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.instaPost("https://www.instagram.com/p/CNLOThQjnzU/")
  api.pretyPrint(res) #for prety print result
```

<br />

### INSTAGRAMPROFILE
**URL :** 
<https://beapi.me/igprofile>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `user` ( instagram username )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.instaProfile("instagram")
  api.pretyPrint(res) #for prety print result
```

<br />

### JOOXSEARCH
**URL :** 
<https://beapi.me/joox>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `search` ( your search query ) OR `id` ( your song id ) 

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  #WITH SEARCH QUERY
  res = api.jooxSearch("bring me the horizon")
  #WITH SONG ID
  res = api.jooxSearchId("1W09eg2vDIJLQgrWOj_4FQ==")
  api.pretyPrint(res) #for prety print result
```

<br />

### KBBISEARCH
**URL :** 
<https://beapi.me/kbbi>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `search` ( your search query )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.KBBISearch("makan")
  api.pretyPrint(res) #for prety print result
```

<br />

### LINEAPPNAMELAST
**URL :** 
<https://beapi.me/appnameline>

**PRICE :**
`Free`

**METHOD :**
`GET`

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.lineAppName()
  api.pretyPrint(res) #for prety print result
```

<br />

### LINEAPPNAMERANDOM
**URL :** 
<https://beapi.me/line_appname_random>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `osname` ( osname ['android', 'androidlite', 'ios', 'iosipad', 'desktopwin', 'desktopmac', 'chromeos'] )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.lineAppNameRandom("chromeos")
  api.pretyPrint(res) #for prety print result
```

<br />

### LINEQRROTATE
**URL :** 
<https://beapi.me/lineqr>

**PRICE :**
`15 Credit`

**METHOD :**
`GET`

**HEADERS :**
- `apikey` ( optional, can input in header/arg )
- `appname` ( your appname login )
- `sysname` ( your login system name )
- `cert` ( your account cert, you can fill `None` if don't have)

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  cert = None
  res = api.lineQr(sysname="BE-Team", appName="IOSIPAD\t10.5.2\tiPhone 8\t11.2.5", cert=cert)
  print("QR Link: " + res["result"]["qr_link"])
  if not cert:
      print("Callback Pincode: " + res["result"]["cb_pincode"])
      for num in range(600):
          resx = api.sendGet(res["result"]["cb_pincode"].replace(api.host,""))
          if resx["result"] != "not ready":
              print("Your Pincode: " + resx["result"])
              break
          time.sleep(1)
      if resx["result"] == "not ready": raise Exception("login timeout!!")
  for num in range(600):
      resx = api.sendGet(res["result"]["cb_token"].replace(api.host,""))
      if resx["result"] != "not ready":
          print("Your Cert: " + resx["result"]["cert"])
          print("Your Token: " + resx["result"]["token"])
          cert, authToken= resx["result"]["cert"], resx["result"]["token"]
          break
      time.sleep(1)
  if resx["result"] == "not ready": raise Exception("login timeout!!")
```

### LINEPRIMARYCONVERT
**URL :** 
<https://beapi.me/lineprimary2second>

**PRICE :**
`15 Credit`

**METHOD :**
`GET`

**HEADERS :**
- `apikey` ( optional, can input in header/arg )
- `appname` ( your appname login )
- `sysname` ( your login system name )
- `authtoken` ( your primary authtoken)

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.linePrimaryConvert(authToken="your_authtoken", sysname="BE-Team", appName="IOSIPAD\t10.5.2\tiPhone 8\t11.2.5")
  api.pretyPrint(res) #for prety print result
```

<br />

### MUSICALLYDOWN
**URL :** 
<https://beapi.me/musicallydown>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `url` ( your tiktok url )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.musicallyDown('https://www.tiktok.com/@msglowbdl/video/6933152608211307778')
  api.pretyPrint(res) #for prety print result
```

### 9GAG
**URL :** 
<https://beapi.me/9gag-fresh> || <https://beapi.me/9gag-hot>

**PRICE :**
`10 Credit`

**METHOD :**
`GET`

**ARGS :**
- `apikey` ( optional, can input in header/arg )
- `category` ( 9gag page category ['funny', 'among-us', 'animals', 'anime-manga', 'animewaifu', 'animewallpaper', 'apexlegends', 'ask9gag', 'awesome', 'car', 'comic-webtoon', 'coronavirus', 'cosplay', 'countryballs', 'home-living', 'crappydesign', 'cyberpunk2077', 'drawing-diy-crafts', 'rate-my-outfit', 'food-drinks', 'football', 'fortnite', 'got', 'gaming', 'gif', 'girl', 'girlcelebrity', 'guy', 'history', 'horror', 'kpop', 'timely', 'leagueoflegends', 'lego', 'superhero', 'meme', 'movie-tv', 'music', 'basketball', 'nsfw', 'overwatch', 'pcmr', 'pokemon', 'politics', 'pubg', 'random', 'relationship', 'savage', 'satisfying', 'science-tech', 'sport', 'starwars', 'school', 'travel-photography', 'video', 'wallpaper', 'warhammer', 'wholesome', 'wtf', 'darkhumor', 'funny', 'nsfw', 'girl', 'wtf', 'anime-manga', 'random', 'animals', 'animewaifu', 'awesome', 'car', 'comic-webtoon', 'cosplay', 'cyberpunk2077', 'gaming', 'gif', 'girlcelebrity', 'leagueoflegends', 'meme', 'politics', 'relationship', 'savage', 'video', 'algeria', 'argentina', 'australia', 'austria', 'bosniaherzegovina', 'bahrain', 'belgium', 'bolivia', 'brazil', 'bulgaria', 'canada', 'chile', 'colombia', 'costarica', 'croatia', 'cyprus', 'czechia', 'denmark', 'dominicanrepublic', 'ecuador', 'egypt', 'estonia', 'finland', 'france', 'georgia', 'germany', 'ghana', 'greece', 'guatemala', 'hongkong', 'hungary', 'iceland', 'india', 'indonesia', 'iraq', 'ireland', 'israel', 'italy', 'japan', 'jordan', 'kenya', 'kuwait', 'latvia', 'lebanon', 'lithuania', 'luxembourg', 'malaysia', 'mexico', 'montenegro', 'morocco', 'nepal', 'netherlands', 'newzealand', 'nigeria', 'norway', 'oman', 'pakistan', 'peru', 'philippines', 'poland', 'portugal', 'puertorico', 'qatar', 'romania', 'russia', 'saudiarabia', 'senegal', 'serbia', 'singapore', 'slovakia', 'slovenia', 'southafrica', 'southkorea', 'spain', 'srilanka', 'sweden', 'switzerland', 'taiwan', 'tanzania', 'thailand', 'tunisia', 'turkey', 'uae', 'usa', 'ukraine', 'uk', 'uruguay', 'vietnam', 'yemen', 'zimbabwe'] )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.nineGagFresh('funny')
  api.pretyPrint(res) #for prety print result
  #OR
  res = api.nineGagHot('funny')
  api.pretyPrint(res) #for prety print result
```
