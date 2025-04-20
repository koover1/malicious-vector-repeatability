from datascience import *

input_data=Table.read_table("input_data.csv")

print(input_data.column(2))