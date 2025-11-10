import React from "react";
import PostagensUnicas from "./components/PostagensUnicas";
import VideoApproval from "./components/VideoApproval";
import EbookApproval from "./components/EbookApproval";
import MarketingApproval from "./components/MarketingApproval";
import Reports from "./components/Reports";

function App() {
  return (
    <div className="p-4 font-sans">
      <h1 className="text-2xl font-bold mb-4">Painel de Marketing Autônomo</h1>

      <section className="mb-6">
        <h2 className="text-xl font-semibold mb-2">Postagens Semanais/Dia</h2>
        <PostagensUnicas />
      </section>

      <section className="mb-6">
        <h2 className="text-xl font-semibold mb-2">Aprovação de Vídeos</h2>
        <VideoApproval />
      </section>

      <section className="mb-6">
        <h2 className="text-xl font-semibold mb-2">Aprovação de Ebooks</h2>
        <EbookApproval />
      </section>

      <section className="mb-6">
        <h2 className="text-xl font-semibold mb-2">Aprovação de Marketing</h2>
        <MarketingApproval />
      </section>

      <section>
        <h2 className="text-xl font-semibold mb-2">Relatórios</h2>
        <Reports />
      </section>
    </div>
  );
}

export default App;
