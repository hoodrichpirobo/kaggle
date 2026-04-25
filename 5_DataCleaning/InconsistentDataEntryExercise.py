# TODO: Your code here

# professors["Graduated from"] = professors["Graduated from"].str.lower()
# professors["Graduated from"] = professors["Graduated from"].str.strip()
colleges = professors["Graduated from"].unique()
colleges.sort()
colleges

# TODO: Your code here
professors["Graduated from"] = professors["Graduated from"].str.strip()

# Check your answer
q2.check()

# TODO: Your code here!
matches = fuzzywuzzy.process.extract("usa", countries, limit = 10, scorer = fuzzywuzzy.fuzz.token_sort_ratio)
matches

replace_matches_in_column(df = professors, column = "Country", string_to_match = "usa", min_ratio = 74)

# Check your answer
q3.check()


