import axios from 'axios';

const axiosClient = axios.create({
    baseURL: process.env.REACT_APP_API_ENDPOINT,
    headers: {
        'Content-Type': 'application/json',
    },
    withCredentials: false,
});

const axiosAuth = axios.create({
    baseURL: process.env.REACT_APP_API_ENDPOINT,
    headers: {
        'Content-Type': 'application/json',
    },
    withCredentials: false,
});

axiosAuth.interceptors.request.use(
    (config) => {
        if (!config.headers['Authorization']) {
            const accessToken = JSON.parse(localStorage.getItem('userInfo')).access;
            config.headers['Authorization'] = `Bearer ${accessToken}`;
        }
        return config;
    },
    (error) => Promise.reject(error),
);

export { axiosClient, axiosAuth };
