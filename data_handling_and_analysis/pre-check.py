# Copy and paste the following code into a Jupypter Notebook

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from scipy import stats

famous_scientists = {'first_name': ['Albert', 'Marie', 'Isaac', 'Charles', 'Erwin', 'Francis'],
                     'last_name': ['Einstein', 'Curie', 'Newton', 'Darwin', 'Schrödinger', 'Crick'],
                     'field': ['physics', 'physics and chemistry', 'physics',
                               'biology and geology', 'physics', 'biology'],
                     'year_of_birth': [1879, 1867, 1642, 1809, 1887, 1916],
                     'place_of_birth': ['Ulm, Germany', 'Warsaw, Poland', 'Woolsthorpe, England',
                                        'Shrewsbury, England', 'Vienna, Austria', 'Northampton, England']}
df = pd.DataFrame(famous_scientists)
print(df)

x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
y = np.sin(x**2)
plt.plot(x, y)
plt.title('f(x) = sin(x²)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

x = np.linspace(-5, 15, 50)
plt.plot(x, stats.norm.pdf(x=x, loc=5, scale=2), lw=3)
plt.hist(stats.norm.rvs(loc=5, scale=2, size=1000),
                        bins=50, density=True, color='red', alpha=0.3)
plt.title('Gaussian distribution')
plt.show()