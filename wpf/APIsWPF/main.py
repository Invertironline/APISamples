import tkinter as tk
import requests
import json

class APISamplesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("API Samples App")
        self.geometry("800x600")

        self.api_url = "https://api.example.com"
        self.bearer_token = ""

        self.create_widgets()

    def create_widgets(self):
        self.token_label = tk.Label(self, text="Bearer Token:")
        self.token_label.pack()

        self.token_entry = tk.Entry(self, width=50)
        self.token_entry.pack()

        self.token_button = tk.Button(self, text="Set Token", command=self.set_token)
        self.token_button.pack()

        self.endpoint_label = tk.Label(self, text="API Endpoint:")
        self.endpoint_label.pack()

        self.endpoint_entry = tk.Entry(self, width=50)
        self.endpoint_entry.pack()

        self.request_button = tk.Button(self, text="Send Request", command=self.send_request)
        self.request_button.pack()

        self.response_text = tk.Text(self, wrap=tk.WORD, height=20, width=80)
        self.response_text.pack()

    def set_token(self):
        self.bearer_token = self.token_entry.get()

    def send_request(self):
        endpoint = self.endpoint_entry.get()
        url = f"{self.api_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.bearer_token}"}

        response = requests.get(url, headers=headers)
        response_data = response.json()

        self.update_response_text(response_data)

    def update_response_text(self, data):
        self.response_text.delete(1.0, tk.END)
        formatted_data = json.dumps(data, indent=4)
        self.response_text.insert(tk.END, formatted_data)

if __name__ == "__main__":
    app = APISamplesApp()
    app.mainloop()
