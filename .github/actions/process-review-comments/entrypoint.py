from github import Github
import argparse
import os
import requests
import json
from urllib.parse import urlparse


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", help="A GitHub token for the repo")
    parser.add_argument("--pr-number", help="get the PR number")

    return parser.parse_args()

def review_comment_check(comment_body):
    print(comment_body)
    res = comment_body.startswith(tuple(pref_list)) 
    
    return res

    
def review_comment_edit(id, github, body):
    url = "https://api.github.com/repos/{}/pulls/comments/{}".format(repository_name, id)
    print(url)
    headers = { 'Accept': 'application/vnd.github.v3+json',
              'Authorization': 'Bearer ' + str(github) }
    print(headers)
    payload = {'body': '⚠️  review etiquette not followed on : ' + str(body) + ' \n \n \n For more information please visit : https://github.com/HomeXLabs/reviewington/blob/main/docs/pr_etiquette.md '}
    resp = requests.patch(url=url, headers=headers, data=json.dumps(payload))
    
    print(resp)
    


def main():
    job_name = os.environ["GITHUB_WORKFLOW"]
    global repository_name 
    repository_name = os.environ["GITHUB_REPOSITORY"]
    global pref_list
    pref_list = ['Change','Question','Concern']
    # setup arguments
    args = setup_args()
    github = args.token
    global pr
    pr = args.pr_number
    print("Running in job %s on %s with sha %s" % (job_name, repository_name, args.pr_number))
    url = "https://api.github.com/repos/{}/pulls/{}/comments".format(repository_name, pr)
    
    print(url)
    headers = { 'Accept': 'application/vnd.github.v3+json' }
    
    resp = requests.get(url=url, headers=headers)
    data = resp.json()
    
    for comment in data:
        if "in_reply_to_id" not in comment:
            if not review_comment_check(comment['body']):
                review_comment_edit(comment['id'], github, comment['body'])
    # Creates an API object



if __name__ == "__main__":
    main()

