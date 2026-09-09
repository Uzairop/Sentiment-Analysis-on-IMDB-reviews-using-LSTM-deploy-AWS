# Sentiment Analysis on IMDb Reviews Using LSTM

This project implements a sentiment analysis system on IMDb movie reviews using a Long Short-Term Memory (LSTM) neural network. The project is built with Django for the web interface and leverages Keras and TensorFlow for the deep learning model.
Project Overview

<img width="1039" height="378" alt="image" src="https://github.com/user-attachments/assets/d8be00ca-bcc1-4557-8330-bd9eaeb58829" />

This sentiment analysis project aims to classify movie reviews from IMDb as either positive or negative using a neural network, specifically an LSTM. The project demonstrates the application of deep learning in natural language processing (NLP) and provides a web-based interface to interact with the model.
Motivation

Sentiment analysis is a crucial task in natural language processing, widely used in areas like market research, customer feedback, and social media monitoring. IMDb reviews are an excellent resource for understanding public sentiment towards movies. By using an LSTM model, this project can capture the sequential nature of text data, making it highly effective for sentiment prediction.
Architecture

The project consists of the following components:

    Frontend: Built with Django templates, HTML, and CSS, providing a user-friendly interface to input movie reviews.
    Backend: Powered by Django, handling requests, model inference, and database interactions.
    Model: An LSTM neural network built using Keras and TensorFlow, trained on IMDb reviews to classify sentiment.
    Database: Used to store user inputs and results for further analysis (if needed).

# Features

    Sentiment Analysis: Classifies movie reviews into positive or negative categories.
    LSTM Neural Network: Uses an LSTM model built with Keras and TensorFlow for accurate sentiment prediction.
    Web Interface: Django-based web interface to input reviews and display predictions.
    Scalable: Easily extendable to other NLP tasks with minimal modifications.

# Prerequisites

Ensure you have the following installed:

    Python 3.7+
    Django 3.0+
    TensorFlow 2.x
    Keras 2.x
    NumPy
    Pandas

# Usage
Running the Development Server

Start the Django development server:

python manage.py runserver

Visit http://127.0.0.1:8000 in your web browser.
Inputting Reviews

    Enter a movie review in the text box provided.
    Click the "Analyze" button.
    The predicted sentiment (positive/negative) will be displayed on the screen.


# Future Improvements

    Data Augmentation: Enhance the training dataset by including more diverse reviews to improve model accuracy.
    Hyperparameter Tuning: Experiment with different LSTM architectures, activation functions, and optimizers to improve performance.
    Real-Time Sentiment Analysis: Extend the application to perform real-time sentiment analysis on live social media feeds or streaming data.
    Multilingual Support: Extend the model to handle reviews in multiple languages by using pre-trained embeddings or multi-lingual datasets.

# Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.
Additional Sections Explained

    Motivation: Explains the reason behind choosing this project and its importance in the field of NLP.
    Architecture: Provides an overview of the different components that make up the project.
    Future Improvements: Suggests possible enhancements to the project, making it more robust and scalable.
