import React, { useEffect, useState } from "react";
import axios from "axios";

const Postagens = () => {
  const [postagens, setPostagens] = useState([]);

  const carregarPostagens = () => {
    axios.get("http://127.0.0.1:8000/api/postagens")
      .then(res => setPostagens(res.data))
      .catch(err => console.log(err));
  };

  const aprovar = (index) => {
    axios.post(`http://127.0.0.1:8000/api/postagens/aprovar/${index}`)
      .then(res => {
        alert("Postagem aprovada e agendada!");
        carregarPostagens();
      })
      .catch(err => console.log(err));
  };

  useEffect(() => {
    carregarPostagens();
  }, []);

  return (
    <div>
      {postagens.map((post, idx) => (
        <div key={idx} className="flex items-center justify-between mb-2 p-2 border rounded">
          <span>{post.tipo} - {post.arquivo} - Rede: {post.rede_social} - Horário sugerido: {post.horario_sugerido} - Aprovado: {post.aprovado.toString()}</span>
          {!post.aprovado && (
            <button onClick={() => aprovar(idx)} className="bg-green-500 text-white px-2 py-1 rounded">Aprovar</button>
          )}
        </div>
      ))}
    </div>
  );
};

export default Postagens;
