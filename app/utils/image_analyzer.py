from app.model.predict import predict_image
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
def rebuild_model(num_classes):
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(244, 244, 3))
    for layer in base_model.layers:
        layer.trainable = False
    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    return model
model = rebuild_model(num_classes=7)
model.load_weights("app/model/SKIN Diseases.h5")
model.summary()
def analyze_image(filepath):
    """
    調用預測模型分析上傳的圖片，返回預測結果和信心水平。
    """
    global model  # 確保使用全局的 model 變數
    if model is None:
        return {"error": "Model is not initialized or failed to load."}
    try:
        # 調用 predict_image 函數進行圖片預測
        predicted_class, confidence = predict_image(filepath, model)
        
        # 返回結果
        return {
            "predicted_class": predicted_class,
            "confidence": f"{confidence * 100:.2f}%"
        }
    except Exception as e:
        # 如果發生錯誤，返回錯誤信息
        return {"error": str(e)}