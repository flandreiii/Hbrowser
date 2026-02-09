#!/usr/bin/env python3
# hbrowser - by flandreiii (educational cyber-security search tool)

import requests
import time
import os

# =============== ANIMATIE INTRO =====================

def animate(text, delay=0.05):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

def intro():
    os.system("clear")
    animate("Loading hbrowser...", 0.04)
    animate("Made by flandreiii", 0.06)
    animate("==========================", 0.02)

# ================= SEARCH FUNCTIONS ==================

def search_duckduckgo(query):
    url = "https://duckduckgo.com/html"
    params = {"q": query}

    r = requests.get(url, params=params, headers={"User-Agent": "hbrowser"})
    if r.status_code != 200:
        return ["Error accessing DuckDuckGo"]

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    results = []

    for a in soup.select(".result__a"):
        results.append(a.get_text())

    return results[:10]

def search_hackernews(query):
    url = f"https://hn.algolia.com/api/v1/search?query={query}"
    r = requests.get(url)

    if r.status_code != 200:
        return ["Error accessing HackerNews"]

    data = r.json()
    return [hit["title"] for hit in data["hits"][:10]]

# ================= MAIN PROGRAM ======================

def main():
    intro()

    while True:
        query = input("\n[hbrowser] Search: ")

        if query.lower() in ["exit", "quit"]:
            animate("Exiting hbrowser...")
            break

        animate("\nSearching...", 0.02)

        print("\n--- DuckDuckGo Results ---")
        for r in search_duckduckgo(query):
            print("•", r)

        print("\n--- HackerNews Results ---")
        for r in search_hackernews(query):
            print("•", r)

        print("\n====================================")

if __name__ == "__main__":
    main()
