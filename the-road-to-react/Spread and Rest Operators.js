// Spread and Rest Operators
const List = ({list}) =>
  list.map(({ objectID, ...item }) => <Items key={objectID} {...item} />);

const Items = ({ title, url, author, num_comments, points }) => (
 <div>
   <span>
     <a href={url}>{title}</a>
   </span>
   <span>{author}</span>
   <span>{num_comments}</span>
   <span>{points}</span>
 </div>
);