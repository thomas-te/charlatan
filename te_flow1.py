from prefect import flow

@flow
def sentiment_flow():
    return "thomas just did managed exec!"

if __name__ == '__main__':
    flow.from_source("https://github.com/thomas-te/charlatan.git", entrypoint="te_flow1.py:sentiment_flow"
                     ).deploy(name="prov-deployment", work_pool_name="managed-exec")
