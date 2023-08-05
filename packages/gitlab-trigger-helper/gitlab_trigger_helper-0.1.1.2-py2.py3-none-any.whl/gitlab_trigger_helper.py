"""GitLab trigger module.
This module helps docker bypassing "multi-project pipelines"
capability which is covered on on gitLab silver or higher.
"""
import sys
import time
import argparse
from typing import List
from blessings import Terminal
import gitlab


def git_lab_login(git_lab_host, api_gilab_token):
    """

    :param git_lab_host:
    :param api_gilab_token:
    :return:
    """
    git_trigger = gitlab.Gitlab(git_lab_host, private_token=api_gilab_token)

    return git_trigger


def convert_args(args: List[str]):
    """

    :param args:
    :return: Args trasformed by the user
    """
    parser = argparse.ArgumentParser(
        description='Gilab trigger helper',
        add_help=False)
    parser.add_argument('-a', '--api-token', required=True,
                        help='personal access token (not required when running detached)',
                        dest='gitlab_api_token')
    parser.add_argument('-h', '--host', default='gitlab.com', dest="git_lab_host")
    parser.add_argument('--help', action='help', help='show this help message and exit')
    parser.add_argument('-t', '--target-ref', default='master',
                        help='target ref (branch, tag, commit)', dest='target_branch')
    parser.add_argument('-p', '--project-id', required=True,
                        help='repository id found on settings', dest='project_id')
    parsed_args = parser.parse_args(args)

    return parsed_args


def trigger(args: List[str]):
    """

    :project_id variable aims gitlab id found on project >> General:
    """

    term = Terminal()

    # Require parameters
    args = convert_args(args)
    assert args.gitlab_api_token, 'token should be set'
    assert args.project_id, 'project id must be set'

    #  Moving args to local variables
    git_lab_host = args.git_lab_host
    project_id = args.project_id
    api_gilab_token = args.gitlab_api_token
    target_branch = args.target_branch

    git_trigger = git_lab_login(git_lab_host, api_gilab_token)

    project = git_trigger.projects.get(project_id)
    create_pipeline = project.pipelines.create({'ref': target_branch})

    pipeline = project.pipelines.get(create_pipeline.id)
    pipe_jobs = pipeline.jobs.list()
    pipeline_jobs_count = len(pipe_jobs)
    pipeline_jobs_count = str(pipeline_jobs_count)
    print(term.bold_cyan("Triggered pipeline holds " + pipeline_jobs_count + " jobs"))
    timeout = time.time() + 60 * 30

    while pipeline.finished_at is None:

        pipeline.refresh()

        if pipeline.status == "pending":
            print(term.bright_yellow(project.name + " is " + pipeline.status))
        elif pipeline.status == "running":
            print(term.bold_blue(project.name + " is " + pipeline.status))
        if pipeline.status == "success":
            print(term.bright_green(project.name + " is " + pipeline.status))
        elif pipeline.status == "failed":
            print(term.bold_red(project.name + " is " + pipeline.status))
            raise Exception
        elif pipeline.status == "canceled":
            print(term.bold_red(project.name + " is " + pipeline.status))
            raise Exception
        elif time.time() > timeout:
            print(term.bright_red(project.name + " is " + pipeline.status))
            raise Exception

        time.sleep(10)


def main():
    trigger(sys.argv[1:])
    sys.exit(0)


if __name__ == "__main__":
    main()
