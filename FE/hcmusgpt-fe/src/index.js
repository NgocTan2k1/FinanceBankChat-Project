import ReactDOM from 'react-dom/client';

import { GoogleReCaptchaProvider } from 'react-google-recaptcha-v3';
import App from './App.js';
import GlobalStyles from './components/GlobalStyles';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    // <React.StrictMode>
    <GoogleReCaptchaProvider
        scriptProps={{
            async: true,
        }}
        reCaptchaKey={process.env.REACT_APP_SITE_KEY}
    >
        <GlobalStyles>
            <App />
        </GlobalStyles>
    </GoogleReCaptchaProvider>,
    // </React.StrictMode>,
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
