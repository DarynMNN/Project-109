import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
data = df['reading score'].tolist()
data_mean = statistics.mean(data)
data_median = statistics.median(data)
data_mode = statistics.mode(data)
print("Mean, Median, Mode of the data is {}, {} and {} respectively".format(data_mean, data_median, data_mode))
data_std_deviation = statistics.stdev(data)
data_first_std_deviation_start, data_first_std_deviation_end = data_mean - data_std_deviation, data_mean + data_std_deviation
data_second_std_deviation_start, data_second_std_deviation_end = data_mean - (2*data_std_deviation), data_mean + (2*data_std_deviation)
data_third_std_deviation_start, data_third_std_deviation_end = data_mean - (3*data_std_deviation), data_mean + (3*data_std_deviation)
data_of_data_within_1_std_deviation = [result for result in data if result>data_first_std_deviation_start and result<data_first_std_deviation_end]
data_of_data_within_2_std_deviation = [result for result in data if result>data_second_std_deviation_start and result<data_second_std_deviation_end]
data_of_data_within_3_std_deviation = [result for result in data if result>data_third_std_deviation_start and result<data_third_std_deviation_end]

print("{}% of data for data lies within 1 standard deviation".format(len(data_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data for data lies within 2 standard deviation".format(len(data_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data for data lies within 3 standard deviation".format(len(data_of_data_within_3_std_deviation)*100.0/len(data)))
