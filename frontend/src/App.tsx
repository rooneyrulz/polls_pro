import React, { useEffect } from 'react';
import { BrowserRouter } from 'react-router-dom';

// LAYOUTS
import AppHeader from './layouts/AppHeader';
import AppFooter from './layouts/AppFooter';

// ROUTES
import Routing from './routes/Routing';

// PROVIDER
import RootProvider from './RootProvider';

// REDUX
import store from './store';
import { loadUser } from './action/auth';

// STYLES
import './App.css';

const App: React.FC = () => {
  // useEffect(() => {
  //   store.dispatch(loadUser());
  // }, []);

  return (
    <RootProvider>
      <BrowserRouter>
        <div className='App'>
          <header>
            <AppHeader />
          </header>
          <main>
            <Routing />
          </main>
          <footer>
            <AppFooter />
          </footer>
        </div>
      </BrowserRouter>
    </RootProvider>
  );
};

export default App;
