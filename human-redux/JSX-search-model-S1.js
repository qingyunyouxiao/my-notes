// JSX search model S1
state = {
  query: '',
  fetching: false,
  results: [
  ],
}

const Content = ({state}) => {
  if (!state.fetching && state.query) {
    return null
  }
} 
  