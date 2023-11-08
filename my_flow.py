from prefect import flow

@flow
def my_flow():
    return "thomas just did managed exec!"
    

if __name__ == '__main__':
    flow.from_source("https://github.com/thomas-te/charlatan.git", entrypoint="my_flow.py:my_flow"
                     ).deploy(name="prov-deployment", work_pool_name="managed-exec")
