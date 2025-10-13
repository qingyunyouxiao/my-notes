// JSX search model S4
state = {
  query: 'puppies',
  fetching: false,
  results: [
  ],
}

const Content = ({state}) => {
  if (!state.fetching && state.query) {
    return null
  }
  if (state,fetching) {
    return <p>Search for images of {state.query}...</p>
  }
  
  if (state.results.length) {
    return (
      <ul>
        {state.results.map(result => (
          <li>
            <img src={result.url}/>
          </li>
        ))}
      </ul>
    )
  }
}    