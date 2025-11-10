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
