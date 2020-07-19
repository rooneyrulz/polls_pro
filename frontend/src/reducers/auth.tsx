import {
  USER_LOADED,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  AUTH_ERROR,
  LOGOUT,
} from '../action/types';

const initialState = {
  loading: true,
  token: localStorage.getItem('token'),
  user: null,
  isAuthenticated: null,
};

export default (state: any = initialState, action: any) => {
  const { type, payload } = action;

  switch (type) {
    case USER_LOADED:
      return {
        ...state,
        loading: false,
        isAuthenticated: true,
        ...payload,
      };

    case LOGIN_SUCCESS:
      localStorage.setItem('token', payload.token);
      return {
        ...state,
        loading: false,
        isAuthenticated: true,
        ...payload,
      };

    case LOGIN_FAIL:
    case AUTH_ERROR:
    case LOGOUT:
      localStorage.removeItem('token');
      return {
        ...state,
        loading: false,
        isAuthenticated: false,
        token: null,
        user: null,
      };

    default:
      return state;
  }
};
