import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler

# Function to predict MOS using the saved model
def predict_mos(model_file, scaler_file, new_feature_file, output_file):
    # Load the trained model
    svr_model = joblib.load(model_file)

    # Load the scaler
    scaler = joblib.load(scaler_file)

    # Load new features
    new_features = pd.read_csv(new_feature_file, index_col=0, keep_default_na=False)

    # Transform new features
    new_features_scaled = scaler.transform(new_features)

    # Predict MOS
    predicted_scores = svr_model.predict(new_features_scaled)

    # Convert to 0-10 scale if needed
    predicted_scores = predicted_scores * 10

    # Save the predicted scores to a CSV file
    result_df = pd.DataFrame(predicted_scores, index=new_features.index, columns=['Predicted_MOS'])
    result_df.to_csv(output_file)
    print(f'Predicted MOS scores saved to {output_file}')

# Path to the saved model, scaler, and new features
model_file = 'svr_model.joblib'
scaler_file = 'scaler.joblib'
new_feature_file = 'features.csv'
output_file = 'predicted_mos.csv'

# Predict MOS for new point clouds and save to CSV
predict_mos(model_file, scaler_file, new_feature_file, output_file)
