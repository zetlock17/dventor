import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createApplication } from '../services/applicationServices';

const RegisterPage = () => {
  const [login, setLogin] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [specialization, setSpecialization] = useState<string>('');
  const [experience, setExperience] = useState<number>(0);
  const [name, setName] = useState<string>('');
  const [surname, setSurname] = useState<string>('');
  const [place_of_study, setPlace_of_study] = useState<string>('');
  const [company, setCompany] = useState<string>('');
  const [post, setPost] = useState<string>('');
  const [descriptiion, setDescriptiion] = useState<string>('');
  const [stack, setStack] = useState<string[]>([]);
  const [age, setAge] = useState<number>(0);
  const [city, setCity] = useState<string>('');
  
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await createApplication({ login, password, name, surname, age, city, place_of_study, experience, company, post, descriptiion, specialization, stack  });
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
          onChange={(e) => setExperience(Number(e.target.value))}
        />
        <input
          type="text"
          placeholder="Age"
          value={age}
          onChange={(e) => setAge(Number(e.target.value))}
        />
        <input
          type="text"
          placeholder="Stack"
          value={stack}
          onChange={(e) => setStack([e.target.value])}
        />
        <input 
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input 
          type="text"
          placeholder="Surname"
          value={surname}
          onChange={(e) => setSurname(e.target.value)}
        />
        <input 
          type="text"
          placeholder="Place_of_study"
          value={place_of_study}
          onChange={(e) => setPlace_of_study(e.target.value)}
        />
        <input 
          type="text"
          placeholder="Company"
          value={company}
          onChange={(e) => setCompany(e.target.value)}
        />
        <input 
          type="text"
          placeholder="Post"
          value={post}
          onChange={(e) => setPost(e.target.value)}
        />
        <input 
          type="text"
          placeholder="Descriptiion"
          value={descriptiion}
          onChange={(e) => setDescriptiion(e.target.value)}
        />
        <input 
          type="text"
          placeholder="City"
          value={city}
          onChange={(e) => setCity(e.target.value)}
        />
        <button type="submit" className='bg-[var(--main-purple)] text-white px-4 py-2 rounded mt-2'>Отправить</button>
      </form>
      <button onClick={() => navigate('/login')} className='bg-[var(--main-purple)] text-white px-4 py-2 rounded mt-2'>Go to Login</button>
    </div>
  );
};

export default RegisterPage;