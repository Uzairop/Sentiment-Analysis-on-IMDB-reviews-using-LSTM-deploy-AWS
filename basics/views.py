from django.shortcuts import render # type: ignore
import os
import pickle
import pandas as pd
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

def file(request):
    if request.method == "POST":
        data = request.POST
        neo = data.get('neo')

        if 'buttonflo' in request.POST:
            model_path = "sentiment_model.keras"
            tokenizer_path = "tokenizer.pkl"

            # Check if model and tokenizer exist
            if os.path.exists(model_path) and os.path.exists(tokenizer_path):
                model = load_model(model_path)
                with open(tokenizer_path, "rb") as f:
                    tokenizer = pickle.load(f)
            else:
                # Train model
                data = pd.read_csv("C:\\Users\\umraf\\Downloads\\archive\\IMDB Dataset.csv")
                data.replace({"sentiment": {"positive": 1, "negative": 0}}, inplace=True)
                train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

                tokenizer = Tokenizer(num_words=5000)
                tokenizer.fit_on_texts(train_data["review"])
                X_train = pad_sequences(tokenizer.texts_to_sequences(train_data["review"]), maxlen=200)
                X_test = pad_sequences(tokenizer.texts_to_sequences(test_data["review"]), maxlen=200)
                Y_train = train_data["sentiment"]
                Y_test = test_data["sentiment"]

                model = Sequential()
                model.add(Embedding(input_dim=5000, output_dim=128, input_length=200))
                model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
                model.add(Dense(1, activation="sigmoid"))
                model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

                model.fit(X_train, Y_train, epochs=3, batch_size=64, validation_split=0.2)

                # Save model and tokenizer
                model.save(model_path)
                with open(tokenizer_path, "wb") as f:
                    pickle.dump(tokenizer, f)

            # Prediction function
            def predict_sentiment(review):
                sequence = tokenizer.texts_to_sequences([review])
                padded = pad_sequences(sequence, maxlen=200)
                pred = model.predict(padded)
                return "positive" if pred[0][0] > 0.5 else "negative"

            res = predict_sentiment(neo)
            result = "Is positive Sentiment" if res == "positive" else "Is negative Sentiment"

            return render(request, "file.html", context={'result': result})

    return render(request, 'file.html')
