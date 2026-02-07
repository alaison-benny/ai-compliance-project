import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
import sys

try:
    # 1. Test Pandas and Numpy
    df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    mean_val = np.mean(df['a'])
    
    # 2. Test Scikit-Learn
    model = LinearRegression()
    
    print("--- Environment Check ---")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Pandas: {pd.__version__}")
    print(f"Numpy: {np.__version__}")
    print(f"Scikit-Learn: {sklearn.__version__}")
    print("\nStatus: All systems go! 🚀")
    print("Data processing and ML model initialization successful.")

except Exception as e:
    print(f"\n❌ Error detected: {e}")
