import React from "react";

const MarketingApproval = () => {
  const investimentos = [
    { descricao: "Marketing Ebook Instagram", valor: 20 },
    { descricao: "Marketing Produto TikTok", valor: 10 },
  ];

  return (
    <div>
      {investimentos.map((item, idx) => (
        <div key={idx} className="flex items-center justify-between mb-2 p-2 border rounded">
          <span>{item.descricao} - ${item.valor}</span>
          <button className="bg-green-500 text-white px-2 py-1 rounded">Aprovar</button>
        </div>
      ))}
    </div>
  );
};

export default MarketingApproval;
