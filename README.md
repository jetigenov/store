# QooVee Trade

### Installation
1. clone repository `git@bitbucket.org:qooveedev/trade.git`
2. create virtualenv with python3.6 `virtualenv venv` or `virtualenv -p /path/to/python3.6` if your default python version is different
3. install requirements `pip install -r requirements.txt`
4. copy .env settings `cp project/.env_sample project/.env`
5. copy local.py settings `cp project/local_sample project/local.py`

### FAQ
1. pip is configured with locations that require TLS/SSL, however the ssl module in Python is not avalable
 - **Solution**: You have to install these libs: `python3-dev`, `libffi-dev`, `libssl-dev`. After installation you have to recompile python 3.6.

2. zipimport.ZipImportError: can't decompress data; zlib not available make
 - **Solution**: Install this lib `zlib1g-dev`. After installation you have to recompile python 3.6 

By default Qoovee trade using [PostgreSQL db](https://www.digitalocean.com/community/tutorials/postgresql-ubuntu-16-04-ru)

Add db settings to `.env`

`DATABASE_URL=postgres://user:password@127.0.0.1:5432/db_name`

### Build trade main image
`docker build -f Dockerfile-image . -t qoovee/trade:image`
#### push

`docker push qoovee/trade:image`
