# This program calculates butterfly population estimates
# Inputs:   males, estimated number of male butterflies
#           females, estimated number of female butterflies
# Outputs:  total butteflies, sex ratio, variance
# Written by: C. Conner
# Modified by: Javier Hernandez Requena
# Modified Date: Feb 12, 2021

W
print("Butterfly Estimator\n")
# input/get data
males = int(input("Enter the estimated males population: "))
females = int(input("Enter the estimated females population: "))


# perform calculations
total_butterflies = males + females
sex_ratio = males // females
ratio_variance = males % females

# new functionality variables
# modified by: Javier Hernandez Requena
# date: Feb 12, 2021
gender_difference = males - females
mating_pairs = males * females


# output results
print("\nTotal Butterflies: " , total_butterflies)
print("Sex Ratio        : " , sex_ratio)
print("Variance         : " , ratio_variance)
print("Gender Differnece: " , gender_difference)
print("Mating Pairs     : " , mating_pairs)
