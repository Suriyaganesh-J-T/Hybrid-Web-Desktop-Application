import { useState } from "react";
import api from "../services/api";

export default function Upload({ onUpload }) {
  const [file, setFile] = useState(null);

  const uploadCSV = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await api.post("upload/", formData);
    onUpload(res.data);
  };

  return (
    <div>
      <h2>Upload CSV</h2>
      <input type="file" accept=".csv" onChange={e => setFile(e.target.files[0])} />
      <button onClick={uploadCSV}>Upload</button>
    </div>
  );
}
