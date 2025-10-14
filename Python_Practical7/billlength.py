import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns 
# Set default theme for all the plots
#theme_set(theme_matplotlib())
penguins = sns.load_dataset('penguins')
penguins
penguins_smooth = penguins.dropna()

#Histogram Seaborn version
sns.histplot(data=penguins_smooth, x='bill_length_mm', hue='species', kde=True)
plt.xlabel('Bill length (mm)')
plt.ylabel('Count')
plt.title('Penguin bill length distribution by species')
plt.savefig('penguin_bill_length_distribution_by_species.png')
