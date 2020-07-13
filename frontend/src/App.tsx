import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

// COMPONENTS
import Polls from './pages/Polls';
import Register from './pages/auth/Register';
import Login from './pages/auth/Login';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <div className='App'>
        <header></header>
        <main>
          <Switch>
            <Route exact path='/' component={Polls} />
            <Route exact path='/login' component={Login} />
            <Route exact path='/register' component={Register} />
          </Switch>
        </main>
        <footer></footer>
      </div>
    </BrowserRouter>
  );
};

export default App;
