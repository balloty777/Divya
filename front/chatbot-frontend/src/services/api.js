import axios from 'axios';

const BACKEND_URL = "http://127.0.0.1:8000/chat";

export const sendMessageToChatbot = async (userMessage, history=[]) => {
    try {
        const response = await axios.post(BACKEND_URL, {
            message: userMessage,
            history: history
        });
        return response.data;
    } catch (error) {
        console.error("Error sending message to chatbot:", error);
        throw error;
    }
};