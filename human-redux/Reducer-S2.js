// Reducer-S2
import { conbineReducers, createStore } from 'redux'

const floodCountReducer = (state = 0, action) => {
  if (action.type === 'APARTMENT_FLOODED') {
    return state + 1
  }

  return state
}

const initialFurnitureState = { hasFurniture: true }
const furnitureReducer = (state = initialFurnitureState, action) => {
  if (action.type === 'APARTMENT_FLOODED') {
    return { hasFurniture: false }
  }

  if (action.type === 'BOUGHT_FURNITURE') {
    return { hasFurniture: true }
  }

  return state
}

const rootReducer = conbineReducers({
  floodCount: floodCountReducer,
  furniture: furnitureReducer
})

const store = createStore(rootReducer)