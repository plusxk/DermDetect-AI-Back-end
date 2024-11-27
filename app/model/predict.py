# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from PIL import Image
# 重建模型架構
# def rebuild_model(num_classes):
#     base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(244, 244, 3))
#     for layer in base_model.layers:
#         layer.trainable = False
#     model = Sequential([
#         base_model,
#         GlobalAveragePooling2D(),
#         Dense(512, activation='relu'),
#         Dropout(0.5),
#         Dense(num_classes, activation='softmax')
#     ])
#     return model
# model = rebuild_model(num_classes=7)
# model.load_weights("../SKIN Diseases.h5")
# model.summary()
class_labels = ['Eczema', 'Warts Molluscum and other Viral Infections', 
                'Atopic Dermatitis', 'Melanocytic Nevi', 
                'Psoriasis pictures Lichen Planus and related diseases', 
                'Seborrheic Keratoses and other Benign Tumors',
                'Tinea Ringworm Candidiasis and other Fungal Infections']


def predict_image(filepath, model):
    """
    傳入圖片路徑，進行預測並回傳結果
    """

    # img = Image.open(BytesIO(image.read()))
    # img = img.convert("RGB")  # 確保圖片是 RGB 格式
    # img = img.resize((244, 244))  # 調整大小與模型要求一致
    img = load_img(filepath, target_size=(244, 244))  # 確保尺寸與模型輸入相符
    img_array = img_to_array(img)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)  
    img_array = np.expand_dims(img_array, axis=0) 


    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class = class_labels[predicted_class_index]
    confidence = np.max(predictions)

    return predicted_class, confidence


# image_path = "../../../0_2.jpg" 
# predicted_class, confidence = predict_image(image_path)


# print(f"Predicted Class: {predicted_class}")
# print(f"Confidence: {confidence * 100:.2f}%")


# img = load_img(image_path, target_size=(244, 244))
# plt.imshow(img)
# plt.title(f"Predicted: {predicted_class} ({confidence * 100:.2f}%)")
# plt.axis('off')
# plt.show()