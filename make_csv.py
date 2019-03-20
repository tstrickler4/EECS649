from google.cloud import bigquery

print("logging in")
client = bigquery.Client()

MAX_RESULTS = 100

dataset = client.get_dataset(client.dataset('usa_names', project="bigquery-public-data"))
table = client.get_table(dataset.table(('usa_1910_2013')))
# list_rows returns an iterator over a named-tuple like object whose attributes are
# the table column names: `name`, `year`, `gender`, `state`, and `number`
# this is, however an ITERATOR that must be emptied with [i for i in rows]
rows = [i for i in client.list_rows(table)]

file = open("names.csv", "w+")
for i in rows:
    for j in range(i.number):
        file.write("%s,%s,%d,%s\n" % (i.state, i.gender, i.year, i.name))
file.close()
