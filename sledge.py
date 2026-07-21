import requests
import os
from bs4 import BeautifulSoup
import json

print("            __                  __                     ")
print("          |  \\                |  \\                    ")
print("  _______ | $$  ______    ____| $$  ______    ______  ")
print(" /       \\| $$ /      \\  /      $$ /      \\  /      \\ ")
print("|  $$$$$$$| $$|  $$$$$$\\|  $$$$$$$|  $$$$$$\\|  $$$$$$\\")
print(" \\$$    \\ | $$| $$    $$| $$  | $$| $$  | $$| $$    $$")
print(" _\\$$$$$$\\| $$| $$$$$$$$| $$__| $$| $$__| $$| $$$$$$$$")
print("|       $$| $$ \\$$     \\ \\$$    $$ \\$$    $$ \\$$     \\")
print(" \\$$$$$$$  \\$$  \\$$$$$$$  \\$$$$$$$ _\\$$$$$$$  \\$$$$$$$")
print("                                  |  \\__| $$          ")
print("                                   \\$$    $$          ")
print("                                    \\$$$$$$           ")
print("=-=-=-=-=-=SLEDGE---v2.0=-=-=-=-=-=")
print("Made by Ergi - ergi0411 on Discord")
print(" ")
print("1.Website Status Scanner - Send Requests To A WebSite To Check The Status")
print(" ")
print("2.WebScraper - Download The Links From The WebSite They Get Saved In data.json")
print(" ")
print("3.Path Finder - Enter A Url And It Finds Hidden Paths You Can Add What Paths To Look For In The paths.json Files (e.x /admin or /backup.zip)")
print(" ")
choice = int(input("1, 2 or 3 > "))
if choice == 1:
    while True:
        url = input("Enter Url # ")
        times = int(input("Enter How Many Requests To Send (max 10) # "))
        if times > 10:
            print("Max 10!")
            print("This tool is only for testing")
            break
        for i in range(times):
            r = requests.get(url)
            if r.status_code == 200:
                print("[✔]status code: 200")
            elif r.status_code == 400:
                print("[*] status code: 400")
            else:
                print("[-] Failed To Send")
        break

elif choice == 2:
    if os.path.exists("data.json"):
        os.remove("data.json")

    url = input("Enter Url > ")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    urls_list = []
    links = soup.find_all('a')
    for link in links:
        urls_list.append(link.get('href'))
    data = urls_list

    with open("data.json", "w") as file:
        json.dump(data, file)
        print("Saved links to data.json")

elif choice == 3:
    url = input("Enter The Url You Want To Search > ")
    if not url.startswith(("http://","https://")):
        url = "https://" + url
    
    with open("C:\\Users\\ergis\\Desktop\\sledge\\paths.json", "r") as file:
        print("Current folder:", os.getcwd())
        paths = json.load(file)
        
        for path in paths:
            try:
                r = requests.get(url + path)
                print(f"{path} -> {r.status_code}")
                
                if r.status_code == 200:
                    print(f"[✔] Found: {url + path}")
                else:
                    print(f"[-] {path} not available")
                    
            except requests.exceptions.RequestException:
                print(f"[-] {path} -> Connection error")