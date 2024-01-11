from prefect import flow, task
from prefect_cloud.work_pools.workers.modal.credentials import ModalCredentials

modal_credentials_block = ModalCredentials.load("thomas-modal-1")

@task
def my_task():
    print("thomas just used managed exec!")

    
@flow(log_prints=True)
def my_flow():
    my_task()


if __name__ == '__main__':
    my_flow()
