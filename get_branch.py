import requests
import os

print(os.environ)
git_auth = os.environ['GITHUB_AUTH']
base = os.environ['CI_PULL_REQUEST']
split_base = base.split("/")
url = "https://api.github.com/repos/" + split_base[3] + "/" + split_base[4] + "/pulls/" + split_base[6]
print(url)


payload = {}
headers = {
  'Authorization': git_auth
}

response = requests.request("GET", url, headers=headers, data=payload)
commit_msg = response.json()

print(commit_msg)
head = commit_msg["head"]["ref"]
base = commit_msg["base"]["ref"]
print(f"head is {head}, base is {base}")

if base == "test":
    if head == "main":
        print(f"Success. Test pulled from correct branch {head}")
    else:
        raise Exception(f"Pulled from wrong branch. Should be branch main, not branch {head}")
elif base == "prod":
    if head == "test":
        print(f"Success. Prod pulled from correct branch {head}")
    else:
        raise Exception(f"Pulled from wrong branch. Should be branch test, not branch {head}")
