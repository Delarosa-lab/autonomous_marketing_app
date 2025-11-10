import React from "react";

const EbookApproval = () => {
  const ebooks = ["ebook_semanal.pdf", "ebook_curto_dia_1.pdf"];

  return (
    <div>
      {ebooks.map((ebook, idx) => (
        <div key={idx} className="flex items-center justify-between mb-2 p-2 border rounded">
          <span>{ebook}</span>
          <button className="bg-green-500 text-white px-2 py-1 rounded">Aprovar</button>
        </div>
      ))}
    </div>
  );
};

export default EbookApproval;
import React, { useEffect, useState } from "react";
import axios from "axios";

const EbookApproval = () => {
  const [ebooks, setEbooks] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/ebooks")
      .then(res => setEbooks(res.data))
      .catch(err => console.log(err));
  }, []);

  const aprovar = (ebook) => {
    axios.post(`http://127.0.0.1:8000/api/ebooks/aprovar/${ebook}`)
      .then(() => alert(`Ebook ${ebook} aprovado!`))
      .catch(err => console.log(err));
  }

  return (
    <div>
      {ebooks.map((ebook, idx) => (
        <div key={idx} className="flex items-center justify-between mb-2 p-2 border rounded">
          <span>{ebook}</span>
          <button onClick={() => aprovar(ebook)} className="bg-green-500 text-white px-2 py-1 rounded">Aprovar</button>
        </div>
      ))}
    </div>
  );
};

export default EbookApproval;
