from prefect import flow, task

@task
def my_task():
    phrase = "thomas just did managed exec!"
    return phrase
    
@flow(log_prints=True)
def my_flow():
    my_task()


if __name__ == '__main__':
    my_flow()
