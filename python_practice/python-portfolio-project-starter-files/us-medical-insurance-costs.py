# pylint: disable= pointless-string-statement
r"""°°°
# U.S. Medical Insurance Costs
°°°"""

# |%%--%%| <2Rm7O1AnYU|yxC2c98IWP>
r"""°°°
# Project Overview
For this project, you will be investigating a medical insurance costs dataset in a .csv file,  
using the Python skills that you have developed.  
This dataset and its parameters will seem familiar if you have,  
done any of the previous Python projects in the data science path

# Project Goals:
Work locally on your own computer  
Import a dataset into your program  
Analyze a dataset by building out functions or class methods  
Use libraries to assist in your analysis  
Optional: Document and organize your findings  
Optional: Make predictions about a dataset’s features based on your findings  
°°°"""
# |%%--%%| <yxC2c98IWP|SfhfwqE3OI>
r"""°°°
## Step 1. Look at the data in *insurance.csv*
°°°"""
# |%%--%%| <SfhfwqE3OI|c4Qq0VYK3F>

# Import csv library
import csv

# Read the insurance.csv file
with open("insurance.csv", newline="") as insurance_obj:
    insurance_reader = csv.DictReader(insurance_obj)
    for row in insurance_reader:
        print(row)


# |%%--%%| <c4Qq0VYK3F|MFR1uAzWtf>
r"""°°°
Data includes the age, sex, bmi, number of children, smoker status, region, and charges of patients.
Data is stored in a .csv file, using delim = ",".
°°°"""
# |%%--%%| <MFR1uAzWtf|1xE9Ys6jkY>
r"""°°°
# Step 2. Define the scope of the analysis  
Potential Questions:
* What is the average age of the patients?
* What is the average cost (charge) of the patients?
* What is the ratio between the sexes of the patients?
* How does the different variables affect the charge within the dataset?
    * Is there a difference in average charge when grouped by:
        * Sexes?
        * Smoker status?
        * Region?
        * Number of children?
        * NB. These variables are likely confounded!
    * Is there a difference in average BMI when grouped by:
        * Sexes?
        * Smoker status?
        * Number of children?
        * Region?
        * NB. These variables are likely confounded!
°°°"""
# |%%--%%| <1xE9Ys6jkY|UCw8xLwycq>
r"""°°°
# Step 3. Import the *insurance.csv* dataset
°°°"""
# |%%--%%| <UCw8xLwycq|xK8mSQj3mb>

# Import libraries
import csv

# Read in the insurance.csv file as a file object
# and store {"number": details} in insurance_dict
with open("insurance.csv", newline="") as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    # Create a dict to store the data in
    insurance_dict = {}
    key = 0
    for row in insurance_reader:
        insurance_dict.update({key: {"Age": row["age"], "Sex": row["sex"]}})
        key += 1

# |%%--%%| <xK8mSQj3mb|7724HFYqDY>

insurance_dict[1]
