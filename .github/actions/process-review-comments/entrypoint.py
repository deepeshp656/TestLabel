from github import Github
import argparse
import os
import requests
import json
from urllib.parse import urlparse


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", help="A GitHub token for the repo")
    parser.add_argument("--ref", help="get the git ref")
    

    return parser.parse_args()


def review_comment_check(comment_body):

    return comment_body.startswith(tuple(pref_list))


def fuzzy_review_comment_check(comment_body):
    first_word = comment_body.split()[0]
    match = get_close_matches(first_word, pref_list, cutoff=0.8)
    print(match)
    if not match:
        return False
    else:
        return True
    

def parse_review_comment(data):
    for comment in data:
        if "in_reply_to_id" not in comment:
            if not review_comment_check(comment["body"]):
                review_comment_edit(comment["id"], github, comment["body"])


def review_comment_edit(id, github, body):
    url = "https://api.github.com/repos/{}/pulls/comments/{}".format(
        repository_name, id
    )
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "Bearer " + str(github),
    }
    print(headers)
    payload = {
        "body": "⚠️  review etiquette not followed on : "
        + str(body)
        + " \n \n For more information please visit : https://github.com/HomeXLabs/reviewington/blob/main/docs/pr_etiquette.md "
    }
    resp = requests.patch(url=url, headers=headers, data=json.dumps(payload))

    print(resp)


def main():
    job_name = os.environ["GITHUB_WORKFLOW"]
    global repository_name
    repository_name = os.environ["GITHUB_REPOSITORY"]
    global pref_list
    pref_list = [
        "Change",
        "Question",
        "Concern",
        "Discussion",
        "Praise",
        "Suggestion",
        "Nitpick",
        "Guide",
        "⚠️ ",
    ]
    # setup arguments
    args = setup_args()
    github = os.environ["GITHUBREF"]
    global pr
    git_ref= args.ref
    print(git_ref)
    pr = 2 #git_ref.split("/")[2]
    

    url = "https://api.github.com/repos/{}/pulls/{}/comments".format(
        repository_name, pr
    )

    headers = {"Accept": "application/vnd.github.v3+json"}

    resp = requests.get(url=url, headers=headers)
    data = resp.json()
    parse_review_comment(data)


if __name__ == "__main__":
    main()
