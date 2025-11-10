import React from "react";

const VideoApproval = () => {
  // Exemplo de vídeos pendentes (mais tarde virá do backend)
  const videos = ["video_longo_semanal.mp4", "video_curto_dia_1.mp4"];

  return (
    <div>
      {videos.map((video, idx) => (
        <div key={idx} className="flex items-center justify-between mb-2 p-2 border rounded">
          <span>{video}</span>
          <button className="bg-green-500 text-white px-2 py-1 rounded">Aprovar</button>
        </div>
      ))}
    </div>
  );
};

export default VideoApproval;
