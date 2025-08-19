export interface LoginData {
  login: string;
  password: string;
}

export interface RegisterData {
  username: string;
  login: string;
  password: string;
}

export interface AuthResponse {
  token: string;
  user: {
    id: string;
    username: string;
    login: string;
  };
}
