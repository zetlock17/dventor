import { Navigate, Outlet } from 'react-router-dom';
import { getToken } from '../utils/tokenUtils';

const ProtectedRoute = () => {
  const isAuthenticated = !!getToken();

  return isAuthenticated ? <Outlet /> : <Navigate to="/login" />;
};

export default ProtectedRoute;
