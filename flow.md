# ORDER OF OPERATION

1. Firstly intialise the global data (app_data) and server routes
 
```
app_server = Flask(__name__,
                   template_folder = "../templates",
                   static_folder="../static",
                   static_url_path=""
               )

app_data = AppData()
session_handler = SessionHandler()
```

2. The most critical step is creating the datasource object! This must be done 
before anything else can move on.

3. Now per request, the session should hold what model it wants to use. It should
be able to change on the fly since each model should build classifiers and preferences 
vectors per session id
