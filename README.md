
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
        <li><a href="#AlphaCoders">AlphaCoders</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>

## Instalation
coming soon...

<!-- API LIST -->
## API LIST
### AlphaCoders
**URL :** 
<https://beapi.me/alphacoders>

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
