import tkinter as tk
from tkinter import Scrollbar, Text, Entry, INSERT, END, StringVar, OptionMenu

class CollegeAdmissionBot:
    def __init__(self):
        self.memory = {'name': None, 'preferred_field': None, 'application_status': None}
        self.college_recommendations = {"Engineering": ["IIT Bombay", "IIT Delhi", "IIT Madras", "BITS Pilani", "NIT Trichy"],
                                        "Medicine": ["AIIMS Delhi", "Christian Medical College Vellore", "Armed Forces Medical College Pune", "JIPMER Puducherry", "Maulana Azad Medical College Delhi"],
                                        "Business Administration": ["IIM Ahmedabad", "IIM Bangalore", "IIM Calcutta", "XLRI Jamshedpur", "FMS Delhi"],
                                        "Computer Science": ["IIT Bombay", "IIT Delhi", "IIT Madras", "BITS Pilani", "IIIT Hyderabad"],
                                        "Humanities": ["St. Stephen's College Delhi", "Lady Shri Ram College for Women Delhi", "Presidency College Kolkata", "Jawaharlal Nehru University Delhi", "Christ University Bengaluru"]}

    def greet(self):
        return "Hello! I'm Arjun, your college admission assistant. What's your name?"

    def ask_name(self):
        self.memory['name'] = "Arjun"
        return f"Nice to meet you. Please select your preferred field from the options below."

    def provide_field_options(self):
        return ["Select Field", "Engineering", "Medicine", "Business Administration", "Computer Science", "Humanities"]

    def update_memory(self, key, value):
        self.memory[key] = value

    def respond_to_admission_queries(self, question):
        admission_responses = {"admission procedures": f"For admission procedures in {self.memory['preferred_field']} programs, you typically need to submit an online application, provide high school transcripts, recommendation letters, and take part in an entrance exam. Please check the specific college's official website for detailed instructions.",
                               "admission requirements": f"The admission requirements for {self.memory['preferred_field']} programs usually include high school transcripts, competitive entrance exam scores, recommendation letters, and a well-crafted personal statement. Check the specific college's website for detailed information.",
                               "application deadlines": f"Application deadlines for {self.memory['preferred_field']} programs vary. It's important to check the specific college's official website for the most accurate and up-to-date information.",
                               "list of colleges": self.list_colleges_response(),
                               "status of my application": f"You can check the status of your application for {self.memory['preferred_field']} programs by logging into your online applicant portal or by contacting the admissions office. If you have an application reference number, I can guide you through the process.",
                               "default": f"I'm sorry, I don't have detailed information about {question.lower()} for {self.memory['preferred_field']} programs. You may want to check the college's official website or contact the admissions office for specific details."}

        return admission_responses.get(question.lower(), admission_responses["default"]).capitalize()

    def provide_personalized_response(self):
        if self.memory['preferred_field']:
            return f"Great choice! Aspiring to pursue {self.memory['preferred_field']} is commendable. Let me provide you with information specific to {self.memory['preferred_field']} programs."
        else:
            return "Feel free to ask any questions you have about the admission process."

    def list_colleges_response(self):
        if self.memory['preferred_field'] in self.college_recommendations:
            colleges = "\n".join(self.college_recommendations[self.memory['preferred_field']])
            return f"Here are some top colleges for {self.memory['preferred_field']} in India:\n{colleges}"
        else:
            return "I'm sorry, I don't have recommendations for colleges in that field at the moment."

    def handle_error(self):
        error_responses = ["I'm sorry, I couldn't understand that. Could you please rephrase?",
                           "I'm still learning. Could you provide more details or ask a different question?",
                           "I'm afraid I don't have information on that. Let's try another question."]
        return error_responses

class CollegeAdmissionGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("College Admission Chatbot")
        self.master.geometry("600x500")
        self.master.configure(bg="#FF0000")

        self.admission_bot = CollegeAdmissionBot()

        self.chat_display = Text(self.master, wrap="word", width=60, height=12, bg="#FFFFFF", fg="#000000", insertbackground="#000000", selectbackground="#000000", font=("Helvetica", 10), spacing1=5)
        self.chat_display.pack(pady=10)

        self.scrollbar = Scrollbar(self.master, command=self.chat_display.yview, bg="#FF0000", troughcolor="#000000")
        self.scrollbar.pack(side="right", fill="y")

        self.chat_display.configure(yscrollcommand=self.scrollbar.set, state=tk.DISABLED)

        self.user_input_entry = Entry(self.master, width=40, bg="#FFFFFF", fg="#000000", insertbackground="#000000", font=("Helvetica", 10))
        self.user_input_entry.insert(0, "Type a message")
        self.user_input_entry.pack(pady=10)
        self.user_input_entry.bind("<FocusIn>", self.clear_default_message)
        self.user_input_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.master, text="Send", command=self.send_message, bg="#000000", fg="#FF0000", font=("Helvetica", 10))
        self.send_button.pack()

        self.exit_button = tk.Button(self.master, text="Exit", command=self.exit_program, bg="#000000", fg="#FF0000", font=("Helvetica", 10))
        self.exit_button.pack(pady=10)

        self.display_message("Arjun: " + self.admission_bot.greet())
        self.display_message("Arjun: " + self.admission_bot.ask_name())

        self.field_var = StringVar()
        self.field_var.set("Select Field")
        self.field_options = self.admission_bot.provide_field_options()
        self.field_dropdown = OptionMenu(self.master, self.field_var, *self.field_options)
        self.field_dropdown.pack()

    def clear_default_message(self, event):
        if self.user_input_entry.get() == "Type a message":
            self.user_input_entry.delete(0, END)

    def send_message(self, event=None):
        user_input = self.user_input_entry.get()
        if user_input:
            self.display_message("You: " + user_input, is_user=True)

            if "exit" in user_input.lower():
                self.display_message("Arjun: Goodbye! If you have more questions, feel free to ask anytime.")
                self.master.after(2000, self.master.destroy)
            else:
                if not self.admission_bot.memory['name']:
                    self.admission_bot.update_memory('name', user_input)
                    self.display_message("Arjun: " + self.admission_bot.ask_name())

                elif not self.admission_bot.memory['preferred_field']:
                    if self.field_var.get() in self.field_options[1:]:
                        self.admission_bot.update_memory('preferred_field', self.field_var.get())
                        self.display_message("Arjun: " + self.admission_bot.provide_personalized_response())
                    else:
                        self.display_message("Arjun: Please select a valid field from the options.")

                else:
                    response = self.admission_bot.respond_to_admission_queries(user_input)
                    if "application status" in user_input:
                        reference_number = input("User: ")
                        self.admission_bot.update_memory('application_status', 'In Progress')
                        response = f"Arjun: Your application status is currently {self.admission_bot.memory['application_status']}."

                    self.display_message("Arjun: " + response)

        self.user_input_entry.delete(0, END)
        self.user_input_entry.insert(0, "Type a message")

    def exit_program(self):
        self.display_message("Arjun: Thank you for using the College Admission Chatbot. Goodbye!")
        self.master.after(2000, self.master.destroy)

    def display_message(self, message, is_user=False):
        self.chat_display.configure(state=tk.NORMAL)
        self.chat_display.insert(INSERT, message + "\n\n")
        self.chat_display.yview(END)
        self.chat_display.configure(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    admission_gui = CollegeAdmissionGUI(root)
    root.mainloop()
