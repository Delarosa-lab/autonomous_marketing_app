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
