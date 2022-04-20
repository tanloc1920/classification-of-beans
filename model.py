import pandas as pd


df = pd.read_csv('./Dry_Bean_Dataset.csv')

y = df.Class
X = df.drop(columns=['Class'])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.tree import DecisionTreeClassifier
def training_model():
    model = DecisionTreeClassifier(criterion="entropy",min_samples_leaf=5, max_depth= 25)
    trained_model = model.fit(X_train, y_train)
    return trained_model