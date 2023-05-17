import { Form } from 'antd';
import NodeRSA from 'node-rsa';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { GetPublicKeyUser, SignInApi } from '../../../services/auth.js';
import { GetPublicKey } from '../../../services/chat.js';

export const useLogin = ({ ...param }) => {
    const [open, setOpen] = useState(false);
    const [content, setContent] = useState('');
    const [form] = Form.useForm();
    const [valueUpdate, setValueUpdate] = useState({});
    const [loading, setLoading] = useState(false);
    const [showPassword, setShowPassword] = useState(false);
    const [error, setError] = useState(false);
    const [tokenCaptcha, setTokenCaptcha] = useState('');
    const navigate = useNavigate();
    const [userAnymousKey, setUserAnymousKey] = useState('');

    // eslint-disable-next-line react-hooks/exhaustive-deps
    // useEffect(() => {
    //     console.log('test');
    //     const getAnymousKey = async () => {
    //         const anymousKey = await GetPublicKeyUser();
    //         console.log('KeyUser response:', anymousKey);
    //     };

    //     getAnymousKey();

    //     // console.log('KeyUser response:', anymousKey);
    //
    // }, []);

    const checkExpireAnymousKey = async () => {
        console.log(userAnymousKey.expire);
        const expireDate = new Date(Date.parse(userAnymousKey.expire));
        const currentDate = new Date();
        if (expireDate.getTime() > currentDate.getTime()) {
            const fetchData = async () => {
                // console.log('===== lấy anymousKey =====');
                const anymousKey = await GetPublicKeyUser();
                await setUserAnymousKey(anymousKey.data);
            };
            await fetchData();
        }
    };

    async function handleSubmit() {
        setLoading(true);
        await checkExpireAnymousKey();

        if (valueUpdate.password && valueUpdate.username && userAnymousKey.public_key) {
            const publicKey = new NodeRSA();
            const pub = userAnymousKey.public_key;
            publicKey.importKey(pub, 'pkcs8-public');
            const passwordEncrypt = publicKey.encrypt(valueUpdate.password, 'base64');
            const usenameEncrypt = publicKey.encrypt(valueUpdate.username, 'base64');

            const data = {
                password: passwordEncrypt,
                username: usenameEncrypt,
                gcaptcha: tokenCaptcha,
            };

            await SignInApi(data)
                .then(async (response) => {
                    // console.log('response:', response);
                    localStorage.setItem(
                        'userInfo',
                        JSON.stringify({
                            access: response.data.access,
                            refresh: response.data.refresh,
                        }),
                    );
                    setError(false);
                    const getData = async () => {
                        const key = await GetPublicKey();
                        localStorage.setItem(
                            'key',
                            JSON.stringify({
                                public: key.data.public_key,
                                expire: key.data.expire,
                            }),
                        );
                    };
                    await getData();
                    setLoading(false);
                    navigate('/chat');
                })
                .catch((error) => {
                    if (error) {
                        // console.log('error:', error);
                        setError(true);
                        setContent('Tên đăng nhập hoặc mật khẩu không đúng!');
                        setOpen(true);
                    }
                });
        } else {
            setError(true);
        }
        setLoading(false);
    }

    function handleSetValueUpdate(value) {
        if (value) {
            setValueUpdate({ ...valueUpdate, ...value });
        }
    }
    return {
        form,
        handleSubmit,
        handleSetValueUpdate,
        loading,
        showPassword,
        setShowPassword,
        error,
        setError,
        valueUpdate,
        setValueUpdate,
        tokenCaptcha,
        setTokenCaptcha,
        open,
        setOpen,
        content,
        setContent,
        setUserAnymousKey,
        userAnymousKey,
    };
};

// export { useLogin };
