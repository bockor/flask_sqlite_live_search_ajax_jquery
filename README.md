## Python Flask Live Data Search using Jquery Ajax and Sqlite Database

```sh
bockor@home flask_sqlite_live_search_ajax_jquery % . .venv/bin/activate     
(.venv) bockor@home flask_sqlite_live_search_ajax_jquery % flask run                
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### logging

```sh
127.0.0.1 - - [20/Nov/2026 16:29:34] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [20/Nov/2026 16:29:34] "GET /favicon.ico HTTP/1.1" 404 -
search_word: p
127.0.0.1 - - [20/Nov/2026 16:29:39] "POST /ajaxlivesearch HTTP/1.1" 200 -
search_word: po
127.0.0.1 - - [20/Nov/2026 16:29:39] "POST /ajaxlivesearch HTTP/1.1" 200 -
search_word: pop
```