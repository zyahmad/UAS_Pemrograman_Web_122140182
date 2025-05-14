import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import useFetch from '../context/useFetch';
import ProductList from '../components/ProductList';
import Loading from '../components/Loading';
import Error from '../components/Error';
import Popular from '../components/Popular';

const Home = () => {
  // Ambil data kopi dari API hot
  const { data: coffeeData, loading, error } = useFetch('https://6823578865ba058033965cb4.mockapi.io/kopireem/Kopi');
  const [featuredProducts, setFeaturedProducts] = useState([]);

  useEffect(() => {
    if (coffeeData && coffeeData.length > 0) {
      // Ambil 4 produk pertama sebagai featured
      const simulatedProducts = coffeeData.slice(0, 4).map((item, index) => ({
        ...item,
        price: 15000 + index * 5000, // Simulasi harga
      }));
      setFeaturedProducts(simulatedProducts);
    }
  }, [coffeeData]);

  return (
    <div className="home-page">
      <Popular />

      <section className="featured-section py-12 px-4">
        <h2 className="text-2xl font-semibold mb-6 text-center">Featured Products</h2>
        {loading ? (
          <Loading />
        ) : error ? (
          <Error message={error} />
        ) : (
          <>
            <ProductList products={featuredProducts} />
            <div className="view-more text-center mt-8">
              <Link to="/products" className="view-more-link text-blue-600 hover:underline">
                View All Products
              </Link>
            </div>
          </>
        )}
      </section>
    </div>
  );
};

export default Home;