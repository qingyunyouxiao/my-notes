import { combineReducers, createStore } from 'redux'

export type FloodAction = { type: 'APARTMENT_FLOODED' }
export type FurnitureAction = { type: 'BOUGHT_FURNITURE' } | FloodAction
export type AnyAction = FloodAction | FurnitureAction | { type: string }

const floodCountReducer = (state: number = 0, action: AnyAction): number => {
  if (action.type === 'APARTMENT_FLOODED') {
    return state + 1
  }

  return state
}

export type FurnitureState = { hasFurniture: boolean }
const initialFurnitureState: FurnitureState = { hasFurniture: true }
const furnitureReducer = (
  state: FurnitureState = initialFurnitureState,
  action: AnyAction
): FurnitureState => {
  if (action.type === 'APARTMENT_FLOODED') {
    return { hasFurniture: false }
  }

  if (action.type === 'BOUGHT_FURNITURE') {
    return { hasFurniture: true }
  }

  return state
}

export const rootReducer = combineReducers({
  floodCount: floodCountReducer,
  furniture: furnitureReducer,
})

export type RootState = ReturnType<typeof rootReducer>

export const store = createStore(rootReducer)


