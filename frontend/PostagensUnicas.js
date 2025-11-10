import React, { useEffect, useState } from "react";
import axios from "axios";

const PostagensUnicas = () => {
  const [postagens, setPostagens] = useState([]);

  const carregarPostagens = () => {
    axios.get("http://127.0.0.1:8000/api/postagens")
      .then(res => setPostagens(res.data))
      .catch(err => console.log(err));
  };

  useEffect(() => {
    carregarPostagens();
  }, []);

  const aprovarTodas = () => {
    const promises = postagens.map((_, idx) =>
      axios.post(`http://127.0.0.1:8000/api/postagens/aprovar/${idx}`)
    );

    Promise.all(promises)
      .then(() => {
        alert("Todas as postagens aprovadas e liberadas!");
        carregarPostagens();
      })
      .catch(err => console.log(err));
  };

  return (
    <div>
      <button
        onClick={aprovarTodas}
        className="bg-green-600 text-white px-4 py-2 rounded mb-4"
      >
        Aprovar Todas as Postagens da Semana/Dia
      </button>

      {postagens.map((post, idx) => (
        <div
          key={idx}
          className="flex items-center justify-between mb-2 p-2 border rounded"
        >
          <span>
            {post.tipo} - {post.arquivo} - Rede: {post.rede_social} - Horário: {post.horario_sugerido} - Aprovado: {post.aprovado.toString()}
          </span>
        </div>
      ))}
    </div>
  );
};

export default PostagensUnicas;
