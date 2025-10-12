// Better approach with unique IDs
const Items = [
  { id: 'task-1', text: 'Learn React' },
  { id: 'task-2', text: 'Build a project' },
  { id: 'task-3', text: 'Deploy to production' }
];

function List() {
  return (
    <ul>
      {Items.map(item => (
        <li key={item.id}>{item.text}</li>
      ))}
    </ul>
  );
}