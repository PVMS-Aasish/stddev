import pandas as pd
import statistics
import csv

df=pd.read_csv('Normal_distribution.csv')
height_list=df['Height(Inches)'].to_list()

height_mean=statistics.mean(height_list)
print(height_mean) 

height_median=statistics.median(height_list)
print('height_median: '+str (height_median) )

height_mode=statistics.mode(height_list)
print('height_mode'+str (height_mode))

print("mean , median and mode of height is {},{} and {} respectively".format(height_mean,height_median,height_mode))

weight_list=df['Weight(Pounds)'].to_list()

weight_mean=statistics.mean(weight_list)
print(weight_mean) 

weight_median=statistics.median(weight_list)
print('weight_median: '+str (weight_median) )

weight_mode=statistics.mode(weight_list)
print('weight_mode'+str (weight_mode))

print("mean , median and mode of weight is {},{} and {} respectively".format(weight_mean,weight_median,weight_mode))

height_std_deviation=statistics.stdev(height_list)
print(height_std_deviation)

weight_std_deviation=statistics.stdev(weight_list)
print(" weight stdev :- "+str(weight_std_deviation))

height_first_std_dev_start,height_first_std_dev_end=height_mean-height_std_deviation,height_mean+height_std_deviation
height_list_of_data_within_first_std_dev=[result for result in height_list if result>height_first_std_dev_start and result<height_first_std_dev_end]
print("{}% of data for height lies within first stddev".format(len(height_list_of_data_within_first_std_dev)*100.0/len(height_list)))

height_second_std_dev_start,height_second_std_dev_end=height_mean-(2*height_std_deviation),height_mean+(2*height_std_deviation)
height_list_of_data_within_second_std_dev=[result for result in height_list if result>height_second_std_dev_start and result<height_second_std_dev_end]
print("{}% of data for height lies within second stddev ".format(len(height_list_of_data_within_second_std_dev)*100/len(height_list)))

height_third_std_dev_start,height_third_std_dev_end=height_mean-(3*height_std_deviation),height_mean+(3*height_std_deviation)
height_list_of_data_within_third_std_dev=[result for result in height_list if result>height_third_std_dev_start and result<height_third_std_dev_end ]
print("{}% of data for height lies within third stddev ".format(len(height_list_of_data_within_third_std_dev)*100/len(height_list))) 

weight_first_std_dev_start,weight_first_std_dev_end=weight_mean-weight_std_deviation,weight_mean+weight_std_deviation
weight_list_of_data_within_first_std_dev=[result for result in weight_list if result>weight_first_std_dev_start and result<weight_first_std_dev_end]
print("{}% of data for weight lies within first stddev".format(len(weight_list_of_data_within_first_std_dev)*100.0/len(weight_list)))

weight_second_std_dev_start,weight_second_std_dev_end=weight_mean-(2*weight_std_deviation),weight_mean+(2*weight_std_deviation)
weight_list_of_data_within_second_std_dev=[result for result in weight_list if result>weight_second_std_dev_start and result<weight_second_std_dev_end]
print("{}% of data for weight lies within second stddev ".format(len(weight_list_of_data_within_second_std_dev)*100/len(weight_list)))

weight_third_std_dev_start,weight_third_std_dev_end=weight_mean-(3*weight_std_deviation),weight_mean+(3*weight_std_deviation)
weight_list_of_data_within_third_std_dev=[result for result in weight_list if result>weight_third_std_dev_start and result<weight_third_std_dev_end ]
print("{}% of data for weight lies within third stddev ".format(len(weight_list_of_data_within_third_std_dev)*100/len(weight_list))) 