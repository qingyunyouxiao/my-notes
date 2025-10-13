// JSX search model S3
state = {
  query: 'puppies',
  fetching: false,
  results: [
    { id: 1, url: 'https://puppies.com/one.png' },
    { id: 2, url: 'https://puppies.com/two.png' },
    { id: 3, url: 'https://puppies.com/three.png' },
  ],
}

const Content = ({state}) => {
  if (!state.fetching && state.query) {
    return null
  }

  if (state.fetching) {
    return <p>Searching for images of {state.query}...</p>
  } 
  
  if (state.results.length) {
    return (
      <ul>
        {state.results.map(result => (
          <li key={result.id}>
            <img src={result.url} alt="" />
          </li>
        ))}
      </ul>
    )
  }
  return <p>No results found for {state.query}</p>
}  