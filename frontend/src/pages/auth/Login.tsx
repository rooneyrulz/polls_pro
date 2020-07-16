import React, { useState } from 'react';

// BOOTSTRAP
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

const Login: React.FC = () => {
  const [formData, setFormData] = useState({ email: '', password: '' });

  const onChange = (e: any) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = (e: any) => console.log(formData);

  const { email, password } = formData;

  return (
    <div className='Login'>
      <div className='login-header'>
        <h2>Let's Login</h2>
      </div>
      <hr />
      <Form onSubmit={(e) => onSubmit(e)}>
        <Form.Group controlId='formBasicEmail'>
          <Form.Label>Email</Form.Label>
          <Form.Control
            type='email'
            name='email'
            value={email}
            placeholder='Enter email'
            onChange={(e) => onChange(e)}
          />
          <Form.Text className='text-muted'>
            We'll never share your email with anyone else.
          </Form.Text>
        </Form.Group>

        <Form.Group controlId='formBasicPassword'>
          <Form.Label>Password</Form.Label>
          <Form.Control
            type='password'
            name='password'
            value={password}
            placeholder='Password'
            onChange={(e) => onChange(e)}
          />
        </Form.Group>
        <Form.Group controlId='formBasicCheckbox'>
          <Form.Check type='checkbox' label='Check me out' defaultChecked />
        </Form.Group>
        <Button variant='primary' type='submit'>
          Login
        </Button>
      </Form>
    </div>
  );
};

export default Login;
