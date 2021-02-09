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
    print(res)
    
    return res

def review_comment_reply(id):
    url = "https://api.github.com/repos/{}/pulls/{}/comments/{}/replies".format(repository_name, pr, id)
    print(url)
    headers = { 'Accept': 'application/vnd.github.v3+json',
              'Authorization': 'Bearer "{}".format(args.token)'}
    payload = {'body': 'Your review comment does not follow review etiquette'}
    resp = requests.post(url=url, headers=headers, data=json.dumps(payload))
    
    print(resp)
    


def main():
    job_name = os.environ["GITHUB_WORKFLOW"]
    global repository_name 
    repository_name = os.environ["GITHUB_REPOSITORY"]
    global pref_list
    pref_list = ['Change','Question','Concern']
    # setup arguments
    args = setup_args()
    github = Github(args.token)
    global pr
    pr = args.pr_number
    print("Running in job %s on %s with sha %s" % (job_name, repository_name, args.pr_number))
    url = "https://api.github.com/repos/{}/pulls/{}/comments".format(repository_name, pr)
    
    print(url)
    headers = { 'Accept': 'application/vnd.github.v3+json' }
    
    resp = requests.get(url=url, headers=headers)
    data = resp.json()
    #print(data)
    
    for comment in data:
        if "in_reply_to_id" not in comment:
            if not review_comment_check(comment['body']):
                print("comenting")
                review_comment_reply(comment['id'])
                print(comment['path'])
    # Creates an API object



if __name__ == "__main__":
    main()
