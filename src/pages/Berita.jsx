import React, { useState, useEffect } from "react";
import Loading from '../components/Loading';

const newsArticles = [
  {
    id: 1,
    title: "Coffee Shop Lokal Meningkatkan Pengunjung dengan Menu Baru",
    date: "2024-06-10",
    summary: "Coffee Shop kami meluncurkan variasi minuman baru yang menarik perhatian para penikmat kopi setempat."
  },
  {
    id: 2,
    title: "Tren Kopi Cold Brew di Tahun 2024",
    date: "2024-06-05",
    summary: "Cold brew semakin populer di kalangan pecinta kopi muda, mengubah cara menikmati kopi di musim panas."
  },
  {
    id: 3,
    title: "Cara Menyajikan Kopi Berkualitas di Rumah",
    date: "2024-05-28",
    summary: "Tips dan trik sederhana agar Anda bisa menikmati kopi ala coffee shop favorit tanpa harus keluar rumah."
  },
  {
    id: 4,
    title: "Sustainability di Dunia Coffee Shop",
    date: "2024-05-15",
    summary: "Coffee shop kami berkomitmen meminimalisir limbah dan mendukung petani kopi yang berkelanjutan."
  },
];

const NewsPage = () => {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Simulate data fetching delay
    const timer = setTimeout(() => {
      setLoading(false);
    }, 500);

    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="news-container">
      <h1 className="news-title">Berita Seputar Coffee Shop</h1>
      {loading ? (
        <Loading />
      ) : (
        <div className="news-list">
          {newsArticles.map(({ id, title, date, summary }) => (
            <article key={id} className="news-card">
              <h2 className="news-article-title">{title}</h2>
              <time className="news-date" dateTime={date}>
                {new Date(date).toLocaleDateString("id-ID", {
                  day: "numeric",
                  month: "long",
                  year: "numeric",
                })}
              </time>
              <p className="news-summary">{summary}</p>
            </article>
          ))}
        </div>
      )}
      <footer className="news-footer">
        <p>© 2024 Coffee Shop News. Semua hak cipta dilindungi.</p>
      </footer>
    </div>
  );
};

export default NewsPage;

