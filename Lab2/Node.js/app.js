const axios = require('axios');
console.log('Making a GET request to JSONPlaceholder API...\n');
axios.get('https://jsonplaceholder.typicode.com/users/1')
  .then(response => {
    const user = response.data;
    console.log('User Information:');
    console.log(`Name: ${user.name}`);
    console.log(`Email: ${user.email}`);
    console.log(`Address: ${user.address.city}, ${user.address.street}`);
  })
  .catch(error => {
    console.error('Error:', error.message);
  });