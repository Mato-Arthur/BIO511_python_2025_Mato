data = dict({'pat_001': ['bacZZt98', 'bac889Ytd'], 'pat_002': ['bac0GFrr'], 'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']})

# Loop through the dict printing each key and each value as a list.
for key_patient, value_bact_list in data.items():  
  print(key_patient)
  print(value_bact_list)

# add a line to see if the value (list) has the bacterial strain 'bac889Ytd'. 
# If it does it should return 'True'. If not, it should say 'False'.

#for key_patient, value_bact_list in data.items():  
 # print(key_patient)
  #print(value_bact_list)
  #'bac889Ytd' in value_bact_list

unique_bacteria = list()  # Create an empty list to store unique bacterial strains.
for value_bact_list in data.values():  # Loop through the values (lists of bacterial strains).
  for bacterium in value_bact_list:  # Loop through each bacterial strain in the list.
    if bacterium not in unique_bacteria:  # Check if the bacterial strain is not already in the unique list.
      unique_bacteria.append(bacterium)  # If it's not, append it to the unique list.
print("Unique bacterial strains:", unique_bacteria)  # Print the list of unique bacterial strains.   

unique_bacteria_dict = dict()  # Create an empty dictionary to store unique bacterial strains as keys.
for value_bact_list in data.values():  # Loop through the values (lists of bacterial strains).
  for bacterium in value_bact_list:  # Loop through each bacterial strain in the list.
    if bacterium not in unique_bacteria_dict:  # Check if the bacterial strain is not already a key in the dictionary.
      unique_bacteria_dict[bacterium] = list()  # If it's not, add it as a key with a value of None.
      for key_patient, value_bact_list in data.items():  # Loop through the original dictionary again.
        if bacterium in value_bact_list:  # Check if the bacterial strain is in the patient's list.
          unique_bacteria_dict[bacterium].append(key_patient)  # If it is, append the patient ID to the list of patients for that bacterial strain.
print("Unique bacterial strains in dictionary:", unique_bacteria_dict)  # Print the dictionary of
#print("Unique bacterial strains in dictionary:", list(unique_bacteria_dict.keys()))  # Print the list of unique bacterial strains (keys of the dictionary).


