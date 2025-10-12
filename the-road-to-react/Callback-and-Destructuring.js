// Callback and Destructuring
function List() {
  const Items = ["Item1", "Item2", "Item3"];
  return (
    <div>
      {Items.map((index, item) => {
        return <div key={index}>{item}</div>
      })}
    </div>
  );
}

const Search = ({ search, onSearch }) => (
 <div>
   <label htmlFor="search">Search: </label>
   <input
     id="search"
     type="text"
     value={search}
     onChange={onSearch}
   />
 </div>
);