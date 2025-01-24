# Date Night Outfit Suggestor

This project is a simple machine learning application that suggests outfits based on weather and occasions. Its also a nice way to keep track of what I have in my closet so I can plan for dates with my wife

## Project Structure

```
outfit-suggester
├── src
│   ├── main.py          # Entry point of the application
│   ├── data
│   │   └── dataset.csv  # Dataset for training the model
│   ├── models
│   │   └── model.py     # Machine learning model for outfit suggestion
│   ├── utils
│       └── helpers.py   # Utility functions for data handling
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd outfit-suggester
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute the following command:

```
python src/main.py
```

## Usage

Once the application is running, you can input your preferences such as weather conditions and occasion, and the model will suggest suitable outfits based on the provided dataset.

## Contributing

Feel free to submit issues or pull requests for improvements or additional features.
