export default function SummaryCards({ summary }) {
  return (
    <div style={{ display: "flex", gap: "20px", margin: "20px 0" }}>
      <Card title="Total Units" value={summary.total_equipment} />
      <Card title="Avg Temp (°C)" value={summary.avg_temperature} />
      <Card title="Avg Pressure (atm)" value={summary.avg_pressure} />
      <Card title="Avg Flowrate" value={summary.avg_flowrate} />
    </div>
  );
}

function Card({ title, value }) {
  return (
    <div style={{
      background: "#fff",
      padding: "20px",
      width: "200px",
      boxShadow: "0 2px 6px rgba(0,0,0,0.1)"
    }}>
      <h4>{title}</h4>
      <h2>{value}</h2>
    </div>
  );
}
