import { createStore } from 'redux'

export type AppState = { loggedIn: boolean }
export type Action = { type: string }

const initialState: AppState = { loggedIn: false }

const reducer = (state: AppState = initialState, action: Action): AppState => {
  if (action.type === 'LOGGED-IN') {
    return { ...state, loggedIn: true }
  }
  return state
}

export const store = createStore(reducer)


