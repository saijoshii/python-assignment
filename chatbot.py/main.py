import random
import re
import json
import time
import os

qa_dict = {} # This dictionary will store questions/answers

def load_qa(): # Function to load questions/answers from a file
    global qa_dict
    try:
        with open("qa_data.json", "r") as file:
            qa_dict = json.load(file)
    except FileNotFoundError:
        qa_dict = {}

def save_qa(): # Function to save question answers to a file
    with open("qa_data.json", "w") as file:
        json.dump(qa_dict, file)

def save_user_data(user_name, user_question, response): # Function to save user names and questions to a file
    with open("user_log.txt", "a") as file:
        file.write(f"User: {user_name}, Question: {user_question}, Response: {response}\n")

def get_agent_name(): # Function to get a random agent name
    agent_names = ["Sai", "Dipsan", "Stuti", "Eva", "Kohli", "Patrick"] 
    return random.choice(agent_names) #selects name from the list randomly

def greet_user(agent_name): # Function to greet the user and get their name
    while True:
        user_name = input("\nHello! Welcome to the University of Poppleton. May I know your name? ")
        if re.search(r'\d', user_name): #makes sure that the name does not contain numbers
            print("Names cannot contain numbers. Please enter a valid name.")
        else:
            break
    print(f"Hi {user_name}! My name is {agent_name}. How can I help you today?")
    return user_name

def help(): # Function to show help message
    print("You can ask me any questions about the University of Poppleton.")
    print("To exit the chat, you can type 'bye', 'quit', 'exit', or any similar word.")
    print("If you need help, just type 'help'.")

def admin(): # Function for the admin page
    while True:
        print("\nAdmin Page")
        print("1. Add Question and Answer")
        print("2. View All Questions and Answers")
        print("3. View User Logs")
        print("4. Exit Admin Page")
        choice = input("Enter your choice: ")

        if choice == "1": #question and answer can be added
            question = input("Enter the question: ").strip().lower()
            answer = input("Enter the answer: ").strip()
            qa_dict[question] = answer
            save_qa()
            print("Question and answer added successfully.")
        elif choice == "2": #can view the question and answers
            if not qa_dict:
                print("No questions and answers available.")
            else:
                for q, a in qa_dict.items():
                    print(f"Q: {q}\nA: {a}\n")
        elif choice == "3": #view user logs
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

def question(user_name, user_input): # Function to handle user questions
    keywords = { #defining keywords and there random responses
        "coffee": "The campus coffee shop is open from 7 AM to 5 PM.",
        "parking": " Parking is beside block A and it is free.",
        "transportation":" The university does not have the transportation facility at the moment",
        "admission": "You can find admission details on our website or contact the admission office.",
        "admission office" : " You can contact the admisson office on 01-123321",
        "library": "The library is open from 8:30 AM to 9:00 PM everyday.",
        "courses": "We offer a wide range of undergraduate and postgraduate courses. Check our website for details.",
        "website":" Simply search Poppleton university on google and click on the first link."
    }
    random_response = [ #list of random messages deploys whenever there is no matched Kyewords
        "Hmmm i did not get that, please be clear.",
        "I'm not sure about that, but I'll find out for you.",
        "Could you clarify your question please?",
        "I am confused would you clarify a bit?",
        f"Thank you for asking, {user_name}. I will pass your question to the relevant department.",
    ]

    response = None #checks if keyword matches or not
    for keyword, reply in keywords.items():
        if keyword in user_input:
            response = reply
            break

    if not response: #random response if no keyword is found
        response = random.choice(random_response)

    print(response) #print response
    save_user_data(user_name, user_input, response)

def disconnect(): # Function to randomly disconnect
    if random.random() < 0.05:  # There is 5% chance of disconnection
        print("seems like we got disconnected. Please refresh or try reconnecting later.")
        exit()

def main(): # Main function to run the chatbot
    load_qa() #load any existing Q/A 
    agent_name = get_agent_name()
    user_name = greet_user(agent_name)

    while True:
        disconnect() #checks for disconnection
        user_input = input(f"{user_name}, please enter your question: ").strip().lower()
        if user_input in ["bye", "quit", "exit", "goodbye", "see you", "later"]:
            print(f"Goodbye {user_name}! Have a great day!")
            break
        elif user_input == "help": #displays help
            help()
        elif user_input == "admin":
            print("Entering Admin Page. Please follow the instructions.")
            admin() #enter admin page for managing q/a.
        else:
            question(user_name, user_input)

# It runs the main function if the script is executed
if __name__ == "__main__":
    main()
