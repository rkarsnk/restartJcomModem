import requests
import time

def isConnectJcomWebPage():
    try:
        response = requests.get('https://www.jcom.co.jp', timeout=(3.0, 7.5))
        response.raise_for_status()
        return True
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.ConnectionError:
        return False
    except requests.exceptions.RequestException:
        return False


url_login = "http://192.168.0.1/api/logincheck.cmd"
url_reboot = "http://192.168.0.1/rebootinfo.cgi"

auth = {
    "username":"admin",
    "password":"password"
}

session = requests.session()

response = session.post(url_login, auth)

if response.status_code != 200:
    session.close()
    print ("Login failure. Session closed. Status Code:", response.status_code )
    exit()
else :
    print ("Login success. Status Code:", response.status_code )

response = session.post( url_reboot )
if response.status_code == 200:
    print ("Restarting KAON KCM-3100. Status Code:", response.status_code )
    time.sleep(10)
else :
    print ("Failed to restart KAON KCM-3100. Status Code:", response.status_code )

session.close()
while False == isConnectJcomWebPage() :
    time.sleep(5)

print("Restart KAON KCM-3100: SUCCESS.")
exit()
