import axios from 'axios';
import type { AxiosInstance, AxiosResponse, AxiosError, InternalAxiosRequestConfig } from 'axios';
import { getAccessToken, getRefreshToken, setAccessToken } from '../utils/tokenUtils';
import { refreshToken } from './authServices';

export interface ApiResponse<T = unknown> {
  data: T;
  status: number;
  message?: string;
}

const api: AxiosInstance = axios.create({
  // baseURL: import.meta.env.VITE_API_URL,
  baseURL: 'http://localhost:8000',
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  }
});

api.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    const token = getAccessToken();
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error: AxiosError) => Promise.reject(error)
);

export const getRequest = async <T = unknown>(url: string, params?: Record<string, unknown>): Promise<ApiResponse<T>> => {
  try {
    const response: AxiosResponse<T> = await api.get(url, { params });
    return {
      data: response.data,
      status: response.status,
    };
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      if (error.response?.status === 403 || error.response?.status === 401) {
        const newAccessToken: string = (await refreshToken(getRefreshToken())).access_token;
        setAccessToken(newAccessToken)
      }

      if (error.response?.status === 404) {
        window.location.href = '/error';
      }

      console.error(`API error for ${url}:`, error);

      const isArrayResponse = url.includes('/api/programs/');
      return {
        data: (isArrayResponse ? [] : {}) as T,
        status: error.response?.status || 500,
        message: (error.response?.data as { message: string })?.message || error.message,
      };
    }
    console.error(`An unexpected error occurred for ${url}:`, error);
    const isArrayResponse = url.includes('/api/programs/');
    return {
      data: (isArrayResponse ? [] : {}) as T,
      status: 500,
      message: error instanceof Error ? error.message : 'An unexpected error occurred',
    };
  }
};

export const postRequest = async <T = unknown>(url: string, data?: any): Promise<ApiResponse<T>> => {
  try {
    const response: AxiosResponse<T> = await api.post(url, data);
    return {
      data: response.data,
      status: response.status,
    };
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      if (error.response?.status === 403 || error.response?.status === 401) {
        const newAccessToken: string = (await refreshToken(getRefreshToken())).access_token;
        setAccessToken(newAccessToken)
      }

      if (error.response?.status === 404) {
        window.location.href = '/error';
      }

      return {
        data: {} as T,
        status: error.response?.status || 500,
        message: (error.response?.data as { message: string })?.message || error.message,
      };
    }
    console.error(`An unexpected error occurred for ${url}:`, error);
    return {
      data: {} as T,
      status: 500,
      message: error instanceof Error ? error.message : 'An unexpected error occurred',
    };
  }
};

export const deleteRequest = async <T = unknown>(url: string, data?: Record<string, unknown>): Promise<ApiResponse<T>> => {
  try {
    const response: AxiosResponse<T> = await api.delete(url, { data });
    return {
      data: response.data,
      status: response.status,
    };
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      if (error.response?.status === 403 || error.response?.status === 401) {
        const newAccessToken: string = (await refreshToken(getRefreshToken())).access_token;
        setAccessToken(newAccessToken)
      }

      if (error.response?.status === 404) {
        window.location.href = '/error';
      }

      return {
        data: {} as T,
        status: error.response?.status || 500,
        message: (error.response?.data as { message: string })?.message || error.message,
      };
    }
    console.error(`An unexpected error occurred for ${url}:`, error);
    return {
      data: {} as T,
      status: 500,
      message: error instanceof Error ? error.message : 'An unexpected error occurred',
    };
  }
}

export const patchRequest = async <T = unknown>(url: string, data?: Record<string, unknown>): Promise<ApiResponse<T>> => {
  try {
    const response: AxiosResponse<T> = await api.patch(url, data);
    return {
      data: response.data,
      status: response.status,
    };
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      if (error.response?.status === 403 || error.response?.status === 401) {
        const newAccessToken: string = (await refreshToken(getRefreshToken())).access_token;
        setAccessToken(newAccessToken)
      }

      if (error.response?.status === 404) {
        window.location.href = '/error';
      }

      return {
        data: {} as T,
        status: error.response?.status || 500,
        message: (error.response?.data as { message: string })?.message || error.message,
      };
    }
    console.error(`An unexpected error occurred for ${url}:`, error);
    return {
      data: {} as T,
      status: 500,
      message: error instanceof Error ? error.message : 'An unexpected error occurred',
    };
  }
}

export default api;