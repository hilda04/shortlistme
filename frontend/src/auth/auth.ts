const TOKEN_KEY = 'shortlistme_token';

export const authStore = {
  getToken: () => localStorage.getItem(TOKEN_KEY),
  setToken: (token: string) => localStorage.setItem(TOKEN_KEY, token),
  clear: () => localStorage.removeItem(TOKEN_KEY),
  isAuthenticated: () => Boolean(localStorage.getItem(TOKEN_KEY)),
};

export const cognitoConfig = {
  userPoolId: import.meta.env.VITE_COGNITO_USER_POOL_ID,
  clientId: import.meta.env.VITE_COGNITO_CLIENT_ID,
  region: import.meta.env.VITE_COGNITO_REGION,
};
