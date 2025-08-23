import { useEffect, useState } from "react";
import { cancelApplication, confirmApplication, getApplications } from "../services/applicationServices";
import type { application } from '../types/application';


const AdminPage = () => {
  const [applications, setApplications] = useState<application[]>([]);

  const fetchApplications = async () => {
    const response = await getApplications();
    setApplications(response.data);
    console.log(response);
  };

  useEffect(() => {
    fetchApplications();
  }, []);

  const handleConfirm = async (id: number) => {
    const response = await confirmApplication(id);
    alert(response.status || 'Application confirmed');
    fetchApplications();
  };

  const handleCancel = async (id: number) => {
    const response = await cancelApplication(id);
    alert(response.status || 'Application cancelled');
    fetchApplications();
  };

  return (
    <>
        <h1>Admin Page</h1>

        <ul>
          {applications.map((app) => (
            <li key={app.id}>
                <p>Username: {app.username}</p>
                <p>Login: {app.login}</p>
                <p>Password: {app.password}</p>
                <p>Specialization: {app.specialization}</p>
                <p>Experience: {app.experience}</p>
                <p>Telegram ID: {app.telegram_id}</p>
                <p>Telegram Username: {app.telegram_username}</p>
                <p>Status: {app.status}</p>
                <button onClick={() => handleConfirm(app.id)}>Confirm</button>
                <button onClick={() => handleCancel(app.id)}>Cancel</button>
            </li>
          ))}
        </ul>
    </>
  )
}

export default AdminPage