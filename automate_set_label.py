from os import environ
from github import Github

ACCESS_TOKEN               = environ.get("ACCESS_TOKEN")
TARGET_GITHUB_REPOSITORY   = environ.get("TARGET_GITHUB_REPOSITORY") 
TARGET_PULL_REQUEST_NUMBER = int(environ.get("TARGET_PULL_REQUEST_NUMBER"))

print("TARGET_GITHUB_REPOSITORY = %s" %(TARGET_GITHUB_REPOSITORY)) 
print("TARGET_PULL_REQUEST_NUMBER = %s" %(TARGET_PULL_REQUEST_NUMBER)) 

g = Github(ACCESS_TOKEN)
repo = g.get_repo(TARGET_GITHUB_REPOSITORY)
pr = repo.get_pull(TARGET_PULL_REQUEST_NUMBER)

# ラベル名
awaiting_review   = "レビュー待ち"
awaiting_rereview = "再レビュー待ち"
point_of_order    = "指摘事項あり"

labels = pr.get_labels()
label_num = labels.totalCount

# PR時のラベル名を取得
if label_num == 0:
    label_name = ""
else:
    label_name = labels[0].name

# ラベルを設定
if label_name == "":
    pr.add_to_labels(awaiting_review)
elif label_name == point_of_order:
    pr.remove_from_labels(point_of_order)
    pr.add_to_labels(awaiting_rereview)

