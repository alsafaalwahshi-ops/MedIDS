import numpy as np
from PIL import Image
import tensorflow as tf
import sys



model_path = "image_ids/ids_image.tflite"
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict(image):
    img = image.convert('RGB').resize((224, 224))
    img_array = np.array(img, dtype=np.float32)
    img_array = img_array / 255.0  
    img_array = np.expand_dims(img_array, axis=0) 
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()

    prediction = interpreter.get_tensor(output_details[0]['index'])[0][0]
    
    print(prediction)
    
    return prediction

   

