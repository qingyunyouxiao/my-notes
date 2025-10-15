import React from 'react'

export type SearchResult = { id: number; url: string }
export type State = { query: string; fetching: boolean; results: SearchResult[] }

export const state: State = {
  query: 'puppies',
  fetching: false,
  results: [
    { id: 1, url: 'https://puppies.com/one.png' },
    { id: 2, url: 'https://puppies.com/two.png' },
    { id: 3, url: 'https://puppies.com/three.png' },
  ],
}

export function Content({ state }: { state: State }) {
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


