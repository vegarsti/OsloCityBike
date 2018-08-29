from make_pivot_table import read_server_file_and_write_processed_data_to_file
import pandas as pd
import time

server_filename = "serverdata.txt"
stations_filename = "stations/stations.txt"
table_filename = "full_table.txt"
t = time.time()
read_server_file_and_write_processed_data_to_file(
    server_filename, stations_filename, table_filename
)
full_table = pd.read_csv(
    table_filename, index_col="datetime", date_parser=pd.to_datetime
)
print((time.time() - t))
