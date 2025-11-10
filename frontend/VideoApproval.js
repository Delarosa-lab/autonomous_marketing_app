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
import React, { useEffect, useState } from "react";
import axios from "axios";

const VideoApproval = () => {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/videos")
      .then(res => setVideos(res.data))
      .catch(err => console.log(err));
  }, []);

  const aprovar = (video) => {
    axios.post(`http://127.0.0.1:8000/api/videos/aprovar/${video}`)
      .then(() => alert(`Vídeo ${video} aprovado!`))
      .catch(err => console.log(err));
  }

  return (
    <div>
      {videos.map((video, idx) => (
        <div key={idx} className="flex items-center justify-between mb-2 p-2 border rounded">
          <span>{video}</span>
          <button onClick={() => aprovar(video)} className="bg-green-500 text-white px-2 py-1 rounded">Aprovar</button>
        </div>
      ))}
    </div>
  );
};

export default VideoApproval;
