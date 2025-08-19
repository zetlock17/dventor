import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { register } from '../services/authServices';

const RegisterPage = () => {
  const [username, setUsername] = useState('');
  const [loginField, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await register({ username, login: loginField, password });
    if (response.status === 200 || response.status === 201) {
      navigate('/');
    } else {
      alert(response.message);
    }
  };

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
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
        <button type="submit">Register</button>
      </form>
      <button onClick={() => navigate('/login')}>Go to Login</button>
    </div>
  );
};

export default RegisterPage;