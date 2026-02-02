export default function UploadBox({ onFileSelect, onUpload, file }) {
  return (
    <div style={{
      border: "2px dashed #ccc",
      padding: "40px",
      textAlign: "center",
      margin: "20px 0"
    }}>
      <input type="file" accept=".csv" onChange={onFileSelect} />
      <br /><br />
      <button onClick={onUpload}>Run Analysis</button>
      {file && <p>{file.name}</p>}
    </div>
  );
}
