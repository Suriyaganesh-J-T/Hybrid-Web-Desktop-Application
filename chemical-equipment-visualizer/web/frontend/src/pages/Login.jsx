import { useState } from "react";
import api from "../services/api";
import "./Login.css";

export default function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      await api.post("auth/login/", { username, password });
      onLogin();
    } catch {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="login-container">
      <div className="login-card">
        <div className="login-icon">🧪</div>
        <h2>Sign in</h2>
        <p className="login-subtitle">
          Chemical Equipment Parameter Visualizer
        </p>

        <input
          className="login-input"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
        />

        <input
          className="login-input"
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button className="login-button" onClick={handleLogin}>
          Log In
        </button>
      </div>
    </div>
  );
}
