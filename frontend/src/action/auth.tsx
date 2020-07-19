import axios from 'axios';
import {
  USER_LOADED,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  AUTH_ERROR,
  LOGOUT,
} from './types';

// LOAD USER
export const loadUser = () => async (dispatch: any) => {
  const config: any = {
    header: {
      'Content-Type': 'application/json',
    },
  };

  // Check for the token in local storage
  if (localStorage.token)
    config.header['Authorization'] = `Token ${localStorage.token}`;

  try {
    const { data } = await axios.get('/api/account/user', config);
    dispatch({
      type: USER_LOADED,
      payload: data,
    });
  } catch (error) {
    dispatch({ type: AUTH_ERROR });
    console.log(`loaduser error: ${error}`);
  }
};

// LOGIN
export const login = (payload: Object) => async (dispatch: any) => {
  loadUser();

  const config: any = {
    header: {
      'Content-Type': 'application/json',
    },
  };

  try {
    const { data } = await axios.post('/api/account/login', payload, config);
    dispatch({
      type: LOGIN_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({ type: LOGIN_FAIL });
    console.log(`login error: ${error}`);
  }
};
