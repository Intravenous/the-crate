import React, { useState, useEffect } from 'react'
import ReactDOM from 'react-dom'
import { HashRouter, Switch, Route } from 'react-router-dom'

import 'bulma'
import './style.scss'

import Home from './components/Home'
import Search from './components/Search'
import NavBar from './components/NavBar'
import Login from './components/Login'
import Register from './components/Register'

const App = () => (
  <HashRouter>
    <NavBar />
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/search" component={Search} />
      <Route exact path="/login" component={Login} />
      <Route exact path="/register" component={Register} />
    </Switch>
  </HashRouter>
)

ReactDOM.render(<App />, document.getElementById('root'))
