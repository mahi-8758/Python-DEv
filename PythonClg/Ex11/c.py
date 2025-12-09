import numpy as np
import pandas as pd
arr = np.array([10, 20, 30, 40, 50])
print("Numpy Mean:", np.mean(arr))
data = {'Name': ['Ajay', 'Raj', 'sauarbh'],
        'Marks': [80, 92, 75]}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)
print("Average Marks:", df['Marks'].mean())