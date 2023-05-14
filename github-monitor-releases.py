import requests
import json
import os

def print_dict(_d):
    print(json.dumps(_d, indent=4, ensure_ascii=False))

def check_new_release_version(repo, cur_ver):
    url = repo.replace("https://github.com", "https://api.github.com/repos") + "/releases"
    params = {"accept": "application/vnd.github+json", "per_page": 1}
    r = requests.get(url, params=params)
    d = r.json()
    if (int(r.status_code / 100) != 2):
        print("[ERR]", repo, "Error", r.status_code, "with message:")
        print_dict(d)
        return
    if (len(d) == 0):
        print("[ERR]", repo, "no releases found in the reposiroty.")
        return
    new_ver = d[0]["tag_name"]
    if (new_ver != cur_ver):
        print("[NEW]", end=' ')
    else:
        print("[---]", end=' ')
    print(repo, cur_ver, "->", new_ver)

open("repos.txt", 'a').close() # Create file if not exist
print("git-monitor-releases")
print("It just checks the latest releases (tags) from the github repository page.")
print("Include repositories urlwith a version (tag name) in repos.txt. See example in repos-example.txt.")
print("Don't forget to manually change the version tag in repos.txt after downloading the update (if available).\n")
for l in open("repos.txt", 'r'):
    l = l.replace('\n', '').replace(" #", '#').split('#')[0]
    if (l == ''):
        continue
    arr = l.split(' ', 1)
    if (len(arr) < 2):
        print("[ERR]", l, ": put the tag name from release page.")
        continue
    repo, cur_ver = arr
    check_new_release_version(repo, cur_ver)

