import React, { useState, useEffect } from 'react'
import ReactDOM from 'react-dom'
import { HashRouter, Switch, Route } from 'react-router-dom'
// import 'bulma'
// import './style.scss'

import Home from './components/Home'

const App = () => (
  <HashRouter>
    <Switch>
      <Route exact path="/" component={Home} />
    </Switch>
  </HashRouter>
)

ReactDOM.render(<App />, document.getElementById('root'))
