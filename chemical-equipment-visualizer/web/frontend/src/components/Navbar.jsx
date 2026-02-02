export default function Navbar({ onLogout }) {
  return (
    <div style={{
      display: "flex",
      justifyContent: "space-between",
      padding: "15px 30px",
      background: "#ffffff",
      boxShadow: "0 2px 6px rgba(0,0,0,0.1)"
    }}>
      <h3>🧪 Chemical Equipment Parameter Visualizer</h3>
      <button onClick={onLogout} style={{ background: "#e74c3c", color: "#fff" }}>
        Logout
      </button>
    </div>
  );
}
