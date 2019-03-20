from google.cloud import bigquery
import disnames

print("logging in")
client = bigquery.Client()

MAX_RESULTS = 100

dataset = client.get_dataset(client.dataset('usa_names', project="bigquery-public-data"))
table = client.get_table(dataset.table(('usa_1910_2013')))
# list_rows returns an iterator over a named-tuple like object whose attributes are
# the table column names: `name`, `year`, `gender`, `state`, and `number`
# this is, however an ITERATOR that must be emptied with [i for i in rows]
rows = client.list_rows(table, max_results=MAX_RESULTS)

if __name__ == "__main__":
    print("analyzing names")
    analysis = disnames.consclusters([i.name for i in rows])
    disnames.print_dict(analysis)
