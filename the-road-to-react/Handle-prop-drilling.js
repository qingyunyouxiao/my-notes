// Handle prop drilling
function PageOne() {
  const [user, setUser] = useState({});

  return (
    <UserStateContext.Provider value={{user, setUser}}>
      <MainLayout>
        <PageOneContent/>
      </MainLayout>
    </UserStateContext.Provider>
  )
}

function PageOneContent() {
  return (
    <UserStateContext.Consumer>
      {({user}) => (
        <UserBio user={user}/>
      )}
    </UserStateContext.Consumer>
  )
}