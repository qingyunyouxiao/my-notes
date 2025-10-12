// Function form with parameters
function List({Items}) {
  return Items.map(item => (
    <div key={item.ObjectID}>
    <span>
      <a href={item.url}>{item.title}</a>
    </span>
    </div>
  ));
}