import React from 'react';
import { Route, Switch } from 'react-router-dom';
import App from './components/App';
import Home from './components/Home';
import About from './components/About';
import Openings from './components/Openings';

const routes = (
  <App>
    <Switch>
      <Route exact path='/' component={Home} />
      <Route path='/about' component={About} />
      <Route path='/openings' component={Openings} />
    </Switch>
  </App>
)

export { routes };
