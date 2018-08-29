from datetime import datetime, timedelta
import pandas as pd


def read_file_to_df(filename):
    return pd.read_csv(filename, names=["date", "time", "id", "bikes", "locks"])


datetimes = {}


def date_and_time_fields_to_datetime_object(date, time):
    key = (date, time)
    if key not in datetimes:
        year, month, day = [int(i) for i in date.split("-")]
        hour, minute = [int(i) for i in time.split(":")]
        datetimes[key] = datetime(year, month, day, hour, minute)
    return datetimes[key]


def make_datetime(row):
    date, time = row[0], row[1]
    datetime_object = date_and_time_fields_to_datetime_object(date, time)
    # add two hours to each item, since API gives incorrect time
    return datetime_object + timedelta(hours=2)


def inplace_add_dates_to_df(df):
    df.loc[:, "datetime"] = df.apply(make_datetime, axis=1)  # axis = 1: row-wise


def merge_df_with_station_df(df, station_names_df):
    return df.merge(station_names_df, on="id", how="right")


def change_column_types_to_int(df):
    df = df.dropna()
    for column in ("bikes", "locks"):
        df.loc[:, column] = df.loc[:, column].astype(int)
    return df


def sorted_df(df):
    return df.sort_values(axis=0, by=["datetime", "name"])


def make_pivoted_table(df):
    full_table = pd.pivot_table(df, index="datetime", columns="name", values="bikes")
    full_table = full_table.fillna(value=-1)
    for column in full_table.columns:
        full_table.loc[:, column] = full_table.loc[:, column].astype("int32")
    return full_table


def read_server_file_and_write_processed_data_to_file(
    server_filename, stations_filename, table_filename
):
    df = read_file_to_df(server_filename)
    inplace_add_dates_to_df(df)
    station_names_df = pd.read_csv(stations_filename, names=["id", "name"])
    df = merge_df_with_station_df(df, station_names_df)
    df = change_column_types_to_int(df)
    df = sorted_df(df)
    full_table = make_pivoted_table(df)
    print(full_table.shape)
    full_table.to_csv(table_filename)


if __name__ == "__main__":
    server_filename = "new_data_25_july.txt"
    stations_filename = "stations/stations.txt"
    table_filename = "full_table2.txt"
    read_server_file_and_write_processed_data_to_file(
        server_filename, stations_filename, table_filename
    )
