# Rule Based ChatBot For Retail <img src="https://cdn-icons-png.flaticon.com/512/6231/6231457.png" alt="Rule Based ChatBot For Retail" width="50" height="50">

A simple rule-based chatbot for retail that can answer customer queries related to a retail store's products and services.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Run App](#run-ai)
- [Usage](#usage)
- [Dockerized Web App](#dockerized-web-app)
- [Customization](#customization)
- [License](#license)

## About

This project implements a basic rule-based chatbot for a retail store. It is designed to respond to specific customer queries and provide information about products, promotions, order tracking, and more. The chatbot is trained to recognize user intents and respond with predefined answers.

## Features

- Responds to common greetings and farewells.
- Provides information about product availability and promotions.
- Explains the return policy for online orders.
- Guides users on tracking their orders.
- Describes accepted payment methods.
- Checks the status of recent orders.
- Assists with password reset.

## Project Structure

- `intents.json`: Contains the training data for the chatbot, including intents, patterns, and responses.
- `training.py`: A script for training the chatbot model using TensorFlow.
- `prediction.py`: Handles user input, predicts intents, and generates responses.
- `app.py`: The Streamlit web application for interacting with the chatbot.

## Getting Started

To get started with this project, you'll need Python and a few libraries installed. Follow these steps:

```bash
git clone https://github.com/iampraveens/Rule-Based-ChatBot-For-Retail.git
```

```bash
cd Rule-Based-ChatBot-For-Retail
```
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```
## Run App

```bash
streamlit run app.py
```
## Usage

- Type your questions or greetings in the input box and press Enter to get responses from the chatbot.
- The chatbot will understand your intent and respond accordingly.

## Dockerized Web App
You can also deploy the Rule Based ChatBot For Retail web application using Docker. Build the Docker image and run the container:
```bash
docker build -t your_docker_username/rule-based-chatbot-app .
```
- To build a docker image.

```bash
docker run -d -p 8501:8501 your_docker_username/rule-based-chatbot-app
```
- To run as a container.

Access the web app at `http://localhost:8501` or `your_ip_address:8501` in your web browser.
Else if you want to access my pre-built container, here is the code below to pull from docker hub(Public).
```bash
docker pull iampraveens/rule-based-chatbot-app:latest
```

## Customization
You can customize by adding more intents to `intents.json` file. Feel free to adapt and extend the system to suit your specific use case.

## License 
This project is licensed under the MIT License - see the [License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
