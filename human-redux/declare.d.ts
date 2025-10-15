declare module 'redux' {
  export function createStore(reducer: any): any
  export function combineReducers(reducers: any): any
}

declare module 'react' {    
  export function useState(initialState: any): any
}