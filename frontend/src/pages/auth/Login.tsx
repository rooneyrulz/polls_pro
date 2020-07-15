import React from 'react';

// BOOTSTRAP
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

const Login: React.FC = () => {
  return (
    <div className='Login'>
      <div className='login-header'>
        <h2>Let's Login</h2>
      </div>
      <hr />
      <Form>
        <Form.Group controlId='formBasicEmail'>
          <Form.Label>Email</Form.Label>
          <Form.Control type='email' placeholder='Enter email' />
          <Form.Text className='text-muted'>
            We'll never share your email with anyone else.
          </Form.Text>
        </Form.Group>

        <Form.Group controlId='formBasicPassword'>
          <Form.Label>Password</Form.Label>
          <Form.Control type='password' placeholder='Password' />
        </Form.Group>
        <Form.Group controlId='formBasicCheckbox'>
          <Form.Check type='checkbox' label='Check me out' defaultChecked />
        </Form.Group>
        <Button variant='primary' type='submit'>
          Submit
        </Button>
      </Form>
    </div>
  );
};

export default Login;
