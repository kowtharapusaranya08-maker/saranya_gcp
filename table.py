from google.cloud import bigquery
client=bigquery.Client()
table_id="my-project-saranya.saranya.customer_order"
schema=[bigquery.SchemaField('cust_id','string',mode="required"),
bigquery.SchemaField('cust_no','string',mode="required"),
bigquery.SchemaField('cust_loc','string',mode="required"),
bigquery.SchemaField('cust_email','string',mode="required")]
table=bigquery.Table(table_id,schema=schema)
table=client.create_table(table)
print('table created successfully')