import React from 'react'

export type SearchResult = { id: number; url: string }
export type State = { query: string; fetching: boolean; results: SearchResult[] }

export const state: State = {
  query: '',
  fetching: false,
  results: [
  ],
}

export function Content({ state }: { state: State }) {
  if (!state.fetching && state.query) {
    return null
  }
  return null
}


