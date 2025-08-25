import { postRequest, type ApiResponse } from './api';
import { setAccessToken, setRefreshToken, removeAccessToken, removeRefreshToken } from '../utils/tokenUtils';
import type { LoginMentorData, AuthResponse } from '../types/auth';

export const login = async (data: LoginMentorData): Promise<ApiResponse<AuthResponse>> => {
  const response = await postRequest<AuthResponse>('/auth/login', data);

  if (response.data && response.data.access_token) {
    setAccessToken(response.data.access_token);
    setRefreshToken(response.data.refresh_token);
  }

  return response;
};

// export const register = async (data: RegisterMentorData): Promise<ApiResponse<AuthResponse>> => {
//   const response = await postRequest<AuthResponse>('/auth/register/mentor', data);

//   if (response.data && response.data.access_token) {
//     setAccessToken(response.data.access_token); 
//     setRefreshToken(response.data.refresh_token);
//   }

//   return response;
// };

export const refreshToken = async (token: string | null): Promise<string> => {
  try {
    const response = await postRequest<string>('auth/refresh-token', token);
    console.log('Refresh token response:', response);
    if (response.data) {
      setAccessToken(response.data);
    }
    window.location.reload();
    return response.data;
  } catch (error) {
    console.error('Failed to refresh token:', error);
    logout()
    window.location.href = '/login';
    throw new Error('Token refresh failed');
  }
};

export const logout = (): void => {
  alert("Вы вышли из аккаунта!")
  removeAccessToken();
  removeRefreshToken();
};
