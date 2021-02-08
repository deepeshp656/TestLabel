from github import Github
import argparse
import os
import requests
from urllib.parse import urlparse


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", help="A GitHub token for the repo")
    parser.add_argument("--pr-number", help="get the PR number")

    return parser.parse_args()


def main():
    job_name = os.environ["GITHUB_WORKFLOW"]
    repository_name = os.environ["GITHUB_REPOSITORY"]
    # setup arguments
    args = setup_args()
    github = Github(args.token)
    pr_number = args.pr_number
    print("Running in job %s on %s with sha %s" % (job_name, repository_name, args.pr_number))
    url = "https://api.github.com/repos/deepeshp656/TestLabel/pulls/{PR_NUMBER}/comments"
    headers = { 'Accept': 'application/vnd.github.v3+json' }
    
    resp = requests.get(url=url, headers=headers)
    data = resp.json()
    print(data)

    # Creates an API object



if __name__ == "__main__":
    main()
