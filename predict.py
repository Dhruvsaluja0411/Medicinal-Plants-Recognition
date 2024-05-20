import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Load the model for inference
loaded_model = load_model('akash_plants.h5')

# Define class mapping
class_mapping = {
    0: 'Aloevera',
    1: 'Amla',
    2: 'Amruta Balli',
    3: 'Arali',
    4: 'Ashoka',
    5: 'Ashwagandha',
    6: 'Avacado',
    7: 'Bamboo',
    8: 'Basale',
    9: 'Betel',
    10: 'Betel_Nut',
    11: 'Brahmi',
    12: 'Castor',
    13: 'Curry Leaf',
    14: 'Doddapatre',
    15: 'Ekka',
    16: 'Ganike',
    17: 'Gauva',
    18: 'Geranium',
    19: 'Henna',
    20: 'Hibiscus',
    21: 'Honge',
    22: 'Insulin',
    23: 'Jasmine',
    24: 'Lemon',
    25: 'Lemon_grass',
    26: 'Mango',
    27: 'Mint',
    28: 'Nagadali',
    29: 'Neem',
    30: 'Nithyapushpa',
    31: 'Nooni',
    32: 'Pappaya',
    33: 'Pepper',
    34: 'Pomegranate',
    35: 'Raktachandini',
    36: 'Rose',
    37: 'Sapota',
    38: 'Tulasi',
    39: 'Wood_sorel',
}

def predict_plant(filename):
    img = cv2.imread(filename)
    img = cv2.resize(img, (150, 150))
    img = img / 255.0  # Normalize the image

    # Expand dimensions to create a batch of 1
    img = np.expand_dims(img, axis=0)

    # Make predictions using the loaded model
    predictions = loaded_model.predict(img)

    # Process the predictions to get the plant name and confidence
    plant_index = np.argmax(predictions)  # Get the index of the predicted class
    confidence = predictions[0, plant_index]  # Get the confidence score for the predicted class
    plant_name = class_mapping[plant_index]  # Get the name of the predicted plant

    return plant_name, confidence
