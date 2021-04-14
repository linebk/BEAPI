
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
  <summary>List API</summary>
  <ol>
    <li><a href="#installation">Installation</a></li>
    <li>
      <a href="#API-LIST">API LIST</a>
      <ul>
        <li><a href="#ALPHACODERS">AlphaCoders</a></li>
        <li><a href="#ANIMESTREAM">AnimeStream</a></li>
        <li><a href="#ANIMEXIN">AnimeXin</a></li>
        <li><a href="#AUTHKEY2PRIMARY">Authkey2Primary</a></li>
        <li><a href="#BRAINLY">BrainlySearch</a></li>
        <li><a href="#COOKPAD">CookpadSearch</a></li>
        <li><a href="#DANBOORU">DanbooruPage</a></li>
      </ul>
    </li>
  </ol>
</details>

## Installation
coming soon...

<!-- API LIST -->
## API LIST
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
- `page` ( page of search result )

**PYTHON**
```PY
  api = BEAPI("your_apikey")
  res = api.alphaCodersSearch("naruto", 1)
  api.pretyPrint(res) #for prety print result
```


<br />
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
