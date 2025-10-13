// JSX search model S2
state = {
  query: 'puppies',
  fetching: true,
  results: [
  ],
}

const Content = ({state}) => {
  if (!state.fetching && state.query) {
    return null
  }
  if (state,fetching) {
    return <p>Search for images of {state.query}</p>
  }
  return <p>Loading...</p>
} 
  