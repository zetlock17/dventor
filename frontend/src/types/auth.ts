export interface LoginMentorData {
  login: string;
  password: string;
}

// export interface RegisterMentorData {
//   username: string;
//   login: string;
//   password: string;
// }

export interface AuthResponse {
  access_token: string;
  refresh_token: string;
}

export interface RefreshTokenResponse {
  access_token: string;
}