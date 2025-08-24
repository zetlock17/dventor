import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createApplication } from '../services/applicationServices';

const RegisterPage = () => {
  const [username, setUsername] = useState<string>('');
  const [login, setLogin] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [specialization, setSpecialization] = useState<string>('');
  const [experience, setExperience] = useState<string>('');
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await createApplication({ username, login, password, specialization, experience });
    if (response.status === 200 || response.status === 201) {
      alert('всё гуд')
      alert('https://t.me/pizdotesto_bot?start=' + response.data)
      console.log(response)
      navigate('/');
    } else {
      alert(response.message);
      console.log(response)
    }
  };

  return (
    <div>
      <h2 className="text-xl font-semibold">Новая заявка</h2>
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
          value={login}
          onChange={(e) => setLogin(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <input 
          type="text"
          placeholder="Specialization"
          value={specialization}
          onChange={(e) => setSpecialization(e.target.value)}
        />
        <input
          type="text"
          placeholder="Experience"
          value={experience}
          onChange={(e) => setExperience(e.target.value)}
        />
        <button type="submit" className='bg-[var(--main-purple)] text-white px-4 py-2 rounded mt-2'>Отправить</button>
      </form>
      <button onClick={() => navigate('/login')} className='bg-[var(--main-purple)] text-white px-4 py-2 rounded mt-2'>Go to Login</button>
    </div>
  );
};

export default RegisterPage;