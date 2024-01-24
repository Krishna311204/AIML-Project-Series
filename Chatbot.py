import tkinter as tk
from tkinter import Scrollbar, Text, Entry, INSERT, END

class ChatBot:
    def __init__(self):
        self.memory = {}

    def greet(self):
        return "Hello! I'm Jarvis, your friendly chatbot. How can I assist you today?"

    def farewell(self):
        return "Goodbye! If you have more questions, feel free to ask anytime."

    def respond_to_basic_questions(self, question):
        responses = {
            "How are you?": "I'm doing well, thank you!",
            "What's your name?": "I am Jarvis, a chatbot.",
            "Who created you?": "I was created by Krishna P Palekar, using Python.",
            "What is the meaning of life?": "The meaning of life is a philosophical question. I'm just here to help!",
            "Can you tell a joke?": "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
            "Tell me about yourself.": "I'm a chatbot designed to assist with basic questions and have conversations.",
            "What do you like to do?": "I enjoy helping and chatting with you.",
            "Where are you from?": "I exist in the digital realm, but my creator is from Chennai, India.",
            "Do you have any siblings?": "No, I was the only chatbot created by Krishna.",
            "What's your favorite color?": "I like Red.",
            "What's the weather like today?": "I'm sorry, I don't have real-time information. You can check a weather website for the current conditions.",
            "Tell me a fun fact.": "Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "What's the latest news?": "I don't have access to real-time news, but you can stay updated by checking reputable news websites or apps.",
            "How can I learn programming?": "Learning programming is a great decision! There are many online resources. You can also explore books and practice by working on small projects."
        }
        return responses.get(question, "I'm not sure how to answer that.")

class ChatBotGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Jarvis")
        self.master.geometry("400x400")
        self.master.configure(bg="#FF0000")  # Set background color to red

        self.chat_display = Text(self.master, wrap="word", width=40, height=10, bg="#FFFFFF", fg="#000000", insertbackground="#000000", selectbackground="#000000")
        self.chat_display.insert(INSERT, "Type a message\n")
        self.chat_display.pack(pady=10)

        self.scrollbar = Scrollbar(self.master, command=self.chat_display.yview, bg="#FF0000", troughcolor="#000000")
        self.scrollbar.pack(side="right", fill="y")

        self.chat_display.configure(yscrollcommand=self.scrollbar.set)

        self.user_input_entry = Entry(self.master, width=30, bg="#FFFFFF", fg="#000000", insertbackground="#000000")
        self.user_input_entry.insert(0, "Type a message")
        self.user_input_entry.pack(pady=10)
        self.user_input_entry.bind("<FocusIn>", self.clear_default_message)
        self.user_input_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.master, text="Send", command=self.send_message, bg="#000000", fg="#FFFFFF")
        self.send_button.pack()

        self.chatbot = ChatBot()

    def clear_default_message(self, event):
        if self.user_input_entry.get() == "Type a message":
            self.user_input_entry.delete(0, END)

    def send_message(self, event=None):
        user_input = self.user_input_entry.get()
        if user_input:
            self.display_message("You: " + user_input)
            if "exit" in user_input.lower():
                self.display_message("Chatbot: " + self.chatbot.farewell())
                self.master.after(2000, self.master.destroy)  # Close the GUI after 2 seconds
            else:
                response = self.chatbot.respond_to_basic_questions(user_input)
                self.display_message("Chatbot: " + response)
        self.user_input_entry.delete(0, END)
        self.user_input_entry.insert(0, "Type a message")

    def display_message(self, message):
        self.chat_display.insert(INSERT, message + "\n")
        self.chat_display.yview(END)


if __name__ == "__main__":
    root = tk.Tk()
    chatbot_gui = ChatBotGUI(root)
    root.mainloop()
