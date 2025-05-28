import React, { useEffect, useState } from "react";
import { getPromos } from "../../utils/dataProvider/promo";

function AllPromo() {
  const [promos, setPromos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    const fetchPromos = async () => {
      try {
        setLoading(true);
        const response = await getPromos({ available: "true" }, controller);
        console.log("Promo API response:", response);
        if (response && response.data && Array.isArray(response.data.data)) {
          setPromos(response.data.data);
        } else if (response && response.data && Array.isArray(response.data)) {
          setPromos(response.data);
        } else {
          setPromos([]);
        }
      } catch (err) {
        if (err.name !== "AbortError") {
          setError("Failed to fetch promos");
        }
      } finally {
        setLoading(false);
      }
    };

    fetchPromos();

    return () => {
      controller.abort();
    };
  }, []);

  if (loading) {
    return <div>Loading promos...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  if (promos.length === 0) {
    return <div>No promos available</div>;
  }

  return (
    <div>
      <h1>Available Promos</h1>
      <ul>
        {promos.map((promo) => (
          <li key={promo.id}>
            <h2>{promo.name}</h2>
            <p>{promo.desc}</p>
            <p>Discount: {promo.discount}</p>
            <p>Coupon Code: {promo.coupon_code}</p>
            <p>
              Valid from: {new Date(promo.start_date).toLocaleDateString()} to{" "}
              {new Date(promo.end_date).toLocaleDateString()}
            </p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AllPromo;