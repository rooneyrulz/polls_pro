import React from 'react';
import { withRouter } from 'react-router-dom';

import Button from 'react-bootstrap/Button';

const AppHeader: React.FC = (props: any) => {
  const redirectTo = (uri: string) => props.history.push(uri);

  return (
    <div className='AppHeader'>
      <Button type='button' onClick={(e) => redirectTo('/register')}>
        Register
      </Button>{' '}
      <Button type='button' onClick={(e) => redirectTo('/login')}>
        Login
      </Button>
    </div>
  );
};

export default withRouter(AppHeader);
