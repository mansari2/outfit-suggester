import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

class OutfitModel:
    def __init__(self):
        self.model = DecisionTreeClassifier()
        self.label_encoders = {}

    def train_model(self, data):
        # Encode categorical features
        for column in data.columns:
            if data[column].dtype == 'object':
                le = LabelEncoder()
                data[column] = le.fit_transform(data[column])
                self.label_encoders[column] = le
        
        # Separate features and target
        X = data[['weather', 'occasion', 'clothing_item', 'color', 'material', 'characterization']]
        y = data['clothing_item']
        
        # Train the model
        self.model.fit(X, y)

    def predict_outfit(self, weather, occasion, available_items):
        # Encode input features
        input_data = {
            'weather': self.label_encoders['weather'].transform([weather])[0],
            'occasion': self.label_encoders['occasion'].transform([occasion])[0],
            'clothing_item': [self.label_encoders['clothing_item'].transform([item])[0] for item in available_items],
            'color': [self.label_encoders['color'].transform([item])[0] for item in available_items],
            'material': [self.label_encoders['material'].transform([item])[0] for item in available_items],
            'characterization': [self.label_encoders['characterization'].transform([item])[0] for item in available_items]
        }
        
        # Predict the outfit
        prediction = self.model.predict([input_data])
        return self.label_encoders['clothing_item'].inverse_transform(prediction)[0]