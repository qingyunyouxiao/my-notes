// Props Passing
const List = ({list}) =>
 list.map(item => <Items key={item.objectID} item={item} />);

const Items = ({item}) => (
 <div>
   <span>
     <a href={item.url}>{item.title}</a>
   </span>
   <span>{item.author}</span>
   <span>{item.num_comments}</span>
   <span>{item.points}</span>
 </div>
);