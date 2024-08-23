import React from "react";
import images from "../../constants/images.js";
import "./Register_Image.css";

const RegisterImage = () => {
    return (
        <div className="app__register-image">
            <img src={images.registerLeftside} alt="Register Leftside" />
        </div>
    );
};
export default RegisterImage;