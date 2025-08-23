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
    <div>
      <h1 className="text-2xl font-bold">Main Page</h1>
      {/* <button onClick={handleLogout}>Logout</button> */}
      <h2 className="text-xl font-semibold">Mentors</h2>
      <ul className="space-y-4">
        {mentors.map((mentor) => (
          <li key={mentor.id}>
            <h3>{mentor.username}</h3>
            <p>Specialization: {mentor.specialization}</p>
            <p>Experience: {mentor.experience} years</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MainPage;