import re
import sys
import subprocess

argument = sys.argv[1]
if len(sys.argv) > 2:
        print("Give only one database name")
        sys.exit()

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

def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)

with open('varicon.txt', 'r') as file:
    # Read the contents of the file
    file_data = file.read()

#creating a backup of file incase something goes wrong
with open('varicon.txt.bak','w') as backup:
        backup.write(file_data)
        print_msg_box('\n~ Created a backup file called varicon.txt.bak ~\n', indent=10)

match_db = re.search(r'SQL_DATABASE=.*', file_data)
match_user = re.search(r'SQL_USER=.*', file_data)
match_password = re.search(r'POSTGRES_PASSWORD=.*',file_data)
match_host = re.search(r'SQL_HOST=.*', file_data)
match_port = re.search(r'SQL_PORT=.*', file_data)

if match_db and match_user and match_password and match_host and match_port:
    # Replace the matched lines with the new values
    new_data = re.sub(r'SQL_DATABASE=.*', 'SQL_DATABASE='+database[argument]['db'], file_data)
    new_data = re.sub(r'SQL_USER=.*', 'SQL_USER='+database[argument]['user'], new_data)
    new_data = re.sub(r'POSTGRES_PASSWORD.*', 'POSTGRES_PASSWORD='+database[argument]['password'], new_data)
    new_data = re.sub(r'SQL_HOST=.*', 'SQL_HOST='+database[argument]['host'], new_data)
    new_port = re.sub(r'SQL_PORT=.*', 'SQL_PORT='+database[argument]['port'], new_data)
    # Open the file for writing
    with open('varicon.txt', 'w') as file:
        # Write the new data to the file
        file.write(new_data)
        print_msg_box('\n~ Changed Config File ~\n', indent=10)


    print_msg_box(f'\n~ Making docker container down ~\n', indent=10)
    down = subprocess.run(['docker', 'compose','-f','docker-compose.yaml','down'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if down.stdout:
        print_msg_box(f'\n~ {down.stdout.decode()} ~\n',indent=10)
    elif down.stdout:
            print(down.stdout.decode())
     
    print_msg_box('\n~ Container Down ~\n',indent=10)
    up = subprocess.run(['docker', 'compose','-f','docker-compose.yaml','up','-d'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if up.stdout:
        print(up.stdout.decode())
    elif up.stderr:
        print(up.stderr.decode())
    print_msg_box('\n~ DONE ~\n',indent=10)

else:
        print_msg_box(f'\n~ No match Found ~\n', indent=10)
 
