import React from 'react';
import { RegisterForm, RegisterImage } from "../../components";
import "./Register.css"

function Register(){
    return(
        <div className="app__register">
            <RegisterForm />
            <RegisterImage />
        </div>
    )
}
export default Register;