import { axiosClient } from '../setup/axios.js';

const getCaptChaApi = () => {
    return axiosClient.get('/api/v1/configs');
};

const SignInApi = (data) => {
    return axiosClient.post('/token/', data);
};

const SignUpApi = (data) => {
    return axiosClient.post('/api/v1/authentication/register/', data);
};

const GetPublicKeyUser = () => {
    return axiosClient.get('/api/v1/configs/login');
};

export { SignInApi, SignUpApi, getCaptChaApi, GetPublicKeyUser };
