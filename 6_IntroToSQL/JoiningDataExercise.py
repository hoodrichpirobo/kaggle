# Get a list of available tables 
list_of_tables = list(client.list_tables(dataset)) # Your code here
list_of_tables = [table.table_id for table in list_of_tables]

# Print your answer
print(list_of_tables)

# Check your answer
q_1.check()# Get a list of available tables 
list_of_tables = list(client.list_tables(dataset)) # Your code here
list_of_tables = [table.table_id for table in list_of_tables]

# Print your answer
print(list_of_tables)

# Check your answer
q_1.check()

# we'll use the column tags on posts_questions to find the specific topics

# Your code here
questions_query = """
                  SELECT id, title, owner_user_id
                  FROM `bigquery-public-data.stackoverflow.posts_questions`
                  WHERE tags LIKE '%bigquery%'
                  """

# Set up the query (cancel the query if it would use too much of 
# your quota, with the limit set to 1 GB)
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
questions_query_job = client.query(questions_query) # Your code goes here

# API request - run the query, and return a pandas DataFrame
questions_results = questions_query_job.to_dataframe() # Your code goes here

# Preview results
print(questions_results.head())

# Check your answer
q_3.check()

# Your code here
answers_query = """
                SELECT a.id, a.body, a.owner_user_id
                FROM `bigquery-public-data.stackoverflow.posts_answers` AS a
                INNER JOIN `bigquery-public-data.stackoverflow.posts_questions` AS q
                    ON q.id = a.parent_id
                WHERE q.tags LIKE '%bigquery%'
                """

# Set up the query
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=27*10**10)
answers_query_job = client.query(answers_query, job_config = safe_config) # Your code goes here

# API request - run the query, and return a pandas DataFrame
answers_results = answers_query_job.to_dataframe() # Your code goes here

# Preview results
print(answers_results.head())

# Check your answer
q_4.check()

# Your code here
bigquery_experts_query = """
                         SELECT a.owner_user_id AS user_id,
                                COUNT(1) AS number_of_answers
                         FROM `bigquery-public-data.stackoverflow.posts_answers` AS a
                         INNER JOIN `bigquery-public-data.stackoverflow.posts_questions` AS q
                             ON q.id = a.parent_id
                         WHERE q.tags LIKE '%bigquery%'
                         GROUP BY user_id
                         ORDER BY number_of_answers DESC
                         """

# Set up the query
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
bigquery_experts_query_job = client.query(bigquery_experts_query, job_config = safe_config) # Your code goes here

# API request - run the query, and return a pandas DataFrame
bigquery_experts_results = bigquery_experts_query_job.to_dataframe() # Your code goes here

# Preview results
print(bigquery_experts_results.head())

# Check your answer
q_5.check()

# You could prompt the user to select a topic among the available tags to then just replace the tags string to any other apart from bigquery


