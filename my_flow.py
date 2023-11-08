from prefect import flow

@task
def my_task():
    return "thomas just did managed exec!"
    
@flow(log_prints=True)
def my_flow():
    my_task()
    
    

if __name__ == '__main__':
    my_flow()
