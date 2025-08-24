import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { login } from '../services/authServices';

const LoginPage = () => {
  const [loginField, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await login({ login: loginField, password });
    if (response.status === 200) {
      navigate('/');
    } else {
      alert(response.message);
    }
  };

  return (
    <div>
      <h2 className="text-xl font-semibold">Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Login"
          value={loginField}
          onChange={(e) => setLogin(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit" className='bg-[var(--main-purple)] text-white px-4 py-2 rounded mt-2'>Login</button>
      </form>
      <button onClick={() => navigate('/register')} className='bg-[var(--accent-green)] text-white px-4 py-2 rounded mt-2'>Подать заявку на создание аккаунта ментора</button>
    </div>
  );
};

export default LoginPage;