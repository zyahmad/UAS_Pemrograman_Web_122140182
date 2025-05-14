import { IoIosStar } from "react-icons/io";
import PropTypes from 'prop-types';

const Popular = () => {
    const popularItems = [
        {
            id: 1,
            image: require('../assets/Popular/popular_1.png'),
            title: 'Vanilla Latte',
            price: '21k',
            rating: '3.8',
            description: 'Espresso yang lembut dicampur dengan susu dan vanila yang manis, menghadirkan rasa creamy dan aroma harum.'
        },
        {
            id: 2,
            image: require('../assets/Popular/popular_2.png'),
            title: 'Espresso',
            price: '12k',
            rating: '2.8',
            description: 'Kopi hitam pekat dengan cita rasa kuat, disajikan tanpa tambahan apapun untuk kenikmatan kopi murni.'
        },
        {
            id: 3,
            image: require('../assets/Popular/popular_3.png'),
            title: 'Hazelnut Latte',
            price: '23k',
            rating: '4.8',
            description: 'Kombinasi kopi espresso dan susu dengan sirop hazelnut yang manis memanjakan lidah Anda.'
        },
    ];

    return (
        <div className="popular-component">
            <div className="container">
                {/* Section Header */}
                <header className="section-header mb-5">
                    <h2>Popular <span>Now</span></h2>
                </header>

                <div className="popular-container">
                    <div className="row gy-5">
                        {popularItems.map(({ id, image, title, price, rating, description }) => (
                            <div key={id} className="col-xl-4 col-lg-4 col-md-12">
                                <div className="popular-content">
                                    <div className="popular-image">
                                        <img src={image} alt={title} />
                                        <div className="popular-rating">
                                            <button 
                                                className="d-flex align-items-center justify-content-center gap-1" 
                                                aria-label={`Rating for ${title}: ${rating}`}
                                                disabled
                                            >
                                                {rating} <IoIosStar color="#ff902b" />
                                            </button>
                                        </div>
                                    </div>
                                    <div className="card-info d-flex align-items-center justify-content-between">
                                        <h3>{title}</h3>
                                        <span>{price}</span>
                                    </div>
                                    <p className="popular-description">{description}</p>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
};

// Optional: Define PropTypes for better type checking
Popular.propTypes = {
    popularItems: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number.isRequired,
            image: PropTypes.oneOfType([PropTypes.string, PropTypes.object]).isRequired,
            title: PropTypes.string.isRequired,
            price: PropTypes.string.isRequired,
            rating: PropTypes.string.isRequired,
            description: PropTypes.string.isRequired,
        })
    )
};

export default Popular;

