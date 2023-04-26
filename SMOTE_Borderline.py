import pandas as pd
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import BorderlineSMOTE, SVMSMOTE, ADASYN
from sklearn.preprocessing import LabelEncoder
# Load the dataset
df = pd.read_csv('cleaned_indian_liver.csv')

# Label encode the 'gender' feature
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])


# Plot the scatter plot before SMOTE
plt.scatter(df['Albumin'], df['TP'], c=df['Disease'])
plt.title('Scatter plot before SMOTE')
plt.xlabel('Albumin')
plt.ylabel('TP')
plt.show()


# Separate the dataset into features and target variable
X = df.drop('Disease', axis=1)
y = df['Disease']

# Perform SMOTE
sm = BorderlineSMOTE()
X_res, y_res = sm.fit_resample(X, y)

# Combine the resampled data into a new dataframe
df_resampled = pd.concat([pd.DataFrame(X_res), pd.DataFrame(y_res, columns=['Disease'])], axis=1)

# Plot the scatter plot after SMOTE
plt.scatter(df_resampled['Albumin'], df_resampled['TP'], c=df_resampled['Disease'])
plt.title('Scatter plot after Borderline SMOTE')
plt.xlabel('Albumin')
plt.ylabel('TP')
plt.show()
