#hello_ai.py
#jasmine radi
#Date: 10/21/2025

import random
import datetime

def greeting_agent():
    """
    a simple AI agent that provides personalized greetings
    This demonstrates a simple reflex agent from Chapter 2
    """

    #Get current time
    current_hour = datetime.datetime.now().hour
    
    #Determine time of day
    if current_hour < 12:
        time_period = "morning"
    elif current_hour < 17:
        time_period = "afternoon"
    else:
        time_period = "evening"

    #Get user's name
    name = input("What is your name?")
    graduate = input("What year do you graduate?") # make the program my own #step five

    #Generate personalized greeting

    greetings = [
        f"Good {time_period}, {name}! Welcome to AI class! You graduate in {graduate} which is soon!", #make the program my own #step five
        f"Hello {name}! Hope you're having a great {time_period}! Your graduation year is {graduate}, exciting times ahead!", #make the program my own #step five
        f"Hi {name}! Ready to learn AI this {time_period}?"
    ] 

    #Select and display random greeting
    print(random.choice(greetings))

    #Simple conversation
    mood = input("\nHow are you feeling about AI?")

    #Simple response based on keywords (reflex agent behavior)
    if "excited" in mood.lower() or "good" in mood.lower():
        print("That's wonderful! Your enthusiasm will help you learn!")
    elif "nervous" in mood.lower() or "worried" in mood.lower():
        print("Don't worry! We'll take it step by step.")
    elif "confused" in mood.lower() or "lost" in mood.lower():
        print("It's okay to feel that way. Ask questions whenever you need help!") #new response
    else:
        print(f"Thanks for sharing! Let's make this a great learning experience.")

    # Display an AI fact

    ai_facts = [
        "Did you know? The term 'Artificial Intelligence' was coined in 1956!",    
        "Fun fact: Your smartphone uses AI for face recognition!",
        "AI insight: Netflix uses AI to recommend shows you might like!",
        "Did you know? AI helps doctors detect diseases earlier!"
        "AI helps analyze vast amounts of data from space missions and can even make decisions to guide the missions themselves. " #new fact
        "AI is being used to create art, music, and even write stories!" #new fact
        "AI algorithms can learn and improve from experience without being explicitly programmed!" #new fact
        ]
    
    print(f"\n{random.choice(ai_facts)}")
    print("\nLet's start our AI journey together!")

    # Run the program

if __name__ == "__main__":
    print("="*50)
    print("Welcome to CSCI 130: Introduction to AI")
    print("="*50)
    print(greeting_agent())