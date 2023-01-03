import requests
from bs4 import BeautifulSoup

add = ""
add_list = [] #free.cccam-premium.co
port = ""
port_list = [] #15014
username = ""
username_list = [] #s0lbpj
password = ""
password_list = [] #cccam-premium.co

def listToString(string):
    char = ""
    return (char.join(string))


def main():
    url='https://cccam-premium.co/free-cccam/'
    resp=requests.get(url)
    if resp.status_code==200:
        print("Successfully opened the web page")
        soup=BeautifulSoup(resp.text,'html.parser')    
        string = soup.prettify()
        for i in range(len(string)):
            if ((string[i] == 'C' and string[i + 1] == ':') and string[i + 2] == ' '):
                i = i + 3
                while (string[i] != ' '):
                    add_list.append(string[i])
                    i = i + 1
                add = listToString(add_list)
                i = i + 1
                while (string[i] != ' '):
                    port_list.append(string[i])
                    i = i + 1
                port = listToString(port_list)
                i = i + 1
                while (string[i] != ' '):
                    username_list.append(string[i])
                    i = i + 1
                username = listToString(username_list)
                i = i + 1
                while (string[i] != ' '):
                    password_list.append(string[i])
                    i = i + 1
                password = listToString(password_list)
                i = i + 1
        print(add)
        print(port)
        print(username)
        print(password)
    else:
        print("Error")
main()
