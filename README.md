Customer Car Price Estimator App
The Customer Car Price Estimator App is a Streamlit-based web application that helps customers estimate the price range of cars they can afford based on their age, salary, and net worth. The app utilizes a pre-trained machine learning model to provide personalized recommendations for suitable car options within the predicted price range.
Features

User-friendly interface for inputting age, salary, and net worth
Data preprocessing and scaling using pre-trained scaler
Price prediction with a pre-trained machine learning model
Display of predicted car price range
Tailored recommendations for suitable car options within the predicted range

Installation

Clone the repository:

bashCopy codegit clone https://github.com/Fastpacer/Machine-Learning-Project

Navigate to the project directory:

bashCopy codecd customer-car-price-estimator

Create a virtual environment (optional but recommended):

bashCopy codepython -m venv venv

Activate the virtual environment:

On Windows:

bashCopy codevenv\Scripts\activate

On Unix or macOS:

bashCopy codesource venv/bin/activate

Install the required dependencies:

bashCopy codepip install -r requirements.txt

Place the pre-trained model (model.pkl) and scaler (scaler.pkl) files in the project directory.

Usage

Run the Streamlit app:

bashCopy codestreamlit run app.py

The web application will open in your default browser.
Enter your age, salary, and net worth in the respective input fields.
Click the "Calculate" button.
The application will display the predicted car price range based on your input.
Explore the recommended car options within the predicted price range.

Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
License
This project is licensed under the MIT License.
Acknowledgments

Streamlit - The framework used for building the web application
scikit-learn - The machine learning library used for training and deploying the model
joblib - The library used for persisting and loading the pre-trained model and scaler