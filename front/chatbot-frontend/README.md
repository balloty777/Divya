# Chatbot Frontend

This project is a React-based frontend for a chatbot application that integrates with a Python backend using Streamlit. The chatbot is designed to provide a conversational experience with a character named Divya, who interacts with users in Hinglish.

## Project Structure

```
chatbot-frontend
├── public
│   └── index.html          # Main HTML file for the React application
├── src
│   ├── App.jsx             # Main component of the React application
│   ├── components
│   │   └── ChatWindow.jsx  # Component for the chat interface
│   ├── services
│   │   └── api.js          # API service for interacting with the backend
│   └── styles
│       └── main.css        # CSS styles for the application
├── package.json             # NPM configuration file
└── README.md                # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd chatbot-frontend
   ```

2. **Install dependencies:**
   ```
   npm install
   ```

3. **Run the application:**
   ```
   npm start
   ```

   This will start the development server and open the application in your default web browser.

## Usage

- The application provides a chat interface where users can interact with Divya.
- Type your message in the input box and hit enter to send it.
- Divya will respond in Hinglish, maintaining a playful and romantic tone.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.