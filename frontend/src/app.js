import React, { useState, useEffect } from 'react'
import ReactDOM from 'react-dom'
import { HashRouter, Switch, Route } from 'react-router-dom'

import 'bulma'
import './style.scss'

import Home from './components/Home'
import Search from './components/Search'
import NavBar from './components/NavBar'

const App = () => (
  <HashRouter>
    <NavBar />
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/search" component={Search} />
    </Switch>
  </HashRouter>
)

ReactDOM.render(<App />, document.getElementById('root'))
