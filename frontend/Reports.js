import React from "react";

const Reports = () => {
  const relatorios = ["Relatório diário", "Relatório semanal", "Relatório mensal"];

  return (
    <div>
      {relatorios.map((rel, idx) => (
        <div key={idx} className="mb-2 p-2 border rounded">
          <span>{rel}</span>
          <button className="bg-blue-500 text-white px-2 py-1 rounded ml-2">Visualizar</button>
        </div>
      ))}
    </div>
  );
};

export default Reports;
import React, { useState } from "react";
import axios from "axios";

const Reports = () => {
  const [message, setMessage] = useState("");

  const gerarRelatorio = (periodo) => {
    axios.get(`http://127.0.0.1:8000/api/marketing/relatorio/${periodo}`)
      .then(res => setMessage(res.data.message))
      .catch(err => console.log(err));
  };

  const periodos = ["diario", "semanal", "mensal", "trimestral", "semestral", "anual"];

  return (
    <div>
      {periodos.map((periodo, idx) => (
        <div key={idx} className="mb-2 p-2 border rounded flex items-center justify-between">
          <span>{periodo}</span>
          <button onClick={() => gerarRelatorio(periodo)} className="bg-blue-500 text-white px-2 py-1 rounded ml-2">Gerar</button>
        </div>
      ))}
      {message && <p className="mt-2 font-semibold">{message}</p>}
    </div>
  );
};

export default Reports;
