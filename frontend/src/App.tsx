import React from 'react';
import { BrowserRouter } from 'react-router-dom';

// LAYOUTS
import AppHeader from './layouts/AppHeader';
import AppFooter from './layouts/AppFooter';

// ROUTES
import Routing from './components/routes/Routing';

const App: React.FC = () => {
  return (
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
  );
};

export default App;
