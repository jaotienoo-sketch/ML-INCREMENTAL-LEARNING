#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import shuffle

# Load dataset

df = pd.read_csv("cropyields.csv")

# Sort features and targets

X = df.drop("Class", axis=1).values
y = df["Class"].values

# Normalize Time and Amount

scaler = StandardScaler()
X[:, [0, 1]] = scaler.fit_transform(X[:, [0, 1]])

# Shuffle and simulate streaming

X, y = shuffle(X, y, random_state=42)

# Initialize incremental model

model = SGDClassifier(loss='log_loss', max_iter=1, warm_start=True)

# Define classes and batches

classes = np.unique(y)

batch_size = 10000
n_batches = X.shape[0] // batch_size

# Train the model

for i in range(n_batches):
    start = i * batch_size
    end = start + batch_size
    X_batch = X[start:end]
    y_batch = y[start:end]
    
    if i == 0:
        model.partial_fit(X_batch, y_batch, classes=classes)
    else:
        model.partial_fit(X_batch, y_batch)

    if i % 5 == 0:
        y_pred = model.predict(X_batch)
        acc = accuracy_score(y_batch, y_pred)
        print(f"Batch {i + 1}, Accuracy: {acc:.4f}")

# Final evaluation

y_pred = model.predict(X[-batch_size:])
print("\nFinal Batch Classification Report:\n")
print(classification_report(y[-batch_size:], y_pred))
