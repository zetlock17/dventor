import type { newApplication, application } from '../types/application';
import { postRequest, getRequest, type ApiResponse } from './api';

export const createApplication = async (data: newApplication): Promise<ApiResponse> => {
  const response = await postRequest('/application/send', data);
  return response;
};

export const getApplications = async (): Promise<ApiResponse<application[]>> => {
  const response = await getRequest<application[]>('/application/');
  return response;
};

export const confirmApplication = async (application_id: number): Promise<ApiResponse> => {
  const response = await postRequest(`/application/confirm?application_id=${application_id}`);
  return response;
};

export const cancelApplication = async (application_id: number): Promise<ApiResponse> => {
  const response = await postRequest(`/application/cancel?application_id=${application_id}`);
  return response;
};