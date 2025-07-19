#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# WARNING: UNAUTHORIZED ACCESS IS ILLEGAL. FOR EDUCATIONAL PURPOSES ONLY.
import random
import time
import sys
from datetime import datetime

class FacebookPhish:
    def __init__(self):
        self.years = [2009, 2011, 2013]
        self.base_url = "https://www.facebook.com"
        self.passwords = ["123456", "123456789", "password123"]
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14"
        ]
    
    def banner(self):
        print(f"""
\033[1;31m
▓█████▄  ▒█████   ███▄ ▄███▓ ██▓███   ██▀███   ▒█████   ███▄    █ 
▒██▀ ██▌▒██▒  ██▒▓██▒▀█▀ ██▒▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ 
░██   █▌▒██░  ██▒▓██    ▓██░▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒
░▓█▄   ▌▒██   ██░▒██    ▒██ ▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒
░▒████▓ ░ ████▓▒░▒██▒   ░██▒▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░ ▒  ▒   ░ ▒ ▒░ ░  ░      ░░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░ ░  ░ ░ ░ ░ ▒  ░      ░   ░░         ░░   ░ ░ ░ ░ ▒     ░   ░ ░ 
   ░        ░ ░         ░               ░         ░ ░           ░ 
 ░                                                               v3.37\033[0m
 [*] Legacy Facebook Account Scanner (2009-2013) 
 [*] Termux-Compatible | No Logging | Instant Output
        """)

    def menu(self):
        print("\n\033[1;32m[MAIN MENU]\033[0m")
        print("1. Start Account Harvesting")
        print("2. Configure Parameters")
        print("3. Exit")
        return input("\n\033[1;37m[?] Select Option: \033[0m")

    def config(self):
        print("\n\033[1;33m[CONFIGURATION]\033[0m")
        self.count = int(input("[?] Accounts to harvest (10000-50000): "))
        while not 10000 <= self.count <= 50000:
            print("\033[1;31m[!] Must be between 10000-50000\033[0m")
            self.count = int(input("[?] Accounts to harvest: "))

        print("\n[+] Targeting years:", ', '.join(map(str, self.years)))
        print("[+] Using base URL:", self.base_url)

    def generate_id(self):
        return ''.join(str(random.randint(0, 9)) for _ in range(15))

    def harvest(self):
        print(f"\n\033[1;35m[+] Harvesting {self.count} accounts...\033[0m")
        time.sleep(2)
        
        for i in range(1, self.count + 1):
            uid = self.generate_id()
            passwd = random.choice(self.passwords)
            creation = random.choice(self.years)
            last_login = f"{random.randint(1,28)}/{random.randint(1,12)}/{creation + random.randint(1,5)}"
            
            sys.stdout.write(
                f"\r\033[1;36m[ID: {uid}] \033[1;33m| \033[1;32mPASS: {passwd} \033[1;33m| "
                f"\033[1;35mCREATED: {creation} \033[1;33m| \033[1;34mLAST LOGIN: {last_login}\033[0m"
            )
            sys.stdout.flush()
            
            time.sleep(0.01)  # Simulate network delay
            
            if i % 100 == 0:
                print(f"\n\033[1;32m[+] {i} accounts found...\033[0m")

    def run(self):
        self.banner()
        while True:
            choice = self.menu()
            if choice == '1':
                if not hasattr(self, 'count'):
                    print("\033[1;31m[!] Configure parameters first!\033[0m")
                    continue
                self.harvest()
                print("\n\n\033[1;32m[+] Operation completed. No data was saved.\033[0m")
            elif choice == '2':
                self.config()
            elif choice == '3':
                print("\n\033[1;31m[!] Session terminated\033[0m")
                break
            else:
                print("\033[1;31m[!] Invalid option\033[0m")

if __name__ == "__main__":
    try:
        tool = FacebookPhish()
        tool.run()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Forced exit detected. Wiping session data...\033[0m")
        sys.exit(0)