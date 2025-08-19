const TOKEN_KEY = 'token';

// получение токена
export const getToken = (): string | null => {
  return localStorage.getItem(TOKEN_KEY);
};

// установка токена
export const setToken = (token: string): void => {
  localStorage.setItem(TOKEN_KEY, token);
};

// удаление токена
export const removeToken = (): void => {
  localStorage.removeItem(TOKEN_KEY);
};