export default function DataTable({ data = [] }) {
  if (!Array.isArray(data) || data.length === 0) {
    return <p>No data to display</p>;
  }

  return (
    <table border="1" width="100%">
      <thead>
        <tr>
          <th>Equipment</th>
          <th>Type</th>
          <th>Flowrate</th>
          <th>Pressure</th>
          <th>Temperature</th>
        </tr>
      </thead>
      <tbody>
        {data.slice(0, 5).map((row, i) => (
          <tr key={i}>
            <td>{row["Equipment Name"]}</td>
            <td>{row.Type}</td>
            <td>{row.Flowrate}</td>
            <td>{row.Pressure}</td>
            <td>{row.Temperature}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
