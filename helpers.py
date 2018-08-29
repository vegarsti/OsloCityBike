from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt
import calendar

def get_station(data_frame, station_name):
    return data_frame[[station_name]]


def get_date(data_frame, year, month, day):
    start_date = date(year, month, day)
    end_date = start_date + timedelta(days=1)
    return data_frame.loc[start_date:end_date]


def is_peak(series):
    N = 3
    peak_comparison_df = pd.concat(
        [series.shift(periods=i) for i in range(-N, N + 1)], axis=1
    )
    peak_comparison_df.columns = (
        [str(i) for i in range(-N, -1)]
        + ["next", "current"]
        + [str(i) for i in range(1, N + 1)]
    )
    peak_comparison_df = peak_comparison_df.fillna(0)
    return (peak_comparison_df.loc[:, "current"] == peak_comparison_df.max(axis=1)) & (
        peak_comparison_df["current"] != peak_comparison_df["next"]
    )


def find_peaks_given_df_with_differences(series):
    peak_df = pd.DataFrame({"bikes": series})
    peak_df.loc[:, "peak"] = is_peak(peak_df.loc[:, "bikes"])
    peak_df.loc[:, "peak"] = peak_df.fillna(False)
    return peak_df


def plot_station_day_with_peaks(station_name, year, month, day, threshold=10):
    station_df = get_station(full_table, station_name)
    subset_df = get_date(station_df, year, month, day)
    subset_series = subset_df[station_name]
    peak_df = find_peaks_given_df_with_differences(subset_series)
    peak_df.loc[:, "peak"] = peak_df.loc[:, "peak"]
    peak_df.loc[:, "peak"] = (peak_df.loc[:, "peak"]) & (
        peak_df.loc[:, "bikes"] >= threshold
    )  # ignore local peaks
    plt.plot(peak_df["bikes"])
    plt.plot(peak_df[peak_df["peak"]]["bikes"], "r.")
    fix_dates()
    plt.title(
        "Number of bikes at {} on {} {}".format(
            station_name, calendar.month_name[month], day
        )
    )
    plt.xlabel("Datetime")
    plt.ylabel("Number of bikes")


def get_window_around_datetime(
    data_frame, year, month, day, hour, minute, timedelta_window
):
    """window must be timedelta"""
    mid_datetime = datetime(year, month, day, hour, minute)
    start_datetime = mid_datetime - timedelta_window
    end_datetime = mid_datetime + timedelta_window
    return data_frame.loc[start_datetime:end_datetime]


station_name = 'Georg Morgenstiernes hus'
year = 2018
month = 5
day = 10
plot_station_day_with_peaks(station_name, year, month, day)