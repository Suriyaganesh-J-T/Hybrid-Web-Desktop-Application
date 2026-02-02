import { useState } from "react";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import api from "./services/api";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [summary, setSummary] = useState(null);
  const [rawData, setRawData] = useState([]);
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await api.post("upload/", formData);
    setSummary(res.data.summary);
    setRawData(res.data.rows);
  };

  if (!loggedIn) {
    return <Login onLogin={() => setLoggedIn(true)} />;
  }

  return (
    <Dashboard
      summary={summary}
      rawData={rawData}
      file={file}
      onFileSelect={(e) => setFile(e.target.files[0])}
      onUpload={handleUpload}
      logout={() => {
        setLoggedIn(false);
        setSummary(null);
        setRawData([]);
      }}
    />
  );
}

export default App;
