import React, { Fragment } from 'react';
import { Route, Switch } from 'react-router-dom';

// COMPONENTS
import Polls from '../pages/polls/Polls';
import Login from '../pages/auth/Login';
import Register from '../pages/auth/Register';

const Routing = () => {
  return (
    <Fragment>
      <Switch>
        <Route exact path='/' component={Polls} />
        <Route exact path='/login' component={Login} />
        <Route exact path='/register' component={Register} />
      </Switch>
    </Fragment>
  );
};

export default Routing;
