import React from 'react'
import axios from 'axios'

import SearchBar from './SearchBar'

class SearchRelease extends React.Component {
  constructor() {
    super()
    this.state = {
      query: '',
      release: {}
    }
  }

  handleChange(event) {
    const searchQuery = event.target.value
    this.setState({ query: searchQuery })
    // console.log(event)
    // console.log(searchQuery)
  }

  handleSubmit(event) {
    event.preventDefault()
    // console.log(event)
    const { query } = this.state
    axios.get(`https://api.discogs.com/releases/${query}`)
      // .then(res => console.log(res))
      .then(res => {
        this.setState({ release: res })
        console.log(this.state.release)
      })
      .catch(err => console.error(err))
  }

  render() {
    const { value } = this.state
    return (
      <section className="Hero hero is-fullheight">
        <div className="hero-body">
          <div className="container">
            <SearchBar value={value} handleSubmit={(event) => this.handleSubmit(event)} handleChange={(event) => this.handleChange(event)} />
            <div>
              {/* Hello */}
              {/* <h1>{this.state.release.artist.name}</h1> */}
            </div>
          </div>
        </div>

      </section>
    )
  }
}

export default SearchRelease