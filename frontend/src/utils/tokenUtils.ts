// const TOKEN_KEY = 'token';

// получение токенов
export const getAccessToken = (): string | null => {
  return localStorage.getItem("access_token");
};

export const getRefreshToken = (): string | null => {
  return localStorage.getItem("refresh_token");
};

// установка токена
export const setAccessToken = (access_token: string): void => {
  localStorage.setItem("access_token", access_token);
};

export const setRefreshToken = (refresh_token: string): void => {
  localStorage.setItem("refresh_token", refresh_token);
};

// удаление токенов
export const removeAccessToken = (): void => {
  localStorage.removeItem("access_token");
};

export const removeRefreshToken = (): void => {
  localStorage.removeItem("refresh_token");
};