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
        <h1 className="text-2xl font-bold">Admin Page</h1>

        <ul className="space-y-4 text-lg">
          {applications.map((app) => (
            <li key={app.id}>
                <p>Username: {app.username}</p>
                <p>Specialization: {app.specialization}</p>
                <p>Experience: {app.experience}</p>
                <p>Telegram ID: {app.telegram_id}</p>
                <p>Telegram Username: @{app.telegram_username}</p>
                <div className="flex space-x-2">
                  <button onClick={() => handleConfirm(app.id)} className="bg-green-500 text-white px-4 py-2 rounded">Confirm</button>
                  <button onClick={() => handleCancel(app.id)} className="bg-red-500 text-white px-4 py-2 rounded">Cancel</button>
                </div>
            </li>
          ))}
        </ul>
    </>
  )
}

export default AdminPage