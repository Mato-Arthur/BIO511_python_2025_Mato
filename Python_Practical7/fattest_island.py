import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

# Set default theme for all the plots
#theme_set(theme_matplotlib())
penguins = sns.load_dataset('penguins')
penguins
penguins_smooth = penguins.dropna()

Output_file = 'fattest_island.txt'

#grouped = penguins_smooth.groupby(['body_mass', 'island'])
Island_size = penguins_smooth.groupby('island')['body_mass_g'].mean()

Island_size.to_csv(Output_file, sep='\t')

#Barplot of fattest island Seaborn version
sns.barplot(x=Island_size.index, y=Island_size.values)
plt.xlabel('Island')
plt.ylabel('Average Body mass (g)')
plt.title('Average Penguin Body mass by Island')
plt.savefig('fattest_island.png')
