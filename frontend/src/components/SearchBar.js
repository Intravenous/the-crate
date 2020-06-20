//From project-2
import React from 'react'

const SearchBar = ({ handleChange, handleSubmit }) => {
  return (
    <div className="Search">
      <div className="container">
        <h1 className="title is-1 has-text-centered">Search...</h1>
        <div className="field is-horizontal has-addons">
          <div className="control is-expanded"></div>
          <input
            className="input is-medium"
            type="search"
            placeholder="Search by track number"
            // placeholder="Search by artist, track or album"
            // value={query}
            onChange={handleChange}
          />
          <div className="control">
            <button onClick={handleSubmit} className="button is-primary is-medium">Search</button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default SearchBar