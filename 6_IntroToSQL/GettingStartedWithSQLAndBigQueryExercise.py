# Write the code you need here to figure out the answer
tables = list(client.list_tables(dataset))

for table in tables:
    print(table.table_id)

len(tables)

num_tables = 1  # Store the answer as num_tables and then run this cell

# Check your answer
q_1.check()

# Write the code to figure out the answer
table_ref = dataset_ref.table("crime")
table = client.get_table(table_ref)

table.schema

num_timestamp_fields = 2 # Put your answer here

# Check your answer
q_2.check()

fields_for_plotting = ["latitude", "longitude"] # Put your answers here

# Check your answer
q_3.check()

# Scratch space for your code
client.list_rows(table, selected_fields = table.schema[:], max_results = 5).to_dataframe()
