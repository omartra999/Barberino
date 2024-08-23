import React, { useState } from 'react';
import "./Register_Form.css"

const RegisterForm = () => {
    const[formData, setFormData] = useState({
        last_name: "",
        first_name: "",
        username: "",
        email: "",
        password: "",
        confirmPassword: ""
    });

    const handleChange = (e) => {
        const {name, value} = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (formData.password !== formData.confirmPassword) {
            alert("passwords do not match")
            return
        }

        try{
            const response = await fetch('http://localhost:8000/register',{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });
            if (!response.ok) {
                throw new Error(`Registeration failed: ${response.statusText}`);
            }
            if(response.ok){
                alert("Registration successful, a verification email has been sent, please verify your registration")
            }
        }catch(error){
            console.error('Error registering: ', error);
            alert("An error occurred during registration")
        }
        
    }
    return(
        <div className='app__register-form'>
        <h2>Register</h2>
        <form onSubmit={handleSubmit}>
            <div className='app__register-form-group'>
                <label htmlFor='last_name'>Last Name:</label><br></br>
                <input type='text' id='last_name' name='last_name' value={formData.last_name} onChange={handleChange} required />
            </div>
            
            <div className='app__register-form-group'>
                <label htmlFor='first_name'>First Name:</label><br></br>
                <input type='text' id='first_name' name='first_name' value={formData.first_name} onChange={handleChange} required />
            </div>

            <div className='app__register-form-group'>
                <label htmlFor='username'>Username:</label><br></br>
                <input type='text' id='username' name='username' value={formData.username} onChange={handleChange} required />
            </div>

            <div className='app__register-form-group'>
                <label htmlFor='email'>E-mail:</label><br></br>
                <input type='email' id='email' name='email' value={formData.email} onChange={handleChange} required />
            </div>

            <div className='app__register-form-group'>
                <label htmlFor='password'>Password:</label><br />
                <input type='password' id='password' name='password' value={formData.password} onChange={handleChange} required />
            </div>

            <div className='app__register-form-group'>
                <label htmlFor='confirmPassword'>Confirm Password:</label><br />
                <input type='password' id='confirmPassword' name='confirmPassword' value={formData.confirmPassword} onChange={handleChange} required />
            </div>
            <div className="app__register-button">
            <button type='submit'>Sign Up</button></div>
            
        </form>
        </div>
    )

};


export default RegisterForm