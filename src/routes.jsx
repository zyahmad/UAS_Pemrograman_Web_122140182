import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Products from './pages/Products';
import ProductDetail from './pages/ProductDetail';
import Cart from './pages/Cart';
import Checkout from './pages/Checkout';
import OrderConfirmation from './pages/OrderConfirmation';
import NotFound from './pages/NotFound';
import Tentang from './pages/Tentang';
import Berita from './pages/Berita';
import Kontak from './pages/Kontak';

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/menu" element={<Products />} />
      <Route path='/tentang' element={<Tentang />} />
      <Route path="/products/:id" element={<ProductDetail />} />
      <Route path="/berita" element={<Berita />} />
      <Route path="/kontak" element={<Kontak />} />
      <Route path="/cart" element={<Cart />} />
      <Route path="/checkout" element={<Checkout />} />
      <Route path="/order-confirmation" element={<OrderConfirmation />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
};

export default AppRoutes;