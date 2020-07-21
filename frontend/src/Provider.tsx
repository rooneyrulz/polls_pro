import React from 'react';

// REDUX
import { Provider } from 'react-redux';
import store from './store';

const Provider = (prop: any) => {
  return <Provider store={store}>{prop.children}</Provider>;
};

export default Provider;
