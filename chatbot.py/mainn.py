import random
import re
import json
import time
import os

# This dictionary will store questions and answers
qa_dict = {}

# Function to load questions and answers from a file
def load_qa():
    global qa_dict
    try:
        with open("qa_data.json", "r") as file:
            qa_dict = json.load(file)
    except FileNotFoundError:
        qa_dict = {}

# Function to save questions and answers to a file
def save_qa():
    with open("qa_data.json", "w") as file:
        json.dump(qa_dict, file)

# Function to save user names and questions to a file
def save_user_data(user_name, user_question, response):
    with open("user_log.txt", "a") as file:
        file.write(f"User: {user_name}, Question: {user_question}, Response: {response}\n")

# Function to get a random agent name
def get_agent_name():
    agent_names = ["Sai", "Dipsan", "Stuti", "Eva", "Kohli", "Patrick"]
    return random.choice(agent_names)

# Function to greet the user and get their name
def greet_user(agent_name):
    while True:
        user_name = input("\nHello! Welcome to the University of Poppleton. What's your name? ")
        if re.search(r'\d', user_name):
            print("Names cannot contain numbers. Please enter a valid name.")
        else:
            break
    print(f"Hi {user_name}! My name is {agent_name}. How can I help you today?")
    return user_name

# Function to show help message
def handle_help():
    print("You can ask me any questions about the University of Poppleton.")
    print("To exit the chat, you can type 'bye', 'quit', 'exit', or any similar word.")
    print("If you need help, just type 'help'.")

# Function for the admin page
def admin_page():
    while True:
        print("\nAdmin Page")
        print("1. Add Question and Answer")
        print("2. View All Questions and Answers")
        print("3. View User Logs")
        print("4. Exit Admin Page")
        choice = input("Enter your choice: ")

        if choice == "1":
            question = input("Enter the question: ").strip().lower()
            answer = input("Enter the answer: ").strip()
            qa_dict[question] = answer
            save_qa()
            print("Question and answer added successfully.")
        elif choice == "2":
            if not qa_dict:
                print("No questions and answers available.")
            else:
                for q, a in qa_dict.items():
                    print(f"Q: {q}\nA: {a}\n")
        elif choice == "3":
            if os.path.exists("user_log.txt"):
                with open("user_log.txt", "r") as file:
                    user_logs = file.read()
                    print("\nUser Logs:\n" + user_logs)
            else:
                print("No user logs available.")
        elif choice == "4":
            print("Exiting Admin Page.")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle user questions
def handle_question(user_name, user_input):
    keywords = {
        "coffee": "The campus coffee bar is open from 7 AM to 5 PM.",
        "parking": " Parking is beside block A and it is free.",
        "transportation":" The university does not have the transportation facility at the moment",
        "admission": "You can find admission details on our website or contact the admission office.",
        "admission office" : " You can contact the admisson office on 01-123321",
        "library": "The library is open from 8:30 AM to 9:00 PM everyday.",
        "courses": "We offer a wide range of undergraduate and postgraduate courses. Check our website for details.",
        "website":" Simply search Poppleton university on google and click on the first link."
    }
    random_responses = [
        "Hmmm i did not get that, let me get back to you on that.",
        "I'm not sure about that, but I'll find out for you.",
        "Could you clarify your question please?",
        "I am confused for"
        f"Thank you for asking, {user_name}. I’ll pass your question to the relevant department.",
    ]

    response = None
    for keyword, reply in keywords.items():
        if keyword in user_input:
            response = reply
            break

    if not response:
        response = random.choice(random_responses)

    print(response)
    save_user_data(user_name, user_input, response)

# Function to randomly disconnect
def maybe_disconnect():
    if random.random() < 0.05:  # 5% chance of disconnection
        print("seems like we got disconnected. Please refresh or try reconnecting later.")
        exit()

# Main function to run the chatbot
def main():
    load_qa()
    agent_name = get_agent_name()
    user_name = greet_user(agent_name)

    while True:
        maybe_disconnect()
        user_input = input(f"{user_name}, please enter your question: ").strip().lower()
        if user_input in ["bye", "quit", "exit", "goodbye", "see you", "later"]:
            print(f"Goodbye {user_name}! Have a great day!")
            break
        elif user_input == "help":
            handle_help()
        elif user_input == "admin":
            print("Entering Admin Page. Please follow the instructions.")
            admin_page()
        else:
            handle_question(user_name, user_input)

# This runs the main function if the script is executed
if __name__ == "__main__":
    main()
