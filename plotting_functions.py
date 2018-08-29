import matplotlib.pyplot as plt
from helpers import get_date, get_station

def fix_dates():
    plt.gcf().autofmt_xdate()

def plot_station_date(data_frame, station_name, year, month, day):
    plt.plot(get_date(get_station(data_frame, station_name), year, month, day))
    fix_dates()
    plt.show()