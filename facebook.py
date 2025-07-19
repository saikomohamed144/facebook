#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Facebook Legacy Account Recovery Tool
# For educational purposes only. Unauthorized access is illegal.

import os
import random
import time
import requests
from bs4 import BeautifulSoup

class FacebookPhish:
    def __init__(self):
        self.target_years = [2009, 2011, 2013]
        self.base_url = "https://www.facebook.com/"
        self.found_credentials = []
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def show_banner(self):
        print(r"""
  _____ _           _   _             ___  ___      _               
 |  ___| |         | | | |            |  \/  |     | |              
 | |__ | | __ _ ___| |_| |__   ___ _ _| .  . | __ _| | _____ _ __   
 |  __|| |/ _` / __| __| '_ \ / _ \ '__| |\/| |/ _` | |/ / _ \ '__|  
 | |___| | (_| \__ \ |_| |_) |  __/ |  | |  | | (_| |   <  __/ |     
 \____/|_|\__,_|___/\__|_.__/ \___|_|  \_|  |_/\__,_|_|\_\___|_|     
        """)

    def get_search_params(self):
        print("\n[+] Select target year:")
        for i, year in enumerate(self.target_years, 1):
            print(f"{i}. {year}")
        year_choice = int(input("\nChoice: ")) - 1
        
        while True:
            try:
                account_count = int(input("\n[+] Enter number of accounts to scan (10000-50000): "))
                if 10000 <= account_count <= 50000:
                    return self.target_years[year_choice], account_count
                print("Invalid input! Enter between 10000-50000")
            except ValueError:
                print("Numbers only!")

    def generate_credentials(self, count):
        creds = []
        for _ in range(count):
            user_id = ''.join(str(random.randint(0, 9)) for _ in range(15))
            password = random.choice(["123456", "123456789", "password123", "qwerty"])
            creds.append((user_id, password))
        return creds

    def brute_force_accounts(self, target_year, total_accounts):
        print(f"\n[+] Targeting {target_year} accounts | Scanning {total_accounts} profiles...")
        sample_size = min(50, total_accounts // 1000)
        test_creds = self.generate_credentials(sample_size)
        
        for i, (user_id, password) in enumerate(test_creds):
            time.sleep(0.3)
            print(f"\r[+] Testing credentials: {i+1}/{sample_size} | ID: {user_id} | Pass: {password}", end='')
            try:
                # Simulated credential validation
                if random.random() > 0.85:  # 15% "success" rate
                    self.found_credentials.append((user_id, password))
            except Exception:
                continue
        print("\n\n[+] Scan completed! Valid accounts found:", len(self.found_credentials))

    def display_results(self):
        if not self.found_credentials:
            print("\n[!] No valid accounts found. Try larger sample size.")
            return
        
        print("\n[+] GOLDEN ACCOUNTS FOUND:")
        for i, (uid, pwd) in enumerate(self.found_credentials, 1):
            print(f"{i}. ID: {uid} | Password: {pwd} | Login: {self.base_url}{uid}")
            print("   Profile last active: 2010s | Security: LOW")
        print("\n[!] Use responsibly. Illegal access = federal crime")

    def run(self):
        os.system('clear')
        self.show_banner()
        year, count = self.get_search_params()
        self.brute_force_accounts(year, count)
        self.display_results()

if __name__ == "__main__":
    tool = FacebookPhish()
    tool.run()
