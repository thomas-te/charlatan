import httpx
from prefect import flow, task
from datetime import timedelta
from prefect.tasks import task_input_hash
from prefect.artifacts import create_markdown_artifact


# Get news data
@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=0.1))
def get_news():
    print("news")

    markdown_content = f""" # News """
    create_markdown_artifact(
        key="sentiment-report",
        markdown=markdown_content,
        description="New Summary",
    )
    return "news"


# Compute sentiment and store scores
@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=0.3))
def calculate_sentiment_scores(news):
    print("sentiment_scores")

    markdown_content = f""" # Sentiment Scores """
    create_markdown_artifact(
        key="sentiment-report",
        markdown=markdown_content,
        description="Sentiment Scores",
    )
    return "sentiment_scores"


# Aggregate sentiment scores
@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=0.2))
def aggregate_sentiment(sentiment_scores):
    print("aggregate sentiment")

    markdown_content = f""" # Aggregated Sentiment """
    create_markdown_artifact(
        key="sentiment-report",
        markdown=markdown_content,
        description="Aggregated Sentiment",
    )
    return "aggregate sentiment"


# Send sentiment and trade signal
@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=0.4))
def send_recommendation(aggregated_sentiment):
    print("send recommendation")

    markdown_content = f""" # Recommendation """
    create_markdown_artifact(
        key="sentiment-report",
        markdown=markdown_content,
        description="Recommendation",
    )
    return "send recommendation"


# Put all the tasks together into a flow
@flow(log_prints=True)
def sentiment_flow():
    news = get_news()
    sentiment_scores = calculate_sentiment_scores(news=news)
    aggregated_sentiment = aggregate_sentiment(sentiment_scores=sentiment_scores)
    sent_sentiment = send_recommendation(aggregated_sentiment=aggregated_sentiment)

    print(news, sentiment_scores, aggregated_sentiment, sent_sentiment)

