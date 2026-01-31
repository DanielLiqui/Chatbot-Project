import { useState } from "react";
import { sendMessage } from "../api";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);

    const response = await sendMessage(input);

    const botMsg = {
      role: "bot",
      text: response.response ?? "No answer from bot",
    };

    setMessages((prev) => [...prev, botMsg]);
    setInput("");
  };

  return (
    <div style={{ width: 400, margin: "50px auto" }}>
      <h2>Chatbot</h2>

      <div style={{ border: "1px solid #ccc", padding: 10, height: 300, overflowY: "auto" }}>
        {messages.map((m, i) => (
          <div key={i}>
            <b>{m.role}:</b> {m.text}
          </div>
        ))}
      </div>

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSend()}
        style={{ width: "100%", marginTop: 10 }}
      />
      <button onClick={handleSend} style={{ width: "100%", marginTop: 5 }}>
        Send
      </button>
    </div>
  );
}
