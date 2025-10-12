// Nested linked list
function ProjectList({userId, projects}) {
  return (
    <ul>
      {projects.map((project, index) => (
        <li key={`${userId}-project-${index}`}>{project}</li>
      ))}
    </ul>
  );
}

function UserRow({user}) {
  return (
    <tr>
      <td>{user.name}</td>
      <td>{user.role}</td>
      <td>
        <ProjectList userId={user.id} projects={user.projects} />
      </td>
    </tr>
  );
}

function UserDirectory() {
  const users = [
    { id: 1, name: 'Alex Johnson', role: 'Developer', projects: ['React Dashboard', 'API Gateway'] },
    { id: 2, name: 'Sam Taylor', role: 'Designer', projects: ['Brand Redesign'] },
    { id: 3, name: 'Jamie Smith', role: 'Product Manager', projects: ['Mobile App', 'Web Platform'] }
  ];

  return (
    <div className="user-directory">
      <h2>Team Members</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Role</th>
            <th>Projects</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <UserRow key={user.id} user={user} />
          ))}
        </tbody>
      </table>
    </div>
  );
}