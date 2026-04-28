# Query to select prolific commenters and post counts
prolific_commenters_query = """
                            SELECT `by` AS author, COUNT(1) AS NumPosts
                            FROM `bigquery-public-data.hacker_news.full`
                            GROUP BY `by`
                            HAVING COUNT(1) > 10000
                            """ # Your code goes here

# Set up the query (cancel the query if it would use too much of 
# your quota, with the limit set to 1 GB)
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
query_job = client.query(prolific_commenters_query, job_config=safe_config)

# API request - run the query, and return a pandas DataFrame
prolific_commenters = query_job.to_dataframe()

# View top few rows of results
print(prolific_commenters.head())

# Check your answer
q_1.check()

# Write your query here and figure out the answer
deleted_query = """
                SELECT COUNT(1) AS DeletedAmount
                FROM `bigquery-public-data.hacker_news.full`
                WHERE deleted = True
                """

query_job = client.query(deleted_query, job_config = safe_config)

deleted_amount = query_job.to_dataframe()

print(deleted_amount.head())


