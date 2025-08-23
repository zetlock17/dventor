import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="py-4 bg-white">
      <nav className="container mx-auto px-4 flex gap-6 items-center">
        <Link to="/" className="text-blue-600 hover:underline">Home</Link>
        <Link to="/admin" className="text-gray-700 hover:text-gray-900">Admin</Link>
        <div className="ml-auto flex gap-4">
          <Link to="/login" className="text-gray-600 hover:text-gray-800">Login</Link>
          <Link to="/register" className="text-white bg-blue-600 hover:bg-blue-700 px-3 py-1 rounded">Register</Link>
        </div>
      </nav>
    </header>
  );
};

export default Header;