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
import React, { useEffect, useState } from "react";
import axios from "axios";

const MarketingApproval = () => {
  const [investimentos, setInvestimentos] = useState([]);

  const carregarVendas = () => {
    axios.get("http://127.0.0.1:8000/api/marketing/vendas")
      .then(res => setInvestimentos(res.data))
      .catch(err => console.log(err));
  };

  useEffect(() => {
    carregarVendas();
  }, []);

  const aprovar = (index) => {
    axios.post(`http://127.0.0.1:8000/api/marketing/aprovar/${index}`)
      .then(() => {
        alert(`Investimento ${index} aprovado!`);
        carregarVendas(); // Atualiza a lista
      })
      .catch(err => console.log(err));
  };

  return (
    <div>
      {investimentos.map((item, idx) => (
        <div key={idx} className="flex items-center justify-between mb-2 p-2 border rounded">
          <span>{item.origem} - Valor: ${item.valor_marketing} - Aprovado: {item.aprovado.toString()}</span>
          {!item.aprovado && (
            <button onClick={() => aprovar(idx)} className="bg-green-500 text-white px-2 py-1 rounded">Aprovar</button>
          )}
        </div>
      ))}
    </div>
  );
};

export default MarketingApproval;
