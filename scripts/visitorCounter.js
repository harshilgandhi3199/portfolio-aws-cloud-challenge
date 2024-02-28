fetch('https://rv1514d5nd.execute-api.us-east-1.amazonaws.com/Prod/counter')
            .then(response => response.json())
            .catch(error => console.error('Error:', error));