// Reducer-S1
import { createStore } from 'redux'

const reducer = (state, action) => {
  if (action.type === 'LOGGED-IN') {
    return { ...state, loggedIn: true }
  }
  return state
}

const store = createStore(reducer)