import React, { useState, useEffect } from 'react'
import axios from 'axios'
import auth from '../lib/auth'

// Getting error 500 - Not fully implemented
const Profile = () => {
  const [data, setData] = useState(null)

  useEffect(() => {
    axios
      .get('/api/profile', {
        headers: { Authorization: `Bearer ${auth.getToken()}` }
      })
      .then((resp) => {
        setData(resp.data)
        console.log(data)
      })
      .catch((error) => console.error(error))
  }, [])

  return (
    <section className="Hero hero is-fullheight">
      <div className="hero-body">
        <div className="container">
          <h1 className="title is-1 has-text-centered">Who am I...</h1>
          <h2 className="subtitle is-2 has-text-centered">I'm Kurupt MF!</h2>
        </div>
      </div>
    </section>
  )
}
export default Profile