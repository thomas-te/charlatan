from prefect import flow

@flow(log_prints=True)
def my_flow():
    return "thomas just did managed exec!"
    

if __name__ == '__main__':
    my_flow()
