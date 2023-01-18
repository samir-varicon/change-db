# Changedb

Simple script to switch db

## Installation

1) Download the script inside work/varicon folder 

```bash  
cd /home/$(whoami)/work/varicon-docker/varicon
```

```bash  
wget https://raw.githubusercontent.com/samir-varicon/change-db/main/changedb.py
```
2) Add remove credentials in script 
```
database = {
        'stage':{
            'db':'stage',
            'user':'postgres',
            'password':'apple',
            'host':'db',
            'port':'5432'
            },
        'dev':{
            'db':'dev',
            'user':'postgres',
            'password':'apple',
            'host':'db',
            'port':'5432'
            },
        'parserobj':{
                'db':'parserobj',
                'user':'postgres',
                'password':'apple',
                'host': 'db',
                'port':'5432'
                }
        }
```

## Usage

```bash
python3 changedb {db_name}
```
eg:- python3 changedb dev will change your database to dev

