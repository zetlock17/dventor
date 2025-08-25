// import { useNavigate } from 'react-router-dom';
// import { logout } from '../services/authServices';
import { getMentors } from '../services/mentorsServices';
import { type Mentor } from '../types/mentor';
import { useEffect, useState } from 'react';

const MainPage = () => {
  // const navigate = useNavigate();
  const [mentors, setMentors] = useState<Mentor[]>([]);

  useEffect(() => {
    const fetchMentors = async () => {
      const response = await getMentors();
      if (response.status === 200) {
        setMentors(response.data);
      } else {
        alert(response.message);
      }
    };

    fetchMentors();
  }, []);

  // const handleLogout = () => {
  //   logout();
  //   navigate('/login');
  // };

  return (
    <div className='bg-gradient-to-tl from-purple-200 to-white h-screen p-10'>
      {/* <button onClick={handleLogout}>Logout</button> */}
      <h1 className="text-2xl font-semibold">Менторы</h1>
      <ul className="flex justify-center m-4 gap-10">
        {mentors.map((mentor) => (
          <li key={mentor.id} className='flex flex-col justify-around w-100 h-80 p-2 rounded-xl border border-purple-300  bg-white'>
            <div className='flex gap-4'>
              <div className="w-15 h-15 rounded-full border border-neutral-300 "/>
              <div>
                <p className='text-center text-[var(--main-purple)]'>{mentor.name}</p>
                <p className='text-center text-[var(--main-purple)]'>{mentor.surname}</p>
                <p className='text-center text-[var(--main-purple)]'>{mentor.specialization}</p>
              </div>
            </div>
              <p>Опыт: {mentor.experience}</p>
              <p>Опыт: {mentor.city}</p>
              <p>Опыт: {mentor.company}</p>
              <p>Опыт: {mentor.descriptiion}</p>
              <p>Опыт: {mentor.place_of_study}</p>
              <p>Опыт: {mentor.post}</p>
              <p>Опыт: {mentor.specialization}</p>
              <p>Опыт: {mentor.stack}</p>
            <div className='bg-neutral-200 h-0.5'/>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MainPage;