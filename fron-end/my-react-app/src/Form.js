import React, { useState } from 'react';

function Form() {
  const [formData, setFormData] = useState({
    test: '',
    win: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };
  

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form Data:', formData.win,' test ' ,formData.test); // Log the form data before sending

    fetch('http://localhost:8000/signup/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('Signup response:', data);
      // Handle response from Django backend
    })
    .catch(error => {
      console.error('Error signing up:', error);
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="test">Test:</label>
        <input
          type="text"
          id="test"
          name="test"
          value={formData.test}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="win">Win:</label>
        <input
          type="number"
          id="win"
          name="win"
          value={formData.win}
          onChange={handleChange}
          required
          pattern="[0-9]*"
          inputMode="numeric"
        />
      </div>
      <button type="submit">Sign Up</button>
    </form>
  );
}

export default Form;
