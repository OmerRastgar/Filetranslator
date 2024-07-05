import customtkinter as ctk
from tkinter import filedialog

# Initialize the custom tkinter library
ctk.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("File Selection and Processing")
        self.geometry("400x200")

        # Variables to store file paths
        self.template_path = ctk.StringVar()
        self.english_doc_path = ctk.StringVar()
        self.other_lang_path = ctk.StringVar()
        self.selected_language = ctk.StringVar()

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Sidebar frame with buttons
        sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="s")

       

        self.template_button = ctk.CTkButton(sidebar_frame, text="Template", command=self.select_template)
        self.template_button.grid(row=2, column=0, padx=20, pady=10)

        self.english_doc_button = ctk.CTkButton(sidebar_frame, text="English Doc", command=self.select_english_doc)
        self.english_doc_button.grid(row=3, column=0, padx=20, pady=10)

        self.other_lang_button = ctk.CTkButton(sidebar_frame, text="Other Lang", command=self.select_other_lang)
        self.other_lang_button.grid(row=4, column=0, padx=20, pady=10)

        # Language selection dropdown
        self.language_label = ctk.CTkLabel(self, text="Select Language")
        self.language_label.grid(row=0, column=1, padx=20, pady=(20, 0))
        
        languages = ["Spanish", "Italian", "Portuguese"]
        self.language_dropdown = ctk.CTkComboBox(self, values=languages, variable=self.selected_language)
        self.language_dropdown.grid(row=1, column=1, padx=20, pady=10)

        # Compute button
        self.compute_button = ctk.CTkButton(self, text="Compute", command=self.compute)
        self.compute_button.grid(row=2, column=1, padx=20, pady=20)

    def select_template(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.template_path.set(file_path)

    def select_english_doc(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.english_doc_path.set(file_path)

    def select_other_lang(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.other_lang_path.set(file_path)

    def compute(self):
        template_path = self.template_path.get()
        english_doc_path = self.english_doc_path.get()
        other_lang_path = self.other_lang_path.get()
        selected_language = self.selected_language.get()

        if template_path and english_doc_path and other_lang_path and selected_language:
            self.process_files(template_path, english_doc_path, other_lang_path, selected_language)
        else:
            print("Please select all files and a language.")

    def process_files(self, template, english_doc, other_lang, language):
        # Implement your file processing logic here
        print(f"Processing files:\nTemplate: {template}\nEnglish Doc: {english_doc}\nOther Lang: {other_lang}\nLanguage: {language}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
