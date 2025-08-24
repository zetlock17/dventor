import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="py-4 bg-white">
      <nav className="container mx-auto px-4 flex gap-6 items-center">
        <Link to="/" className="text-[var(--main-purple)] hover:underline">Home</Link>
        <Link to="/admin" className="text-gray-700 hover:text-gray-900">Admin</Link>
        <div className="ml-auto flex gap-2">
          <Link to="/login" className="text-gray-600 hover:text-gray-800 px-3 py-1">Login</Link>
          <Link to="/register" className="text-white bg-[var(--main-purple)] hover:bg-purple-600 px-3 py-1 rounded">Register</Link>
        </div>
      </nav>
    </header>
  );
};

export default Header;