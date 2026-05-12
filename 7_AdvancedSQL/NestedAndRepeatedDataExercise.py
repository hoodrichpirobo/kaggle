# Write a query to find the answer
max_commits_query = """
                    SELECT committer.name AS committer_name,
                           COUNT(*) AS num_commits
                    FROM `bigquery-public-data.github_repos.sample_commits`
                    WHERE EXTRACT(YEAR FROM committer.date) = 2016
                    GROUP BY committer.name
                    ORDER BY num_commits DESC
                    """

# Check your answer
q_1.check()

# Fill in the blank
num_rows = 6 # the repeated data unnests vertically into more rows

# Check your answer
q_2.check()

# Write a query to find the answer
pop_lang_query = """
                 SELECT l.name AS language_name, COUNT(*) AS num_repos
                 FROM `bigquery-public-data.github_repos.languages`,
                      UNNEST(language) as l
                 GROUP BY l.name
                 ORDER BY num_repos DESC
                 """

# Check your answer
q_3.check()

# Your code here
all_langs_query = """
                  SELECT l.name AS name, SUM(l.bytes) AS bytes
                  FROM `bigquery-public-data.github_repos.languages`,
                      UNNEST(language) as l
                  WHERE repo_name = 'polyrabbit/polyglot'
                  GROUP BY l.name
                  ORDER BY bytes DESC
                  """

# Check your answer
q_4.check()


