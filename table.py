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


from google.cloud import bigquery
client=bigquery.Client()
table_id="my-project-saranya.saranya.amazon_sales"
schema=[bigquery.SchemaField('order_id','string',mode="required"),
bigquery.SchemaField('dates','date',mode="required"),
bigquery.SchemaField('status','string',mode="required"),
bigquery.SchemaField('fulfillment','string',mode="required"),
bigquery.SchemaField('sales_channel','string',mode="required"),
bigquery.SchemaField('category','string',mode="required"),
bigquery.SchemaField('ship_service_level','string',mode="required"),
bigquery.SchemaField('size','string',mode="required"),
bigquery.SchemaField('carrier_status','string',mode="required")]
table=bigquery.Table(table_id,schema=schema)
table=client.create_table(table)
print("table created successfully")

    
----to exexute the python file----
python python_amazon_status.py

-----to remove the python file----
rm python_amazon_status.py