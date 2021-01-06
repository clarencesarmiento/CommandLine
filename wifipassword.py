import subprocess


def wifi_password():
    connected_wifi = []
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    for line in data:
        if 'All User Profile' in line:
            wifi = line.split(':')[1][1:-1]
            connected_wifi.append(wifi)
    for wifi in connected_wifi:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi,
                                          'key=clear']).decode('utf-8').split('\n')
        for lines in result:
            if 'Key Content' in lines:
                password = lines.split(':')[1][1:-1]
                try:
                    print(f'Name: {wifi}  \nPassword: {password}')
                except IndexError:
                    print(f'Name: {wifi}  \n[Password not stored!]')
