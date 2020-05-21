import React from 'react'
import axios from 'axios'
import auth from '../lib/auth'
// import { Link } from 'react-router-dom'

class Register extends React.Component {
  constructor() {
    super()
    this.state = {
      data: {
        email: '',
        username: '',
        first_name: '',
        last_name: '',
        password: '',
        password_confirmation: ''
      },
      errors: {}
    }
  }

  handleChange(event) {
    const { name, value } = event.target
    const data = { ...this.state.data, [name]: value }
    this.setState({ data })
  }

  handleSubmit(event) {
    event.preventDefault()
    axios
      .post('/api/register', this.state.data)
      .then((res) => console.log('response', res))
      .then((res) => {
        this.props.history.push('/login')
      })

      .catch((error) => {
        this.setState({ errors: error.response.data })
      })
  }

  render() {
    const { errors } = this.state

    return (
      <main className="hero is-fullheight">
        <div className="hero-body">
          <div className="container">
            <section className="section">
              <div className="container has-text-centered">
                <div className="columns">
                  <div className="column is-one-third"></div>
                  <div className="column is-block">
                    <div className="box">
                      <h1 className="title">Register</h1>
                      <form
                        className="form has text-left"
                        onSubmit={(event) => this.handleSubmit(event)}
                      >
                        <div className="field">
                          <label className="label">Email</label>
                          <div className="control">
                            <input
                              onChange={(event) => this.handleChange(event)}
                              type="text"
                              name="email"
                              className="input"
                            />
                          </div>
                          {errors.email && (
                            <small className="help is-danger">{errors.email}</small>
                          )}
                        </div>
                        <div className="field">
                          <label className="label">Username</label>
                          <div className="control">
                            <input
                              onChange={(event) => this.handleChange(event)}
                              type="text"
                              name="username"
                              className="input"
                            />
                          </div>
                          {errors.username && (
                            <small className="help is-danger">
                              {errors.username}
                            </small>
                          )}
                        </div>
                        <div className="field">
                          <label className="label">First name</label>
                          <div className="control">
                            <input
                              onChange={(event) => this.handleChange(event)}
                              type="text"
                              name="first_name"
                              className="input"
                            />
                          </div>
                          {errors.first_name && (
                            <small className="help is-danger">
                              {errors.first_name}
                            </small>
                          )}
                        </div>
                        <div className="field">
                          <label className="label">Last name</label>
                          <div className="control">
                            <input
                              onChange={(event) => this.handleChange(event)}
                              type="text"
                              name="last_name"
                              className="input"
                            />
                          </div>
                          {errors.last_name && (
                            <small className="help is-danger">
                              {errors.last_name}
                            </small>
                          )}
                        </div>
                        <div className="field">
                          <label className="label">Password</label>
                          <div className="control">
                            <input
                              onChange={(event) => this.handleChange(event)}
                              type="password"
                              name="password"
                              className="input"
                            />
                          </div>
                          {errors.password && (
                            <small className="help is-danger">
                              {errors.password}
                            </small>
                          )}
                        </div>
                        <div className="field">
                          <label className="label">Confirm your password</label>
                          <div className="control">
                            <input
                              onChange={(event) => this.handleChange(event)}
                              type="password"
                              name="password_confirmation"
                              className="input"
                            />
                          </div>
                          {errors.password_confirmation && (
                            <small className="help is-danger">
                              {errors.password_confirmation}
                            </small>
                          )}
                        </div>
                        <button className="button is-success is-large">
                          Register
                        </button>
                      </form>
                    </div>
                  </div>

                  <div className="column"></div>
                </div>
              </div>
            </section>
          </div>
        </div >
      </main >
    )
  }

}
export default Register
