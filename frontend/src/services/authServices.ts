import { postRequest, type ApiResponse } from './api';
import { setToken, removeToken } from '../utils/tokenUtils';
import type { LoginMentorData, RegisterMentorData, AuthResponse } from '../types/auth';

export const login = async (data: LoginMentorData): Promise<ApiResponse<AuthResponse>> => {
  const response = await postRequest<AuthResponse>('/auth/login', data);

  if (response.data && response.data.token) {
    setToken(response.data.token);
  }

  return response;
};

export const register = async (data: RegisterMentorData): Promise<ApiResponse<AuthResponse>> => {
  const response = await postRequest<AuthResponse>('/auth/register/mentor', data);

  if (response.data && response.data.token) {
    setToken(response.data.token);
  }

  return response;
};

export const logout = (): void => {
  removeToken();
};
