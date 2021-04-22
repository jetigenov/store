# Book Store

### Installation
1. clone repository `git@github.com:jetigenov/store.git`
2. create virtualenv with python3.7.4 `virtualenv venv` or `virtualenv -p /path/to/python3.7.4` if your default python version is different
3. install requirements `pip install -r requirements.txt`

### FAQ
1. pip is configured with locations that require TLS/SSL, however the ssl module in Python is not avalable
 - **Solution**: You have to install these libs: `python3-dev`, `libffi-dev`, `libssl-dev`. After installation you have to recompile python 3.6.

2. zipimport.ZipImportError: can't decompress data; zlib not available make
 - **Solution**: Install this lib `zlib1g-dev`. After installation you have to recompile python 3.7.4 

By default Book Store trade using [PostgreSQL db](https://www.digitalocean.com/community/tutorials/postgresql-ubuntu-16-04-ru)

Add db settings to `.env`

`DATABASE_URL=postgres://user:password@127.0.0.1:5432/db_name`

