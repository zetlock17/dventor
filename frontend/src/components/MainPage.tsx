import { useNavigate } from 'react-router-dom';
import { logout } from '../services/authServices';

const MainPage = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div>
      <h1>Main Page</h1>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default MainPage;