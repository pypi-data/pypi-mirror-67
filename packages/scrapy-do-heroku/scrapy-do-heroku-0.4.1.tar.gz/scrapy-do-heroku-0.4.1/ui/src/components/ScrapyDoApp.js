//------------------------------------------------------------------------------
// Author: Lukasz Janyst <lukasz@jany.st>
// Date: 29.01.2018
//
// Licensed under the 3-Clause BSD License, see the LICENSE file for details.
//------------------------------------------------------------------------------

import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';

import ScrapyDoNav from './ScrapyDoNav';
import BackendStatus from './BackendStatus';
import Dashboard from './Dashboard';
import ProjectList from './ProjectList';
import JobList from './JobList';
import About from './About';
import WrongRoute from './WrongRoute';

class ScrapyDoApp extends Component {
  render() {
    return (
      <div>
        <ScrapyDoNav />
        <div className='content'>
          <BackendStatus />
          <Switch>
            <Route exact path='/' component={Dashboard} />
            <Route exact path='/dashboard' component={Dashboard} />
            <Route exact path='/project-list' component={ProjectList} />
            <Route path='/job-list/:status' component={JobList} />
            <Route exact path='/about' component={About} />
            <Route component={WrongRoute} />
          </Switch>
        </div>
      </div>
    );
  }
}

export default ScrapyDoApp;
