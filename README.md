# UserApiDemo

A sample Flask api wich provides basic user management methods:
Create, Read, Update, Delete.

Uses MongoDB as Database

## Usage Instructions:
### Using Docker:
``` docker compose up -d ``` (I hope this works :D)

### Without Docker:
change the app.config

```
app.config['MONGODB_SETTINGS'] = {
    'db': os.environ['MONGODB_DATABASE'], <--- this
    'host': os.environ['MONGODB_HOSTNAME'], <--- this
    'port': 27017,
    'username':os.environ.get('MONGODB_USERNAME'),
    'password':os.environ.get('MONGODB_PASSWORD')
}

```
run ``` python app.py ```
