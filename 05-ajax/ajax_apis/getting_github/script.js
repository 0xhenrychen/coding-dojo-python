function requestGitHubUser()
{
    fetch("https://api.github.com/users/0xhenrychen")
    .then(response => response.json())
    .then(coderData => console.log(coderData))
    .catch(err => console.log(err))
}

function displayGitHubUser(data)
{
    const name = data.login[]
}