import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
import SummaryCards from "../components/SummaryCards";
import DataTable from "../components/DataTable";
import { Bar } from "react-chartjs-2";

export default function Dashboard({
  summary,
  rawData,
  onUpload,
  onFileSelect,
  file,
  logout
}) {
  return (
    <>
      <Navbar onLogout={logout} />

      <div style={{ width: "90%", margin: "auto" }}>
        {/* Upload section always visible */}
        <UploadBox
          file={file}
          onFileSelect={onFileSelect}
          onUpload={onUpload}
        />

        {/* Show analysis ONLY after CSV upload */}
        {summary && (
          <>
            <SummaryCards summary={summary} />

            <div style={{ display: "flex", gap: "20px" }}>
              <div style={{ width: "50%" }}>
                <Bar
                  key={JSON.stringify(summary.type_distribution)}
                  data={{
                    labels: Object.keys(summary.type_distribution),
                    datasets: [
                      {
                        label: "Equipment Count",
                        data: Object.values(summary.type_distribution),
                        backgroundColor: "#5DADE2"
                      }
                    ]
                  }}
                  options={{ responsive: true }}
                />
              </div>

              <div style={{ width: "50%" }}>
                <DataTable data={rawData} />
                <br />
                <button
                  onClick={() =>
                    window.open("http://127.0.0.1:8000/api/report/pdf/")
                  }
                >
                  📄 View Report
                </button>
              </div>
            </div>
          </>
        )}
      </div>
    </>
  );
}
