import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns # For saving ggplot-style plots
import numpy as np
import pandas as pd
from plotnine import (
    ggplot,
    aes,
    geom_point,
    theme_matplotlib,
    theme_set,
)

# Set default theme for all the plots
theme_set(theme_matplotlib())
penguins = sns.load_dataset('penguins')
penguins
penguins_smooth = penguins.dropna()

#Seaborn version
sns.scatterplot(data=penguins_smooth, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.xlabel('Flipper length (mm)')
plt.ylabel('Body mass (g)')
plt.title('Penguin flipper length vs body mass by species')
plt.savefig('penguin_flipper_vs_mass_by_species.png')

#Matplotlib version
scatter = plt.scatter(data=penguins_smooth, x='flipper_length_mm', y='body_mass_g')
plt.xlabel('Flipper length (mm)')
plt.ylabel('Body mass (g)')
plt.title('Penguin flipper length vs body mass')
plt.savefig('penguin_flipper_vs_mass.png')

#Plotly version
import plotly.express as px
fig = px.scatter(penguins_smooth, x='flipper_length_mm', y='body_mass_g', color='species',
                labels={'flipper_length_mm': 'Flipper length (mm)', 'body_mass_g': 'Body mass (g)'},
                title='Penguin flipper length vs body mass by species')
fig.write_image('penguin_flipper_vs_mass_by_species_plotly.html')

#Plotnine version

ggplot(penguins, aes(x='flipper_length_mm', y='body_mass_g', color='species'))
geom_point()
ggplot.save(ggplot(penguins, aes(x='flipper_length_mm', y='body_mass_g', color='species')) +
    geom_point(), 'penguin_flipper_vs_mass_by_species_plotnine.png')
