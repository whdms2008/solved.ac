import os
import time
import shutil

folder_path = "./boj"

all_entries = os.listdir(folder_path)
# 파일만 필터링하여 가져오기
files_only = []
for entry in all_entries:
    full_path = os.path.join(folder_path, entry)  # 전체 경로 생성
    if os.path.isfile(full_path):  # 파일인지 확인
        files_only.append(entry)


import requests

levels = {1 : "Bronze V",
          2 : "Bronze IV",
          3 : "Bronze III",
          4 : "Bronze II",
          5 : "Bronze I",
          6 : "Silver V",
          7 : "Silver IV",
          8 : "Silver III",
          9 : "Silver II",
          10 : "Silver I",
          11 : "Gold V",
          12 : "Gold IV",
          13 : "Gold III",
          14 : "Gold II",
          15 : "Gold I",
          16 : "Platinum V",
          17 : "Platinum IV",
          18 : "Platinum III",
          19 : "Platinum II",
          20 : "Platinum I"
          }


for idx, file in enumerate(files_only):
    print(f"[{idx+1} / {len(files_only)}] : {file} 처리")
    number = int(file.replace("boj", "").replace(".py", ""))
    url = f"https://solved.ac/api/v3/search/problem?query=({number})&page=1"
    resp = requests.get(url)
    for item in resp.json().get("items"):
        if item.get("problemId") == number:
            os.makedirs(f"{folder_path}/{levels.get(item.get("level"))}", exist_ok=True)
            destination_path = os.path.join("boj", file)
            move_path = os.path.join("boj", levels.get(item.get('level')))
            shutil.move(destination_path, move_path)
    time.sleep(1)

