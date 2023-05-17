/* eslint-disable jsx-a11y/alt-text */
import { faEye, faEyeSlash, faSpinner } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Form, Input } from 'antd';
import { useEffect } from 'react';
import { Link } from 'react-router-dom';

import Modal from 'antd/es/modal/Modal';
import classNames from 'classnames/bind';
import { useGoogleReCaptcha } from 'react-google-recaptcha-v3';
import logo from '../../img/logo.png';
import { GetPublicKeyUser } from '../../services/auth.js';
import styles from './SignIn.module.scss';
import { useLogin } from './hooks/login.js';

const cx = classNames.bind(styles);

function SignIn() {
    const loginHook = useLogin({});
    const {
        form,
        handleSetValueUpdate,
        showPassword,
        setShowPassword,
        handleSubmit,
        error,
        loading,
        setTokenCaptcha,
        tokenCaptcha,
        setError,
        content,
        open,
        setOpen,
        userAnymousKey,
        setUserAnymousKey,
    } = loginHook;
    const { executeRecaptcha } = useGoogleReCaptcha();

    // const handleReCaptchaVerify = useCallback(
    //     (event) => {
    //         if (!executeRecaptcha) {
    //             console.log('Execute recaptcha not yet available');
    //             return;
    //         }
    //         (async () => {
    //             try {
    //                 const token = await executeRecaptcha('signin');
    //                 setTokenCaptcha(token);
    //             } catch (error) {
    //                 console.log(error.response);
    //             }
    //         })();
    //     },
    //     [executeRecaptcha],
    // );

    useEffect(() => {
        if (!executeRecaptcha) {
            // console.log('Execute recaptcha not yet available');
            return;
        }
        (async () => {
            try {
                const token = await executeRecaptcha('signin');
                setTokenCaptcha(token);
            } catch (error) {
                // console.log(error.response);
            }
        })();
    }, [executeRecaptcha]);

    useEffect(() => {
        const getAnymousKey = async () => {
            try {
                const anymousKey = await GetPublicKeyUser();
                await setUserAnymousKey(anymousKey.data);
            } catch (error) {
                // console.log('test error anymousKey');
                // console.log(error.response);
            }
        };

        getAnymousKey();
    }, []);

    return (
        tokenCaptcha &&
        userAnymousKey && (
            <div className={cx('wrapper')}>
                <div className={cx('header')}>
                    <h3 className={cx('title')}>Đăng nhập</h3>
                    {/* eslint-disable-next-line jsx-a11y/alt-text */}
                    <img src={logo} className={cx('logo')}></img>
                </div>
                <div className={cx('container')}>
                    <Modal
                        className={cx('modal-warning')}
                        title="Lưu ý: Không thể đăng nhập!"
                        open={open}
                        onOk={async () => {
                            await setOpen(false);
                            setError((prev) => false);
                        }}
                        onCancel={async () => {
                            await setOpen(false);
                            setError((prev) => false);
                        }}
                        footer={null}
                    >
                        <div className={cx('container-warning')}>
                            <p className={cx('content-warning')}>{content}</p>
                            <img
                                className={cx('img-warning')}
                                src="https://cdn-icons-png.flaticon.com/512/4201/4201973.png"
                            />
                        </div>
                    </Modal>
                    <Form
                        form={form}
                        onValuesChange={handleSetValueUpdate}
                        onFinish={handleSubmit}
                        className={cx('container_form')}
                    >
                        <Form.Item name="username" className={cx('container_form_item')}>
                            <Input
                                type="text"
                                autoComplete="off"
                                placeholder="Nhập tên đăng nhập"
                                className={cx('container_form_item--input')}
                            />
                        </Form.Item>
                        <Form.Item name="password" className={cx('container_form_item')}>
                            <Input
                                type={showPassword ? 'text' : 'password'}
                                autoComplete="off"
                                placeholder="Mật khẩu"
                                className={cx('container_form_item--input')}
                            />
                        </Form.Item>
                        <div className={cx('icon')} onClick={() => setShowPassword(!showPassword)}>
                            {showPassword ? (
                                <FontAwesomeIcon icon={faEye} className={cx('icon_showpassword')} />
                            ) : (
                                <FontAwesomeIcon icon={faEyeSlash} className={cx('icon_hidepassword')} />
                            )}
                        </div>
                        {error ? <div className={cx('error-signin')}>{content}</div> : ''}
                        <button className={cx('signin-btn')}>
                            {loading && <FontAwesomeIcon className={cx('icon-loading-signin')} icon={faSpinner} />}
                            {!loading && `Đăng nhập`}
                        </button>
                        <Link to="/signup" className={cx('signup-link')}>
                            Bạn chưa có tài khoản?
                        </Link>
                    </Form>
                </div>
            </div>
        )
    );
}

export default SignIn;
