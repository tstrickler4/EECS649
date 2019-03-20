from google.cloud import bigquery
import disnames

print("logging in")
client = bigquery.Client()

MAX_RESULTS = 100

dataset = client.get_dataset(client.dataset('usa_names', project="bigquery-public-data"))
table = client.get_table(dataset.table(('usa_1910_2013')))
rows = client.list_rows(table, max_results=MAX_RESULTS)

print("analyzing names")
analysis = disnames.consclusters([i.name for i in rows])
