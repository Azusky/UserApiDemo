# UserApiDemo

A sample Flask api wich provides basic user management methods:
Create, Read, Update, Delete.

Uses MongoDB as Database

## Usage Instructions:
### Using Docker:
``` docker compose up -d ``` (I hope this works :D)

### Without Docker:
to start the service, sent environment variables and run the app

export MONGODB_DATABASE=db42
export MONGODB_HOSTNAME=localhost
python app.py

run ``` python app.py ```
