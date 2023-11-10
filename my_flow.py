from prefect import flow, task

@task
def my_task():
    print("thomas just used managed exec!")

    
@flow(log_prints=True)
def my_flow():
    my_task()


if __name__ == '__main__':
    my_flow()
