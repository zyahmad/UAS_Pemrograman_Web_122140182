import React, { useState } from "react";

const ContactPage = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    message: ""
  });

  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // For demo purposes, just set submitted flag
    if(formData.name && formData.email && formData.message){
      setSubmitted(true);
      setFormData({
        name: "",
        email: "",
        phone: "",
        message: ""
      });
    } else {
      alert("Mohon isi Nama, Email, dan Pesan.");
    }
  };

  return (
    <div className="contact-container">
      <h1 className="contact-title">Kontak Kami</h1>
      <p className="contact-intro">
        Kami senang mendengar dari Anda! Silakan isi formulir di bawah ini atau gunakan informasi kontak kami.
      </p>
      <div className="contact-content">
        <form className="contact-form" onSubmit={handleSubmit} noValidate>
          <label htmlFor="name">Nama<span className="required">*</span></label>
          <input
            type="text"
            id="name"
            name="name"
            placeholder="Nama Anda"
            value={formData.name}
            onChange={handleChange}
            required
          />

          <label htmlFor="email">Email<span className="required">*</span></label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="email@example.com"
            value={formData.email}
            onChange={handleChange}
            required
          />

          <label htmlFor="phone">Telepon</label>
          <input
            type="tel"
            id="phone"
            name="phone"
            placeholder="0812-3456-7890"
            value={formData.phone}
            onChange={handleChange}
          />

          <label htmlFor="message">Pesan<span className="required">*</span></label>
          <textarea
            id="message"
            name="message"
            placeholder="Tulis pesan Anda di sini..."
            rows="5"
            value={formData.message}
            onChange={handleChange}
            required
          />

          <button type="submit" className="submit-button">Kirim Pesan</button>
          {submitted && <p className="submit-success">Terima kasih! Pesan Anda sudah terkirim.</p>}
        </form>

        <aside className="contact-info">
          <h2>Info Kontak</h2>
          <p><strong>Alamat:</strong></p>
          <address>
            Jl. Kopi Nusantara No. 123,<br />
            Jakarta Selatan, 12345<br />
            Indonesia
          </address>
          <p><strong>Telepon:</strong> <a href="tel:+6281234567890">+62 812 3456 7890</a></p>
          <p><strong>Email:</strong> <a href="mailto:info@coffeeshop.com">info@coffeeshop.com</a></p>
          <p><strong>Jam Operasional:</strong> Senin - Minggu, 08.00 - 22.00 WIB</p>
          <div className="social-links">
            <a href="https://facebook.com/coffeeshop" target="_blank" rel="noopener noreferrer" aria-label="Facebook" className="social-icon">📘</a>
            <a href="https://instagram.com/coffeeshop" target="_blank" rel="noopener noreferrer" aria-label="Instagram" className="social-icon">📸</a>
            <a href="https://twitter.com/coffeeshop" target="_blank" rel="noopener noreferrer" aria-label="Twitter" className="social-icon">🐦</a>
          </div>
        </aside>
      </div>
    </div>
  );
};

export default ContactPage;