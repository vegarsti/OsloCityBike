from make_pivot_table import read_server_file_and_write_processed_data_to_file
import pandas as pd
import time

server_filename = "new_data_25_july.txt"
stations_filename = "stations/stations.txt"
table_filename = "full_table2.txt"

t = time.time()
read_server_file_and_write_processed_data_to_file(
    server_filename, stations_filename, table_filename
)
duration = time.time() - t
print(
    "Processed in {} minutes and {} seconds.".format(duration // 60, int(duration % 60))
)
"""
full_table = pd.read_csv(
    table_filename, index_col="datetime", date_parser=pd.to_datetime
)
"""
