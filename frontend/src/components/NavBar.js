import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import auth from '../lib/auth'

class NavBar extends React.Component {
  constructor() {
    super()
    this.state = {}
  }

  handleLogout() {
    auth.logout()
    this.props.history.push('/')
  }

  render() {
    return (
      <nav className="navbar" role="navigation" aria-label="main navigation">
        <div className="container navbar-container">
          <div className="navbar-brand">
            <Link className="navbar-item" to="/">Home</Link>

            <a
              role="button"
              className={`navbar-burger burger ${
                this.state.navMobileOpen ? 'is-active' : ''
              }`}
              aria-label="menu"
              aria-expanded="false"
              onClick={() =>
                this.setState({ navMobileOpen: !this.state.navMobileOpen })
              }
            >
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
            </a>
          </div>

          <div
            className={`navbar-menu ${
              this.state.navMobileOpen ? 'is-active' : ''
            }`}>

            <div className="navbar-end">
              <div className="navbar-item">
                <Link to='/search'>Search</Link>
              </div>
              <div className="navbar-item">
                <Link to='/register'>Register</Link>
              </div>
              <div className="navbar-item">
                <Link to='/login'>Login</Link>
              </div>
              
              <div className="navbar-item">
                <Link to='/profile/:user_id'>Profile</Link>
              </div>
              <div
                onClick={() => this.handleLogout()}
                className="navbar-item">
                {/* Add in this code once login and logout is working */}
                {/* {isLoggedIn && <Link className="navbar-edited">Log out</Link>} */}
                <Link className="navbar-edited">Log out</Link>
              </div>
            </div>
          </div>
        </div>
      </nav>
    )
  }
}

export default withRouter(NavBar)