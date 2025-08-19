export interface LoginMentorData {
  login: string;
  password: string;
}

export interface RegisterMentorData {
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
