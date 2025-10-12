// Conditional Rendering in Lists
function TaskList() {
  const tasks = [
    { id: 1, text: 'Complete project proposal', priority: 'high', completed: false, dueDate: '2023-06-15' },
    { id: 2, text: 'Review pull requests', priority: 'medium', completed: true, dueDate: '2023-06-10' },
    { id: 3, text: 'Update documentation', priority: 'low', completed: false, dueDate: '2023-06-20' },
    { id: 4, text: 'Prepare presentation', priority: 'high', completed: false, dueDate: '2023-06-12' }
  ];

  // Get today's date for comparison
  const today = new Date();
  const formatDate = (dateString) => {
    const options = { month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };

  // Check if task is due soon (within 2 days)
  const isDueSoon = (dateString) => {
    const dueDate = new Date(dateString);
    const diffTime = dueDate - today;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays >= 0 && diffDays <= 2;
  };

  return (
    <ul className="task-list">
      {tasks.map(task => (
        <li 
          key={task.id} 
          className={`
            task 
            ${task.completed ? 'completed' : ''}
            priority-${task.priority}
            ${isDueSoon(task.dueDate) && !task.completed ? 'due-soon' : ''}
          `}
        >
          <div className="task-checkbox">
            <input type="checkbox" checked={task.completed} readOnly />
          </div>

          <div className="task-content">
            {task.completed ? <s>{task.text}</s> : task.text}

            <div className="task-meta">
              {task.priority === 'high' && <span className="badge priority">Urgent</span>}
              <span className="due-date">Due: {formatDate(task.dueDate)}</span>
              {isDueSoon(task.dueDate) && !task.completed && 
                <span className="badge warning">Due Soon!</span>
              }
            </div>
          </div>
        </li>
      ))}
    </ul>
  );
}
