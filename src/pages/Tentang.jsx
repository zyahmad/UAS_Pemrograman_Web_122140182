import React from "react";

const AboutPage = () => {
  return (
    <div className="about-container">
      <h1 className="about-title">Tentang Coffee Shop Kami</h1>
      <p className="about-description">
        Selamat datang di coffee shop kami! Kami menghadirkan pengalaman ngopi terbaik dengan biji kopi pilihan dari seluruh dunia, diseduh dengan penuh cinta dan keahlian.
      </p>
      <p className="about-description">
        Kami berkomitmen untuk menciptakan suasana yang nyaman dan hangat bagi para pecinta kopi, serta memberikan pelayanan yang ramah dan profesional.
      </p>
      <div className="about-values-container">
        <div className="about-value-box">
          <h2 className="about-value-title">Visi</h2>
          <p className="about-value-text">
            Menjadi coffee shop terdepan yang dikenal akan kualitas kopi unggulan dan pengalaman pelanggan yang tak terlupakan.
          </p>
        </div>
        <div className="about-value-box">
          <h2 className="about-value-title">Misi</h2>
          <p className="about-value-text">
            Menyajikan kopi terbaik dengan bahan-bahan segar, serta menciptakan ruang hangat yang menginspirasi komunitas pecinta kopi.
          </p>
        </div>
        <div className="about-value-box">
          <h2 className="about-value-title">Nilai</h2>
          <p className="about-value-text">
            Kualitas, keaslian, keramahan, dan keberlanjutan adalah prinsip utama dalam setiap cangkir kopi yang kami sajikan.
          </p>
        </div>
      </div>
      <footer className="about-footer">
        <p>© 2024 Coffee Shop Kami. Semua hak cipta dilindungi.</p>
      </footer>
    </div>
  );
};

export default AboutPage;