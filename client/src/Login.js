import React from 'react';
import './App.css';
import 'semantic-ui-css/semantic.min.css';
import { Form, Button , Message, Header, Grid} from 'semantic-ui-react';
import { Link } from 'react-router-dom';

function Login() {
    return (
        <body>
                <div className='LoginPage'>
                    <Header size='large' color='white' className='LoginTitle'>
                        Log in to Stocked
                    </Header>

                    <Form className='login-form'>
                        {/* Add error messages later to check for invalid requests */}
                        <Form.Input className='login-email' placeholder='E-mail Address' />
                        <Form.Input className='login-password' placeholder='Password' />
                        
                        <Link to='/dashboard'>
                            <Button className='login-button'>Login</Button>
                        </Link>
                    </Form>
                </div>

        </body>
    )
}

export default Login;