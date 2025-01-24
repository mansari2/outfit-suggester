import pandas as pd
from models.model import OutfitModel
from utils.helpers import load_data

def main():
    # Load the dataset
    data = load_data('data/dataset.csv')
    
    # Initialize the model
    outfit_model = OutfitModel()
    
    # Train the model
    outfit_model.train_model(data)
    
    # Example user input
    weather = input("Enter the weather condition (e.g., sunny, rainy): ")
    occasion = input("Enter the occasion (e.g., casual, formal): ")
    available_items = input("Enter available clothing items (comma-separated): ").split(',')
    
    # Suggest an outfit
    suggested_outfit = outfit_model.predict_outfit(weather, occasion, available_items)
    print("Suggested Outfit:", suggested_outfit)

if __name__ == "__main__":
    main()