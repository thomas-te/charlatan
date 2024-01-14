from prefect import flow, task
from prefect.artifacts import create_markdown_artifact

@task
def my_task():
    word = 'hey good job'
    create_markdown_artifact(key='report', markdown=word, description='resulting content')
    

@flow(log_prints=True)
def my_flow():
    my_task()


if __name__ == '__main__':
    my_flow()
