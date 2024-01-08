import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
import pickle

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('data/churn-prepared.csv',
                        sep=',', dtype=np.float64)
features = tpot_data.drop('Exited', axis=1)
training_features, testing_features, training_target, testing_target = \
    train_test_split(features, tpot_data['Exited'], random_state=42)

# Average CV score on the training set was: 0.8609333333333333
exported_pipeline = ExtraTreesClassifier(
    bootstrap=True, criterion="gini", max_features=0.9000000000000001, min_samples_leaf=6, min_samples_split=16, n_estimators=100)
# Fix random state in exported estimator
if hasattr(exported_pipeline, 'random_state'):
    setattr(exported_pipeline, 'random_state', 42)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)

pickle.dump(exported_pipeline, open("churn/models/model.pk", "wb"))
