
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
        <li><a href="#9GAG">NineGag</a></li>
        <li><a href="#9GAG">NineGag</a></li>
        <li><a href="#9GAG">NineGag</a></li>
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
