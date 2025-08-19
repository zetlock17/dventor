import { postRequest, type ApiResponse } from './api';
import { setToken, removeToken } from '../utils/tokenUtils';
import type { LoginData, RegisterData, AuthResponse } from '../types/auth';

export const login = async (data: LoginData): Promise<ApiResponse<AuthResponse>> => {
  const response = await postRequest<AuthResponse>('/auth/login', data);

  if (response.data && response.data.token) {
    setToken(response.data.token);
  }

  return response;
};

export const register = async (data: RegisterData): Promise<ApiResponse<AuthResponse>> => {
  const response = await postRequest<AuthResponse>('/auth/register', data);

  if (response.data && response.data.token) {
    setToken(response.data.token);
  }

  return response;
};

export const logout = (): void => {
  removeToken();
};
