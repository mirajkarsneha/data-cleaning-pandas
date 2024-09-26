#  🦈 Quest2- Shark Attacks

### 📒 Description
Welcome to the Data Wrangling Quest! Your mission: to clean a messy data set known as “Shark Attacks” through using data wrangling techniques. By doing so you will be able to prepare the data set for analysis for a use case of your choice. 

### 🧠 Project Narrative
To download the Incident Log raw data file as an Excel File check this link - https://www.sharkattackfile.net/incidentlog.htm

All individuals survived unless noted otherwise. Entries on the spreadsheet are color-coded.
- Unprovoked Incidents = Tan
- Provoked Incidents = Orange
- Incidents Involving Watercrafts = Green
- Air / Sea Disasters = Yellow
- Questionable Incidents = Blue

- Unprovoked vs. Provoked - GSAF defines a provoked incident as one in which the shark was speared, hooked, captured or in which a human drew "first blood". Although such incidents are of little interest to shark behaviorists, when the species of shark involved is known and pre-op photos of the wounds are available, the bite patterns are of value in determining species of shark involved in other cases when the species could not identified by the patient or witnesses. We know that a live human is rarely perceived as prey by a shark. Many incidents are motivated by curiosity, others may result when a shark perceives a human as a threat or competitor for a food source, and could be classed as "provoked" when examined from the shark's perspective.

- Incidents involving watercraft – Incidents in which a boat was bitten or rammed by a shark are in green. However, in cases in which the shark was hooked, netted or gaffed, the entry is orange because they are classed as provoked incidents.

- Questionable incidents - Incidents in which there are insufficient data to determine if the injury was caused by a shark or the person drowned and the body was later scavenged by sharks. In a few cases, despite media reports to the contrary, evidence indicated there was no shark involvement whatsoever. Such incidents are in blue.

### 🧹 Data Cleaning
### 📝 Description of each column how it is cleaned
- Date Column - Removed the word "Reported" from the string and kept the date as it is.
- Year Column - Replaced two numbers which has '&' and replaced it with average of two numbers
- Type Column - Replaced 'Unverified', 'Questionable', 'Under investigation' with 'Unconfirmed'; record based on string content (fatal vs non-fatal)
- Activity Column - Replace special characters with empty values, dropped nans
- Name Column - Kept name as it is just replaced female|nan|NaN with empty value.
- Sex Column - Kept F and M values and replaced other with empty value.
- Age Column- Replaced two numbers which has 'and|or|to|&|' and replaced it with average of two numbers. Converted decimal values to integer. Removed ½ and rounded up the numbers (Eg. 6½ converted to 6.5 and rounded up). 
- Injury Column - Renamed to fatal if fatal is in string and non Fatal if "Fatal" not in string
- Species Column - Removed empty space from the label.
- Time Column - Format timestamp

### 🏗️ Project Structure
This is a python project which a has below mentioned files.
- main.ipnyb - Main file is the main file which calls the functions defined in functions.py file and returns the clean data file in csv format.
- functions.py - This file contains all the definations(functions) and the loagic defined.
- README.md - Describes what the project is, how it is structured and what changes are applied to get a clean data file.
- sharkattacks_cleaned_data.csv - How the clean data file looks

### 💭 Hypothesis
- Hypothes 1 -Sharks are more likely to attack when provoked than they are unprovoked.
- Hypothesis 2 - The frequency of shark attacks is higher during the early morning and late afternoon compared to midday.
- Hypothesis 3 - Surfing results in a higher number of shark attacks compared to other water-based activities

### 📊 Presentaion
Link - https://docs.google.com/presentation/d/1ffOLEdsFhuFjwfYm-IKGeflxyXxzx5IARtpaP6XQiTk/edit#slide=id.g3057677211f_0_60
