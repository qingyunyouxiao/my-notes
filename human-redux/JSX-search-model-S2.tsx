import React from 'react'

export type SearchResult = { id: number; url: string }
export type State = { query: string; fetching: boolean; results: SearchResult[] }

export const state: State = {
  query: 'puppies',
  fetching: true,
  results: [
  ],
}

export function Content({ state }: { state: State }) {
  if (!state.fetching && state.query) {
    return <p>Search for images of {state.query}</p>
  }
  return <p>Loading...</p>
}


